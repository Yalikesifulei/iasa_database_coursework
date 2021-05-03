# 8.	Отримати список і загальне число студентів 
#		зазначених груп або вказаного курсу зазначеного 
#		факультету, які здали зазначену сесію на відмінно, 
#		без трійок, без двійок. 

drop procedure if exists task_8;
delimiter $$
create procedure task_8(
	faculty_id int,
	group_code varchar(10),
    semester_from int,
    semester_to int,
    mark varchar(2)
)
begin
	drop table if exists temp_table;
    create table temp_table select * from `session`;
	if `group_code` != -1 then 
		delete t1 from temp_table t1 join `students` t2 on
        t1.student_id = t2.student_id and t2.group_code != `group_code`;
	end if;
    if `faculty_id` != -1 then
		delete t1 from temp_table t1 join `students` t2 
        on t1.student_id = t2.student_id join `groups` t3
        on t2.group_code = t3.group_code join `chairs` t4 on
        t3.chair_id = t4.chair_id and t4.faculty_id != `faculty_id`;
	end if;
    if `semester_from` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester  < `semester_from`;
	end if;
    if `semester_to` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester > `semester_to`;
	end if;
    drop table if exists temp_table2;
    create table temp_table2 select student_id, min(temp_table.mark) as min_mark from temp_table group by student_id;
	if `mark` != -1 then
		case
			when `mark` = 'E' then delete from temp_table2 t where t.min_mark < 60;
            when `mark` = 'D' then delete from temp_table2 t where t.min_mark < 65;
            when `mark` = 'C' then delete from temp_table2 t where t.min_mark < 75;
            when `mark` = 'B' then delete from temp_table2 t where t.min_mark < 85;
            when `mark` = 'A' then delete from temp_table2 t where t.min_mark < 95;
		end case;
	end if;
	select t1.student_id, t2.`name`, t2.`group_code`, t1.min_mark from temp_table2 t1 join
    `students` t2 on t1.student_id = t2.student_id;
    drop table temp_table;
    drop table temp_table2;
end $$