# 12.	Отримати список керівників дипломних робіт 
#		по заданій кафедрі або факультету повністю 
#		і окремо по деяким категоріям викладачів. 

drop procedure if exists task_12;
delimiter $$
create procedure task_12(
	faculty_id int,
	chair_id int,
    title varchar(45)
)
begin
	drop table if exists temp_table;
    create table temp_table select diploma_teacher_id from `students` 
		where diploma_teacher_id is not NULL group by diploma_teacher_id;
    if `chair_id` != -1 then
		delete t1 from temp_table t1 join `teachers` t2 on t1.diploma_teacher_id = t2.teacher_id
        and t2.chair_id != `chair_id`;
	end if;
    if `faculty_id` != -1 then 
		delete t1 from temp_table t1 join `teachers` t2 on t1.diploma_teacher_id = t2.teacher_id
        join `chairs` t3 on t2.chair_id = t3.chair_id and t3.faculty_id != `faculty_id`;
	end if;
    if `title` != -1 then
		delete t1 from temp_table t1 join `teachers` t2 on t1.diploma_teacher_id = t2.teacher_id
        and t2.title != `title`;
	end if;
    select * from `teachers` t1 join temp_table t2 on t1.teacher_id = t2.diploma_teacher_id;
    drop table temp_table;
end $$