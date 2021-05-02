# 5.	Отримати список і загальне число викладачів, 
#		які проводили (проводять) заняття по вказаній 
#		дисципліні в зазначеній групі або на зазначеному 
#		курсі вказаного факультету. 

drop procedure if exists task_5;
delimiter $$
create procedure task_5(
	subj_name varchar(128),
	faculty_id int,
	group_code varchar(10),
    study_year_from int,
    study_year_to int,
    semester_from int,
    semester_to int
)
begin
	drop table if exists temp_table;
    create table temp_table select * from teachers;
end $$