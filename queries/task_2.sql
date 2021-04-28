# 2.	Отримати список і загальне число викладачів зазначених кафедр 
#       або зазначеного факультету повністю або зазначених категорій 
#       (асистенти, доценти, професори і т.д.) за статевою ознакою, 
#       року, віком, ознакою наявності та кількості дітей, розміру 
#       заробітної плати, є аспірантами, захистили кандидатські, 
#       докторські дисертації в зазначений період. 

drop procedure if exists task_2;
delimiter $$
create procedure task_2(
	chair_id int,
    faculty_id int,
    title varchar(45),
    sex varchar(2),
    age int,
    children int,
    salary int,
    phd_date_start date,
    phd_date_end date,
    prof_date_start date,
    prof_date_end date
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
	if `title` != -1 then 
		delete from temp_table where temp_table.title != `title`; 
        end if;
	if `sex` != -1 then 
		delete from temp_table where temp_table.sex != `sex`; 
        end if;
	if `age` != -1 then
		delete from temp_table where (select timestampdiff(year, temp_table.birthday, now()) != `age`); 
        end if;
	if `children` != -1 then
		delete from temp_table where temp_table.child_count != `has_children`; 
        end if;
	if `phd_date_start` != '0000-00-00' then
		delete from temp_table where 
			temp_table.phd_date < `phd_date_start` or temp_table.phd_date is NULL; 
        end if;
	if `phd_date_end` != '0000-00-00' then
		delete from temp_table where 
			temp_table.phd_date > `phd_date_end` or temp_table.phd_date is NULL; 
        end if;
	if `prof_date_start` != '0000-00-00' then
		delete from temp_table where 
			temp_table.prof_date < `prof_date_start` or temp_table.prof_date is NULL; 
        end if;
	if `prof_date_end` != '0000-00-00' then
		delete from temp_table where 
			temp_table.prof_date > `prof_date_end` or temp_table.prof_date is NULL; 
        end if;
	if `salary` != -1 then
		delete from temp_table where temp_table.salary < `salary`; 
        end if;
	select * from temp_table;
    drop table temp_table;
end $$