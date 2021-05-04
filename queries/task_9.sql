# 9.	Отримати перелік викладачів, які беруть (брали) 
#		іспити в зазначених групах, із зазначених дисциплін, 
#		в зазначеному семестрі. 

drop procedure if exists task_9;
delimiter $$
create procedure task_9(
	group_code varchar(10),
    subject_id int,
    semester_from int,
    semester_to int
)
begin
	drop table if exists temp_table;
    create table temp_table select * from `session`;
    if `subject_id` != -1 then 
		delete from temp_table where temp_table.subject_id != `subject_id`;
	end if;
    if `group_code` != -1 then 
		delete t1 from temp_table t1 join `students` t2 on
        t1.student_id = t2.student_id and t2.group_code != `group_code`;
	end if;
    if `semester_from` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester  < `semester_from`;
	end if;
    if `semester_to` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester > `semester_to`;
	end if;
    select distinct t1.teacher_id, t2.`name`, t3.subject_name, t3.subject_control, t4.group_code 
    from temp_table t1 join `teachers` t2 on t1.teacher_id = t2.teacher_id 
    join `subjects` t3 on t1.subject_id = t3.subject_id 
    join `students` t4 on t1.student_id = t4.student_id;
    drop table temp_table;
end $$