# 4.	Отримати перелік кафедр, які проводять заняття 
#		у зазначеній групі або на зазначеному курсі 
#		вказаного факультету в зазначеному семестрі, 
#		або за вказаний період. 

drop procedure if exists task_4;
delimiter $$
create procedure task_4(
	faculty_id int,
	group_code varchar(10),
    semester_from int,
    semester_to int
)
begin
	drop table if exists temp_table;
    create table temp_table select * from `schedule`;
    if `group_code` != -1 then
		delete from temp_table where temp_table.group_code != `group_code`;
	end if;
    if `faculty_id` != -1 then 
		delete t1 from temp_table t1 join `groups` t2 on
        t1.group_code = t2.group_code join `chairs` t3 on 
        t2.chair_id = t3.chair_id join `faculties` t4 on
        t3.faculty_id != `faculty_id`;
        end if;
    if `semester_from` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester  < `semester_from`;
	end if;
    if `semester_to` != -1 then
		delete t1 from temp_table t1 join `subjects` t2 on
        t1.subject_id = t2.subject_id and t2.subject_year*2 - 2 + t2.subject_semester > `semester_to`;
	end if;
	select distinct t3.`chair_id`, t3.`faculty_id`, t3.`chair_name` from
		temp_table t1 join `teachers` t2 on t1.teacher_id = t2.teacher_id 
		join `chairs` t3 on t2.chair_id = t3.chair_id;
	drop table temp_table;
end $$