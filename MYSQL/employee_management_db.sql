-- Create Database
CREATE DATABASE employee_management;
USE employee_management;

-- =========================
-- 1️⃣ Demographics Table
-- =========================
CREATE TABLE demographics (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INT,
    gender VARCHAR(10),
    birth_date DATE
);

-- =========================
-- 2️⃣ Departments Table
-- =========================
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

-- =========================
-- 3️⃣ Salary Table
-- =========================
CREATE TABLE salary (
    employee_id INT PRIMARY KEY,
    occupation VARCHAR(100),
    salary INT,
    dept_id INT,
    FOREIGN KEY (employee_id) REFERENCES demographics(employee_id),
    FOREIGN KEY (dept_id) REFERENCES departments(department_id)
);

-- =========================
-- Insert Departments
-- =========================
INSERT INTO departments (department_name) VALUES
('Information Technology'),
('Finance'),
('Human Resources'),
('Marketing'),
('Operations');

-- =========================
-- Insert Demographics
-- =========================
INSERT INTO demographics VALUES
(1,'Arjun','Mehta',28,'Male','1997-04-12'),
(2,'Sneha','Sharma',32,'Female','1993-09-25'),
(3,'Rohan','Verma',26,'Male','1999-02-18'),
(4,'Priya','Nair',35,'Female','1990-07-09'),
(5,'Karan','Malhotra',40,'Male','1985-11-21'),
(6,'Ananya','Reddy',29,'Female','1996-05-14'),
(7,'Vikram','Singh',38,'Male','1987-03-30'),
(8,'Neha','Kapoor',31,'Female','1994-12-05'),
(9,'Aditya','Joshi',27,'Male','1998-08-17'),
(10,'Ishita','Gupta',33,'Female','1992-06-22');

-- =========================
-- Insert Salary
-- =========================
INSERT INTO salary VALUES
(1,'Software Engineer',85000,1),
(2,'Financial Analyst',72000,2),
(3,'Frontend Developer',78000,1),
(4,'HR Manager',65000,3),
(5,'Operations Head',95000,5),
(6,'Marketing Executive',60000,4),
(7,'Senior Accountant',88000,2),
(8,'Talent Acquisition Specialist',62000,3),
(9,'Backend Developer',83000,1),
(10,'Digital Marketing Manager',75000,4);