from db_connect import db

class QueryField():
    def __init__(self, real_name, display_name, field_type='text', unique_values=None):
        self.real_name = real_name
        self.display_name = display_name
        self.field_type = field_type
        self.unique_values = unique_values

class ListElement:
    def __init__(self, real_name, display_name=None):
        self.real_name = real_name
        if display_name:
            self.display_name = display_name  
        else:
            self.display_name = real_name      

with db.cursor() as cursor:
    cursor.execute(f'select `group_code` from `groups`')
    groups_list = cursor.fetchall()

queries = {
    'task_1': [QueryField('group_code', 'Група', 'list', [ListElement(group_code[0]) for group_code in groups_list]), 
               QueryField('study_year', 'Рік навчання', 'list', [ListElement('1'), ListElement('2'), ListElement('3'), ListElement('4')]),
               QueryField('faculty_id', 'Факультет', 'list', [ListElement('0', 'Інститут прикладного функціонального аналiзу'),
                                                              ListElement('1', 'Факультет інженерно-обчислювальних технологій'),
                                                              ListElement('2', 'Холодноенергетичний факультет')]), 
               QueryField('sex', 'Стать', 'list', [ListElement('ч', 'чоловіча'), ListElement('ж', 'жіноча')]), 
               QueryField('age', 'Вік'),
               QueryField('has_children', 'Наявність дітей', 'list', [ListElement('0', 'немає'), ListElement('1', 'є')]), 
               QueryField('scholarship', 'Розмір стипендії', 'list', [ListElement('0', 'немає'), 
                                                                      ListElement('1300', 'звичайна'),
                                                                      ListElement('1892', 'підвищена')])]
}