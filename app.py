from flask import Flask, render_template, request, redirect, send_file, url_for, current_app
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from Controllers.Files_PracticeController import *
from docxtpl import DocxTemplate
import os
import zipfile
import tempfile
import shutil
import io
from datetime import datetime

from Controllers.GroupsController import GroupsController
from Controllers.StudentsController import StudentsController
from Controllers.UserController import UsersController

# создать объект класса Flask
application = Flask(__name__)
application.secret_key = 'la'
# для библиотеки login_manager добавил объект
# этот объект управляет авторизацией
login_manager = LoginManager(application)
@login_manager.user_loader
def user_loader(id):
    return UsersController.show(int(id))
# Маршрут главной страницы
# Добавить методы работы с данными POST и GET

@application.route('/', methods = ['POST', 'GET'])
def home():
    title = "Вход"
    message = ''


    #Проверка метода
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if UsersController.auth(login, password):
            #Создает сессию для пользователя который прошел аутентификацию
            user = UsersController.show_login(login)
            login_user(user)
            print(user)
            print(type(user.role_id))
            if current_user.role_id.id == 1:
                return redirect('/vhod')
            elif current_user.role_id.id == 2:
                return redirect('/teacher')
        else:
            message = 'Не верный логин или пароль'
    return render_template('index.html',
                           title = title,
                           message = message
                           )

@application.route('/registracia', methods = ['POST', 'GET'])
def registration_site():
    title = 'Регистрация'
    message = ''
    if request.method == 'POST':
        print('1223')
        login = request.form.get('login')
        password = request.form.get('password')
        password1 = request.form.get('password1')
        print('3333')
        if UsersController.registration(login, password):
            print('1233')
            user = UsersController.show_login(login)
            if password == password1:
                print("1243")
                UsersController.auth(login, password)
                login_user(user)
                return redirect('/vhod')
                # Получаем пользователя
            else:
                message = 'Пароли не совпадают'
        else:
            message = 'Ошибка авторизации после регистрации'
        # else:
        #     message = 'Такой логин уже существует'

    return render_template('registration.html', title=title,message=message)

@application.route('/vhod', methods = ['POST', 'GET'])
@login_required
def vhod():
        title = "Группы студентов"
        if current_user.role_id.id == 1:
            groups = GroupsController.get()



            return render_template('group_students.html',
                                   title=title, groups=groups)
        else:
            return redirect('/logout')

@application.route('/list_students/<int:group_id>', methods=['POST', 'GET'])
@login_required
def studenti(group_id):
    title = "Студенты"
    if current_user.role_id.id == 1:
        students = StudentsController.show_group(group_id)
        group=GroupsController.show(group_id)
        group_name = students[0].group_id.name if students else "Группа не найдена"  # Берём название из первого студента
        return render_template('list_students.html',
                             title=title,
                             students=students,
                             group_name=group_name,
                            group=group
                               )
    else:
        return redirect('/logout')


@application.route('/data-students/<int:student_id>', methods=['POST', 'GET'])
@login_required
def data_students(student_id):
    if current_user.role_id.id == 1:
        student = StudentsController.show(student_id)
        if not student:
            return "Студент не найден", 404

        group_name = student.group_id.name if student.group_id else "Группа не указана"

        return render_template('data_students.html',
                           title="Выбор нужных документов",
                           student=student,
                           group_name=group_name)
    else:
        return redirect('/logout')


@application.route('/fill_data_students/<int:student_id>', methods=['GET', 'POST'])
@login_required
def zapolnenie_dokumentov(student_id):
    if current_user.role_id.id != 1:
        return redirect('/logout')

    student = StudentsController.show(student_id)

    if request.method == 'POST':
        try:
            # Получаем данные из формы
            form_data = {
                'company_name': request.form.get('company_name'),
                'company_address': request.form.get('company_address'),
                'start_day': request.form.get('start_day'),
                'start_month': request.form.get('start_month'),
                'end_day': request.form.get('end_day'),
                'end_month': request.form.get('end_month'),
                'practice_time': request.form.get('practice_time'),
                'manager_lastname': request.form.get('manager_lastname'),
                'manager_firstname': request.form.get('manager_firstname'),
                'manager_middlename': request.form.get('manager_middlename'),
                'manager_position': request.form.get('manager_position'),
                'company_phone': request.form.get('company_phone'),
                'school_manager_lastname': request.form.get('school_manager_lastname'),
                'school_manager_firstname': request.form.get('school_manager_firstname'),
                'school_manager_middlename': request.form.get('school_manager_middlename'),
                'practice_name': request.form.get('practice_name'),
                'module_name': request.form.get('module_name'),
                'work_type': request.form.get('work_type'),
                'method_manager_lastname': request.form.get('method_manager_lastname'),
                'method_manager_firstname': request.form.get('method_manager_firstname'),
                'method_manager_middlename': request.form.get('method_manager_middlename')
            }

            # Обработка файла (если нужна)
            if 'practice_file' in request.files:
                file = request.files['practice_file']
                if file.filename != '':
                    # Сохраняем файл
                    file.save(f'uploads/{file.filename}')

            # Здесь можно сохранить данные в БД

            # Перенаправляем на генерацию документов
            return redirect(url_for('generate_docs', student_id=student_id))

        except Exception as e:
            return f"Ошибка обработки данных: {str(e)}", 500

    # GET запрос - отображаем форму
    return render_template('fill_data_students.html',
                           title="Заполнение документов",
                           student=student)


@application.route('/data-students-multiple', methods=['POST'])
@login_required
def data_students_multiple():
    if current_user.role_id.id == 1:
        student_ids = request.form.getlist('selected_students')
        if not student_ids:
            return redirect(request.referrer or url_for('vhod'))

        students = [StudentsController.show(int(student_id)) for student_id in student_ids]
        if not students:
            return "Студенты не найдены", 404

        # Проверяем, что все студенты из одной группы
        group_ids = {student.group_id.id for student in students if student.group_id}
        if len(group_ids) != 1:
            return "Студенты должны быть из одной группы", 400

        group_name = students[0].group_id.name if students[0].group_id else "Группа не указана"

        return render_template('data_students_multiple.html',
                               students=students,
                               group_name=group_name)
    else:
        return redirect('/logout')

@application.route('/logout')
def logout():
    logout_user()
    return redirect('/')


# Для одного студента
@application.route('/generate_doc/<int:student_id>', methods=['POST'])
@login_required
def generate_single_doc(student_id):
    student = StudentsController.show(student_id)
    if not student:
        return "Студент не найден", 404
    return generate_documents([student], request.form)


# Для нескольких студентов
@application.route('/generate_docs', methods=['POST'])
@login_required
def generate_multiple_docs():
    student_ids = request.form.getlist('student_ids')
    students = [StudentsController.show(sid) for sid in student_ids if StudentsController.show(sid)]
    if not students:
        return "Не выбрано студентов", 400
    return generate_documents(students, request.form)


# Общая функция генерации
def generate_documents(students, form_data):
    try:
        # Подготовка общих данных
        common_data = {
            'company_name': form_data['company_name'],
            'company_address': form_data['company_address'],
            'start_day': form_data['start_day'],
            'start_month': form_data['start_month'],
            'end_day': form_data['end_day'],
            'end_month': form_data['end_month'],
            'year': datetime.now().year,
            'method_d_director_s': form_data['manager_lastname'],
            'method_d_director_n': form_data['manager_firstname'],
            'method_d_director_m': form_data['manager_middle_name'],
            'pm_number': '06',
            'pm_name': 'Сопровождение информационных систем'
        }

        # Создаем временную папку
        temp_dir = tempfile.mkdtemp()
        zip_paths = []

        for student in students:
            # Индивидуальные данные
            student_data = {
                'student_name': student.name,
                'student_surename': student.surename,
                'student_middle_name': student.middle_name,
                'group_number': student.group_id.name,
                'specialization': student.specialization,
                'birth_date': student.date_of_birth,
                'course': student.group_id.course,

            }

            # Генерация документов
            templates = Files_Practice.select()
            zip_filename = os.path.join(temp_dir, f"docs_{student.id}.zip")

            with zipfile.ZipFile(zip_filename, 'w') as zip_file:
                for template in templates:
                    doc = DocxTemplate(io.BytesIO(template.file_data))
                    doc.render({**common_data, **student_data})
                    output = io.BytesIO()
                    doc.save(output)
                    zip_file.writestr(
                        f"{template.name}_{student.surename}.docx",
                        output.getvalue()
                    )
            zip_paths.append(zip_filename)

        # Создаем итоговый архив
        final_zip = io.BytesIO()
        with zipfile.ZipFile(final_zip, 'w') as final_zip_file:
            for path in zip_paths:
                final_zip_file.write(path, os.path.basename(path))

        # Очистка
        shutil.rmtree(temp_dir)
        final_zip.seek(0)

        # Имя файла
        filename = f"Документы_{students[0].surename}.zip" if len(
            students) == 1 else f"Документы_{len(students)}_студентов.zip"

        return send_file(
            final_zip,
            as_attachment=True,
            download_name=filename,
            mimetype='application/zip'
        )

    except Exception as e:
        current_app.logger.error(f"Ошибка генерации: {str(e)}")
        return f"Ошибка при генерации: {str(e)}", 500

@application.route('/student/<int:student_id>')
@login_required
def student_form(student_id):
    student = StudentsController.show(student_id)
    return render_template('form.html', student=student)


@application.route('/group/<int:group_id>')
@login_required
def group_form(group_id):
    students = StudentsController.show_group(group_id)
    return render_template('form.html', students=students)
if __name__ == "__main__":
    application.run(debug=True)