# Question - 1
create database eurekadb;

# Question - 2
create table employee(
Employee_id int primary key,
Employee_name varchar(50),
Street varchar(100),
City varchar(50),
Join_date date,
Annual_salary int
);

select * from employee;

create table department(
Department_id int primary key,
Department_name varchar(50),
City varchar(50)
);

select * from department;

create table manages(
Manager_id int,
Employee_id int,
primary key(Manager_id, Employee_id),
foreign key (Employee_id) REFERENCES employee(Employee_id) ON DELETE CASCADE,
foreign key (Manager_id) REFERENCES employee(Employee_id) ON DELETE CASCADE
);

select * from manages;

create table works(
Department_id int ,
Employee_id int ,
Job_title varchar(50) ,
Notes varchar(500) ,
primary key(Department_id, Employee_id),
foreign key (Employee_id) REFERENCES employee(Employee_id) ON DELETE CASCADE,
foreign key (Department_id) REFERENCES department(Department_id) ON DELETE CASCADE
);

select * from works;

