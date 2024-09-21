CREATE SCHEMA `student_management_system` ;
use student_management_system;
Create table students (ID INT Primary KEY AUTO_INCREMENT, Roll_No VARCHAR(20) NOT Null, Name Varchar(100) Not Null, Email varchar(100) Not Null, dob Date Not Null, Gender ENUM('Male' , 'Female') Not null);
    
    Insert Into students(Roll_No , Name , Email , dob , gender)
    Values
    ('Bsdsf21A001','Abdul Rehman','bsdsf21a001@pucit.edu.pk','2003-12-11', 'Male'),
    ('Bsdsf21A002','Sheraz','bsdsf21a002@pucit.edu.pk',  '2002-11-12', 'Male'),
    ('Bsdsf21A003','Abdullah','bsdsf21a003@pucit.edu.pk', '2001-11-12', 'Male'),
    ('Bsdsf21A004','Abdul Moeed','bsdsf21a004@pucit.edu.pk',  '2003-12-11', 'Male'),
    ('Bsdsf21A005','Zain','bsdsf21a005@pucit.edu.pk',  '2002-12-11', 'Male'),
    ('Bsdsf21A006','Shehzad','bsdsf21a006@pucit.edu.pk', '2001-11-12', 'Male'),
    ('Bsdsf21A007','Soban','bsdsf21a007@pucit.edu.pk', '2003-09-09', 'Male'),
    ('Bsdsf21A008','Shiza','bsdsf21a008@pucit.edu.pk',  '2002-09-07', 'Female'),
    ('Bsdsf21A009','LOL','bsdsf21a009@pucit.edu.pk',  '2001-07-04', 'Female'),
    ('Bsdsf21A010','Eman Zahid','bsdsf21a010@pucit.edu.pk', '2001-04-08', 'Female'),
    ('Bsdsf21A011','Ali Hassan','bsdsf21a011@pucit.edu.pk', '2002-03-08', 'Male'),
    ('Bsdsf21A012','Huzaifa','bsdsf21a012@pucit.edu.pk', '2003-07-04', 'Male'),
    ('Bsdsf21A013','Ho Ga Koi','bsdsf21a013@pucit.edu.pk', '2001-07-07', 'Female'),
    ('Bsdsf21A014','Hamza Majeed','bsdsf21a014@pucit.edu.pk',  '2001-07-02', 'Male'),
    ('Bsdsf21A015','Samreen','bsdsf21a015@pucit.edu.pk','2001-12-11', 'Female'),
    ('Bsdsf21A016','Mushtaq','bsdsf21a015@pucit.edu.pk',  '2001-11-12', 'Male'),
    ('Bsdsf21A017','Talal','bsdsf21a017@pucit.edu.pk', '2005-03-01', 'Male'),
    ('Bsdsf21A018','Faizan','bsdsf21a018@pucit.edu.pk',  '2003-12-16', 'Male'),
    ('Bsdsf21A019','Hamza','bsdsf21a019@pucit.edu.pk',  '2002-11-12', 'Male'),
    ('Bsdsf21A020','Haseeb','bsdsf21a020@pucit.edu.pk', '2001-11-12', 'Male'),
    ('Bsdsf21A021','Shabbir','bsdsf21a021@pucit.edu.pk', '2003-09-09', 'Male'),
    ('Bsdsf21A022','Bootta','bsdsf21a022@pucit.edu.pk',  '2001-01-05', 'Male'),
    ('Bsdsf21A023','Faiq','bsdsf21a023@pucit.edu.pk',  '2001-12-12', 'Male'),
    ('Bsdsf21A024','Eman Munir','bsdsf21a024@pucit.edu.pk', '2001-11-11', 'Female'),
    ('Bsdsf21A025','Tota','bsdsf21a025@pucit.edu.pk', '2003-11-11', 'Female'),
    ('Bsdsf21A026','Shah G','bsdsf21a026@pucit.edu.pk', '2002-11-12', 'Male'),
    ('Bsdsf21A027','Ahsan','bsdsf21a027@pucit.edu.pk', '2001-04-06', 'Male'),
    ('Bsdsf21A028','Ahmed','bsdsf21a028@pucit.edu.pk',  '2003-04-06', 'Male'),
    ('Bsdsf21A029','Abdullah','bsdsf21a029@pucit.edu.pk','2002-04-06', 'Male'),
    ('Bsdsf21A030','Kashuf','bsdsf21a030@pucit.edu.pk',  '2001-08-06', 'Female'),
    ('Bsdsf21A031','Hassaan','bsdsf21a031@pucit.edu.pk', '2003-04-06', 'Male'),
    ('Bsdsf21A032','Haji','bsdsf21a032@pucit.edu.pk',  '2002-11-16', 'Male'),
    ('Bsdsf21A033','Rehan Gujjar','bsdsf21a033@pucit.edu.pk',  '2001-02-07', 'Male'),
    ('Bsdsf21A034','Azeem k Agay wala','bsdsf21a034@pucit.edu.pk', '2001-02-07', 'Male'),
    ('Bsdsf21A035','Azeem','bsdsf21a035@pucit.edu.pk', '2001-02-07', 'Male'),
    ('Bsdsf21A036','Azeem k Peechay Wala','bsdsf21a036@pucit.edu.pk',  '2001-02-07', 'Male'),
    ('Bsdsf21A037','Kainat','bsdsf21a037@pucit.edu.pk',  '2002-11-12', 'Female'),
    ('Bsdsf21A038','Aymen','bsdsf21a038@pucit.edu.pk', '2002-11-12', 'Female'),
    ('Bsdsf21A039','Khalid','bsdsf21a039@pucit.edu.pk', '2002-11-12', 'Female'),
    ('Bsdsf21A040','Barira','bsdsf21a040@pucit.edu.pk', '2002-11-12', 'Female'),
    ('Bsdsf21A041','Shoaib','bsdsf21a041@pucit.edu.pk', '2002-11-12', 'Male'),
    ('Bsdsf21A042','Sami','bsdsf21a0@pucit.edu.pk',  '2002-11-12', 'Male'),
	('Bsdsf21A043','Nauman Ishaq','bsdsf21a043@pucit.edu.pk','2002-11-12', 'Male'),
    ('Bsdsf21A044','Abdul Rehman','bsdsf21a044@pucit.edu.pk',  '22002-11-12', 'Male'),
    ('Bsdsf21A045','Jadoo','bsdsf21a045@pucit.edu.pk', '2002-11-12', 'Male'),
    ('Bsdsf21A046','Mudassir','bsdsf21a046@pucit.edu.pk',  '2002-11-12', 'Male'),
    ('Bsdsf21A047','Iqra','bsdsf21a047@pucit.edu.pk', '2002-11-12', 'Female'),
    ('Bsdsf21A048','Ahmed','bsdsf21a048@pucit.edu.pk', '2002-11-12', 'Male'),
    ('Bsdsf21A049','Amima','bsdsf21a049@pucit.edu.pk', '2002-11-12', 'Female'),
    ('Bsdsf21A050','Haris','bsdsf21a050@pucit.edu.pk', '2002-11-12', 'Male');
    
    
-- Task-2 -----------------------------
    
-- showing all the students 
select *, round(datediff(now(), dob)/365) as Age from students;
-- counting male and female student 
select count(*) as Total_Students,
		Count(case when gender = 'Male' Then 1 end) as Male_Students,
		count(case when gender = 'Female' Then 1 end) as female_Students
 from students;   
 
 -- Task-3 -----------------------------
 -- deleting the detail of a particular student 
 delete from students 
 where id IN (9,13,50);
 
 -- Task-3 -----------------------------
 
 update students 
 set dob = '1998-04-16'
 where Roll_No = 'Bsdsf21A001';
 
 -- Task-4-----------------------------
 
 Alter table students add constraint Email_verify 
 check (email Like '%pucit.edu.pk');
 
-- Task-5 -----------------------------
 
 Insert into students(Roll_No , Name , Email , dob , gender)
    Values ('Bsdsf21A051','Ahmed Jawad','bsdsf21a051@gmail.com','2000-03-20', 'Male')
    
    
    