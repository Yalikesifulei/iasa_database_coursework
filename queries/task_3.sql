# 3.	Отримати перелік і загальне число тем кандидатських 
#		і докторських дисертацій, які захистили співробітники 
#		зазначеної кафедри для зазначеного факультету.

drop procedure if exists task_3;
delimiter $$
create procedure task_3(
	faculty_id int,
    chair_id int
)
begin
	drop table if exists temp_table;
    create table temp_table select * from teachers;
    if `faculty_id` != -1 then 
		delete t1 from temp_table t1 join `chairs` t2 on
        t1.chair_id = t2.chair_id and t2.faculty_id != `faculty_id`; 
        end if;
	if `chair_id` != -1 then 
		delete from temp_table where temp_table.chair_id != `chair_id`; 
        end if;
	select `phd_topic`, `prof_topic` from temp_table where
		temp_table.`phd_topic` is not NULL or temp_table.`prof_topic` is not NULL;
    drop table temp_table;
end $$