# 7.	Отримати список і загальне число студентів 
#		зазначених груп, які здали залік або іспит
#		з вказаною дисципліни зі встановленою оцінкою. 

drop procedure if exists task_7;
delimiter $$
create procedure task_7(
	group_code varchar(10),
    subject_id int,
    mark varchar(2)
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
	if `mark` != -1 then
		case
			when `mark` = 'E' then delete from temp_table t where t.mark not between 60 and 64;
            when `mark` = 'D' then delete from temp_table t where t.mark not between 65 and 74;
            when `mark` = 'C' then delete from temp_table t where t.mark not between 75 and 84;
            when `mark` = 'B' then delete from temp_table t where t.mark not between 85 and 94;
            when `mark` = 'A' then delete from temp_table t where t.mark not between 95 and 100;
		end case;
	end if;
	select t1.student_id, t2.`name`, t3.`subject_name`, t1.mark from temp_table t1 
		join `students` t2 on t1.student_id = t2.student_id 
        join `subjects` t3 on t1.subject_id = t3.subject_id;
    drop table temp_table;
end $$

call task_7(-1, -1, 'A');