# 13.	Отримати навантаження викладачів (назва дисципліни, кількість годин), 
#		її обсяг на окремі види занять і загальне навантаження в зазначеному 
#		семестрі для конкретного викладача або для викладачів зазначеної кафедри. 

drop procedure if exists task_13;
delimiter $$
create procedure task_13(
    teacher_id int,
	chair_id int
)
begin
	drop table if exists temp_table;
    create table temp_table select * from `schedule`; 
    if `chair_id` != -1 then
		delete t1 from temp_table t1 join `teachers` t2 on
		t1.teacher_id = t2.teacher_id and t2.chair_id != `chair_id`;
	end if;
    if `teacher_id` != -1 then
		delete from temp_table where temp_table.teacher_id != `teacher_id`;
	end if;
    drop table if exists temp_table2;
    create table temp_table2 select 
		t1.*, 
        ifnull(t2.subject_lec_hours, 0) as subject_lec_hours, 
        ifnull(t2.subject_prac_hours, 0) as subject_prac_hours, 
        ifnull(t2.subject_lab_hours, 0) as subject_lab_hours
        from temp_table t1 join `subjects` t2 on t1.subject_id = t2.subject_id;
	select t1.teacher_id, t2.`name`, 
		sum(t1.subject_lec_hours) as lec_hours, 
        sum(t1.subject_prac_hours) as prac_hours,
        sum(t1.subject_lab_hours) as lab_hours,
        sum(t1.subject_lec_hours) + sum(t1.subject_prac_hours) + sum(t1.subject_lab_hours) as total_hours
        from temp_table2 t1 join `teachers` t2 on t1.teacher_id = t2.teacher_id 
	group by t1.teacher_id;
    drop table temp_table;
    drop table temp_table2;
end $$