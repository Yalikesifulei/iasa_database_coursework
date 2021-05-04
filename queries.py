from db_connect import db

class Query():
    def __init__(self, description, fields):
        self.description = description
        self.fields = fields

class QueryField():
    def __init__(self, real_name, display_name, field_type='text', unique_values=None):
        self.real_name = real_name
        self.display_name = display_name
        self.field_type = field_type
        self.unique_values = unique_values

class ListElement:
    def __init__(self, real_name, display_name=None):
        self.real_name = str(real_name)
        if display_name:
            self.display_name = display_name  
        else:
            self.display_name = real_name      

with db.cursor() as cursor:
    cursor.execute(f'select `faculty_id`, `faculty_name` from `faculties`')
    faculties_list = cursor.fetchall()
    cursor.execute(f'select `chair_id`, `chair_name` from `chairs`')
    chairs_list = cursor.fetchall()
    cursor.execute(f'select `group_code` from `groups`')
    groups_list = cursor.fetchall()
    cursor.execute(f'select `subject_id`, `subject_name` from `subjects`')
    subjects_list = cursor.fetchall()
    cursor.execute(f'select `teacher_id`, `name` from `teachers`')
    teachers_list = cursor.fetchall()

faculties_list = [ListElement(faculty[0], faculty[1]) for faculty in faculties_list]
chairs_list = [ListElement(chair[0], chair[1]) for chair in chairs_list]
groups_list = [ListElement(group_code[0]) for group_code in groups_list]
subjects_list = sorted(list(subjects_list), key=lambda t: t[1])
subjects_list = [ListElement(subject[0], subject[1]) for subject in subjects_list]
study_year_list = [ListElement(1), ListElement(2), ListElement(3), ListElement(4)]
teachers_list = sorted(list(teachers_list), key=lambda t: t[1])
teachers_list = [ListElement(teacher[0], teacher[1]) for teacher in teachers_list]
teacher_title_list = [
    ListElement('асистент'),
    ListElement('викладач'),
    ListElement('старший викладач'),
    ListElement('доцент'),
    ListElement('професор')
]
lesson_type_list = [
    ListElement('lec', 'лекція'),
    ListElement('prac', 'практика'),
    ListElement('lab', 'лабораторні'),
    ListElement('cw', 'курсова робота')
]
marks_list = [
    ListElement('A', 'Відмінно (95-100)'),
    ListElement('B', 'Дуже добре (85-94)'),
    ListElement('C', 'Добре (75-84)'),
    ListElement('D', 'Задовільно (65-74)'),
    ListElement('E', 'Достатньо (60-64)')
]
semester_list = [
    ListElement(1, '1 курс, 1 семестр'),
    ListElement(2, '1 курс, 2 семестр'),
    ListElement(3, '2 курс, 1 семестр'),
    ListElement(4, '2 курс, 2 семестр'),
    ListElement(5, '3 курс, 1 семестр'),
    ListElement(6, '3 курс, 2 семестр'),
    ListElement(7, '4 курс, 1 семестр'),
    ListElement(8, '4 курс, 2 семестр')
]

queries = {
    'task_1': Query('''
            1. Отримати перелік і загальне число студентів зазначених груп 
                або вказаного курсу (курсів) факультету повністю, за статевою ознакою, 
                року, віком, ознакою наявності дітей, за ознакою отримання і розміром стипендії.''',
        [
            QueryField('group_code', 'Група', 'list', groups_list), 
            QueryField('study_year', 'Курс', 'list', study_year_list),
            QueryField('faculty_id', 'Факультет', 'list', faculties_list), 
            QueryField('sex', 'Стать', 'list', [ListElement('ч', 'чоловіча'), ListElement('ж', 'жіноча')]), 
            QueryField('age', 'Вік'),
            QueryField('has_children', 'Наявність дітей', 'list', [ListElement(0, 'немає'), ListElement(1, 'є')]), 
            QueryField('scholarship', 'Розмір стипендії', 'list', [ListElement(0, 'немає'), 
                                                                   ListElement(1300, 'звичайна'),
                                                                   ListElement(1892, 'підвищена')])
        ]),
    'task_2': Query('''
            2. Отримати список і загальне число викладачів зазначених кафедр 
            або зазначеного факультету повністю або зазначених категорій 
            (асистенти, доценти, професори і т.д.) за статевою ознакою, 
            року, віком, ознакою наявності та кількості дітей, розміру 
            заробітної плати, є аспірантами, захистили кандидатські, 
            докторські дисертації в зазначений період.''',
        [
            QueryField('faculty_id', 'Факультет', 'list', faculties_list), 
            QueryField('chair_id', 'Кафедра', 'list', chairs_list),
            QueryField('title', 'Посада', 'list', teacher_title_list),
            QueryField('sex', 'Стать', 'list', [ListElement('ч', 'чоловіча'), ListElement('ж', 'жіноча')]), 
            QueryField('age', 'Вік'),
            QueryField('children', 'Кількість дітей'),
            QueryField('salary', 'Зарплата, більше ніж'),
            QueryField('phd_date_start', 'Захист кандидатської, від','date'),
            QueryField('phd_date_end', 'Захист кандидатської, до', 'date'),
            QueryField('prof_date_start', 'Захист докторської, від', 'date'),
            QueryField('prof_date_end', 'Захист докторської, до', 'date')
        ]),
    'task_3': Query('''
            3. Отримати перелік і загальне число тем кандидатських 
            і докторських дисертацій, які захистили співробітники 
            зазначеної кафедри для зазначеного факультету.''',
        [
            QueryField('faculty_id', 'Факультет', 'list', faculties_list),
            QueryField('chair_id', 'Кафедра', 'list', chairs_list),
        ]),
    'task_4': Query('''
            4.	Отримати перелік кафедр, які проводять заняття 
            у зазначеній групі або на зазначеному курсі 
            вказаного факультету в зазначеному семестрі, 
            або за вказаний період.''',
        [
            QueryField('faculty_id', 'Факультет', 'list', faculties_list),
            QueryField('group_code', 'Група', 'list', groups_list),
            QueryField('semester_from', 'Семестр, від', 'list', semester_list),
            QueryField('semester_to', 'Семестр, до', 'list', semester_list)
        ]),
    'task_5': Query('''
            5.	Отримати список і загальне число викладачів, 
            які проводили (проводять) заняття по вказаній 
            дисципліні в зазначеній групі або на зазначеному 
            курсі вказаного факультету.''',
        [
            QueryField('subject_name', 'Дисципліна', 'list', subjects_list),
            QueryField('faculty_id', 'Факультет', 'list', faculties_list),
            QueryField('semester_from', 'Семестр, від', 'list', semester_list),
            QueryField('semester_to', 'Семестр, до', 'list', semester_list),
            QueryField('group_code', 'Група', 'list', groups_list)
        ]),
    'task_6': Query('''
            6.	Отримати перелік і загальне число викладачів, 
            які проводили (проводять) лекційні, семінарські 
            та інші види занять у зазначеній групі або на 
            зазначеному курсі вказаного факультету в зазначеному 
            семестрі, або за вказаний період.''',
        [
            QueryField('lesson_type', 'Вид заняття', 'list', lesson_type_list),
            QueryField('faculty_id', 'Факультет', 'list', faculties_list),
            QueryField('semester_from', 'Семестр, від', 'list', semester_list),
            QueryField('semester_to', 'Семестр, до', 'list', semester_list),
            QueryField('group_code', 'Група', 'list', groups_list)
        ]),
    'task_7': Query('''
            7.	Отримати список і загальне число студентів 
            зазначених груп, які здали залік або іспит
            з вказаною дисципліни зі встановленою оцінкою.''',
        [
            QueryField('group_code', 'Група', 'list', groups_list),
            QueryField('subject_id', 'Дисципліна', 'list', subjects_list),
            QueryField('mark', 'Оцінка', 'list', marks_list)
        ]),
    'task_8': Query('''
            8.	Отримати список і загальне число студентів 
            зазначених груп або вказаного курсу зазначеного 
            факультету, які здали зазначену сесію на відмінно, 
            без трійок, без двійок.''',
        [
            QueryField('faculty_id', 'Факультет', 'list', faculties_list),
            QueryField('group_code', 'Група', 'list', groups_list),
            QueryField('semester_from', 'Семестр, від', 'list', semester_list),
            QueryField('semester_to', 'Семестр, до', 'list', semester_list),
            QueryField('mark', 'Мін. оцінка, від', 'list', marks_list)
        ]),
    'task_9': Query('''
            9.	Отримати перелік викладачів, які беруть (брали) 
            іспити в зазначених групах, із зазначених дисциплін, 
            в зазначеному семестрі.''',
        [
            QueryField('group_code', 'Група', 'list', groups_list),
            QueryField('subject_id', 'Дисципліна', 'list', subjects_list),
            QueryField('semester_from', 'Семестр, від', 'list', semester_list),
            QueryField('semester_to', 'Семестр, до', 'list', semester_list)
        ]),
    'task_10': Query('''
            10.	Отримати список студентів зазначених груп, 
            яким заданий викладач поставив деяку оцінку 
            за іспит з певних дисциплін, в зазначених семестрах, 
            за деякий період.''',
        [
            QueryField('group_code', 'Група', 'list', groups_list),
            QueryField('teacher_id', 'Викладач', 'list', teachers_list),
            QueryField('semester_from', 'Семестр, від', 'list', semester_list),
            QueryField('semester_to', 'Семестр, до', 'list', semester_list)
        ]),
    'task_11': Query('''
            11.	Отримати список студентів і тим дипломних робіт 
            на зазначеній кафедрі або у зазначеного викладача.''',
        [
            QueryField('chair_id', 'Кафедра', 'list', chairs_list),
            QueryField('teacher_id', 'Викладач', 'list', teachers_list)
        ]),
    'task_12': Query('''
            12.	Отримати список керівників дипломних робіт 
            по заданій кафедрі або факультету повністю 
            і окремо по деяким категоріям викладачів. ''',
        [
            QueryField('faculty_id', 'Факультет', 'list', faculties_list),
            QueryField('chair_id', 'Кафедра', 'list', chairs_list),
            QueryField('title', 'Посада', 'list', teacher_title_list)
        ]),
    'task_13': Query('''
            13.	Отримати навантаження викладачів (назва дисципліни, кількість годин), 
            її обсяг на окремі види занять і загальне навантаження в зазначеному 
            семестрі для конкретного викладача або для викладачів зазначеної кафедри. ''',
        [
            QueryField('teacher_id', 'Викладач', 'list', teachers_list),
            QueryField('chair_id', 'Кафедра', 'list', chairs_list)
        ])
}