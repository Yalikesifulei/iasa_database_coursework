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
    

queries = {
    'task_1': Query(''' Отримати перелік і загальне число студентів зазначених груп 
                    	або вказаного курсу (курсів) факультету повністю, за статевою ознакою, 
                        року, віком, ознакою наявності дітей, за ознакою отримання і розміром стипендії. ''',
        [
            QueryField('group_code', 'Група', 'list', [ListElement(group_code[0]) for group_code in groups_list]), 
            QueryField('study_year', 'Рік навчання', 'list', [ListElement(1), ListElement(2), ListElement(3), ListElement(4)]),
            QueryField('faculty_id', 'Факультет', 'list', [ListElement(faculty[0], faculty[1]) for faculty in faculties_list]), 
            QueryField('sex', 'Стать', 'list', [ListElement('ч', 'чоловіча'), ListElement('ж', 'жіноча')]), 
            QueryField('age', 'Вік'),
            QueryField('has_children', 'Наявність дітей', 'list', [ListElement(0, 'немає'), ListElement(1, 'є')]), 
            QueryField('scholarship', 'Розмір стипендії', 'list', [ListElement(0, 'немає'), 
                                                                ListElement(1300, 'звичайна'),
                                                                ListElement(1892, 'підвищена')])
        ]),
    'task_2': Query(''' Отримати список і загальне число викладачів зазначених кафедр 
                        або зазначеного факультету повністю або зазначених категорій 
                        (асистенти, доценти, професори і т.д.) за статевою ознакою, 
                        року, віком, ознакою наявності та кількості дітей, розміру 
                        заробітної плати, є аспірантами, захистили кандидатські, 
                        докторські дисертації в зазначений період. ''',
        [
            QueryField('chair_id', 'Кафедра', 'list', [ListElement(chair[0], chair[1]) for chair in chairs_list]),
            QueryField('faculty_id', 'Факультет', 'list', [ListElement(faculty[0], faculty[1]) for faculty in faculties_list]), 
            QueryField('title', 'Посада', 'list', [ListElement('асистент'),
                                                ListElement('викладач'),
                                                ListElement('старший викладач'),
                                                ListElement('доцент'),
                                                ListElement('професор')]),
            QueryField('sex', 'Стать', 'list', [ListElement('ч', 'чоловіча'), ListElement('ж', 'жіноча')]), 
            QueryField('age', 'Вік'),
            QueryField('children', 'Кількість дітей'),
            QueryField('salary', 'Зарплата, більше ніж'),
            QueryField('phd_date_start', 'Захист кандидатської, від','date'),
            QueryField('phd_date_end', 'Захист кандидатської, до', 'date'),
            QueryField('prof_date_start', 'Захист докторської, від', 'date'),
            QueryField('prof_date_end', 'Захист докторської, до', 'date')
        ])
}