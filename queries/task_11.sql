# 11.	Отримати список студентів і тим дипломних робіт 
# 		на зазначеній кафедрі або у зазначеного викладача. 

drop procedure if exists task_11;
delimiter $$
create procedure task_11(
	chair_id int,
    teacher_id int
)
begin
	drop table if exists temp_table;
    create table temp_table select * from `students` where diploma_teacher_id is not NULL;
    if `teacher_id` != -1 then
		delete from temp_table where temp_table.diploma_teacher_id != `teacher_id`;
	end if;
    if `chair_id` != -1 then
		delete t1 from temp_table t1 join `teachers` t2 on t1.diploma_teacher_id = t2.teacher_id
        and t2.chair_id != `chair_id`;
	end if;
    select t1.`student_id`, t1.`group_code`, t1.`name`, t1.`diploma_teacher_id`,
    t2.`name` as `diploma_teacher_name`, t1.`diploma_topic` from temp_table t1
    join `teachers` t2 on t1.diploma_teacher_id = t2.teacher_id;
    drop table temp_table;
end $$