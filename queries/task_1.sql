# 1. 	Отримати перелік і загальне число студентів зазначених груп 
# 	 	або вказаного курсу (курсів) факультету повністю, за статевою ознакою, 
#		року, віком, ознакою наявності дітей, за ознакою отримання і розміром стипендії. 

drop procedure if exists task_1;
delimiter $$
create procedure task_1(
	group_code varchar(10), # none is ''
    study_year int,			# none is -1
    faculty_id int,			# none is -1
    sex varchar(1),			# none is ''
    age int,				# none is -1
    has_children tinyint,	# none is -1
    scholarship int			# none is -1
)
begin
	drop table if exists temp_table;
    create table temp_table select * from students;
	if `faculty_id` != -1 then 
		delete t1 from temp_table t1 join `groups` t2 on 
        t1.group_code = t2.group_code join `chairs` t3 on
        t2.chair_id = t3.chair_id and t3.faculty_id != `faculty_id`; 
        end if;
	if `study_year` != -1 then
		delete t1 from temp_table t1 join `groups` t2 on 
        t1.group_code = t2.group_code and 
        t2.study_year != `study_year`; 
        end if;
	if `group_code` != '' then 
		delete from temp_table where temp_table.group_code != `group_code`; end if;
	if `sex` != '' then
		delete from temp_table where temp_table.sex != `sex`; end if;
	if `age` != -1 then
		delete from temp_table where (select timestampdiff(year, '2002-05-01', now()) != `age`); end if;
	if `has_children` != -1 then
		delete from temp_table where temp_table.has_children != `has_children`; end if;
	if `scholarship` != -1 then
		delete from temp_table where temp_table.scholarship != `scholarship`; end if;
    select * from temp_table;
    drop table temp_table;
end $$