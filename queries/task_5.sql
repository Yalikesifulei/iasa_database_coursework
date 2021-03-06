# 5.	Отримати список і загальне число викладачів, 
#		які проводили (проводять) заняття по вказаній 
#		дисципліні в зазначеній групі або на зазначеному 
#		курсі вказаного факультету. 

drop procedure if exists task_5;
delimiter $$
create procedure task_5(
	subject_id int,
	faculty_id int,
	semester_from int,
    semester_to int,
	group_code varchar(10)
)
begin
	drop table if exists temp_table;
    create table temp_table select * from `schedule`;
	if `subject_id` != -1 then
		delete from temp_table where temp_table.subject_id != `subject_id`;
	end if;
    if `group_code` != -1 then
		delete from temp_table where temp_table.group_code != `group_code`;
	end if;
	if `semester_from` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester  < `semester_from`;
	end if;
    if `semester_to` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester > `semester_to`;
	end if;
    if `faculty_id` != -1 then
		delete t1 from temp_table t1 join `groups` t2 
        on t1.group_code = t2.group_code join `chairs` t3 on
        t2.chair_id = t3.chair_id and t3.faculty_id != `faculty_id`;
	end if;
    create table temp_table2 select distinct `teacher_id` from temp_table;
    select * from `teachers` t1 join temp_table2 t2 on
		t1.teacher_id = t2.teacher_id;
    drop table temp_table;
    drop table temp_table2;
end $$