Create table employees(
emp_id varchar(10) primary key,
emp_name VARCHAR(100),
department VARCHAR(50),
designation VARCHAR(50),
joining_date DATE,
salary NUMERIC(10,2)
);
CREATE TABLE attendance (
attendance_id SERIAL PRIMARY KEY,
emp_id VARCHAR(10),
attendance_date DATE,
status VARCHAR(20),
shift VARCHAR(20)
);
CREATE TABLE overtime (
ot_id SERIAL PRIMARY KEY,
emp_id VARCHAR(10),
ot_date DATE,
ot_hours NUMERIC(5,2)
);
CREATE TABLE production (
production_id SERIAL PRIMARY KEY,
production_date DATE,
department VARCHAR(50),
machine_id VARCHAR(20),
units_produced INTEGER
);
CREATE TABLE quality (
quality_id SERIAL PRIMARY KEY,
quality_date DATE,
department VARCHAR(50),
rejected_units INTEGER
);
