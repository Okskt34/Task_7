--1

    CREATE DATABASE my_first_db
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

--2

CREATE TABLE public.student
(
    id integer,
    name text
);

ALTER TABLE IF EXISTS public.student
    OWNER to postgres;

--3

CREATE SEQUENCE employees_id_seq START 1;

CREATE TABLE employee (
  id integer PRIMARY KEY DEFAULT nextval('employees_id_seq'),
  name text,
  salary integer
);

--4

ALTER TABLE student ADD PRIMARY KEY (id);

--5

INSERT INTO public.employee(
	name, salary)
	VALUES ('John', 1000);

INSERT INTO public.student(
	id, name)
	VALUES (01, 'Jonh');
