# 10.	Отримати список студентів зазначених груп, 
#		яким заданий викладач поставив деяку оцінку 
#		за іспит з певних дисциплін, в зазначених семестрах, 
#		за деякий період. 

drop procedure if exists task_10;
delimiter $$
create procedure task_10(
	group_code varchar(10),
	teacher_id int,
    semester_from int,
    semester_to int
)
begin
	drop table if exists temp_table;
    create table temp_table select * from `session`;
    if `group_code` != -1 then 
		delete t1 from temp_table t1 join `students` t2 on
        t1.student_id = t2.student_id and t2.group_code != `group_code`;
	end if;
    if `teacher_id` != -1 then
		delete from temp_table where temp_table.teacher_id != `teacher_id`;
	end if;
    if `semester_from` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester  < `semester_from`;
	end if;
    if `semester_to` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester > `semester_to`;
	end if;
    select t1.student_id, t2.`name`, t2.`group_code`, t3.`subject_name`, t1.`mark` 
    from temp_table t1 join `students` t2 on t1.student_id = t2.student_id
    join `subjects` t3 on t1.subject_id = t3.subject_id;
    drop table temp_table;
end $$