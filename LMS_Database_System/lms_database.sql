create database if not exists lms_db;
use lms_db;

create table instructors(
instructor_id int auto_increment primary key,
name varchar(100) not null,
email varchar(100) not null unique,
specialization varchar(100),
status enum('active','inactive') default 'active'
);
create table courses(
course_id int auto_increment primary key,
course_name varchar(100) not null,
description TEXT,
instructor_id int,
duration varchar(100),
fee decimal(10,2) default 0.00,
status enum('active','inactive') default 'active',
foreign key (instructor_id) references instructors(instructor_id) on delete set null
);
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    enrollment_date DATE NOT NULL,
    status ENUM('Active', 'Inactive') DEFAULT 'Active'
);
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    status ENUM('Enrolled', 'Completed', 'Dropped') DEFAULT 'Enrolled',
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE,
    UNIQUE (student_id, course_id)
);
CREATE TABLE grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    enrollment_id INT NOT NULL UNIQUE,
    assignment_marks DECIMAL(5, 2) DEFAULT 0.00,
    quiz_marks DECIMAL(5, 2) DEFAULT 0.00,
    final_exam_marks DECIMAL(5, 2) DEFAULT 0.00,
    total_marks DECIMAL(5, 2) DEFAULT 0.00,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE
);

-- 1. Insert Instructors
INSERT INTO instructors (name, email, specialization, status) VALUES

('Dr. Ahmed Khan', 'ahmed.khan@lms.edu', 'Data Science & AI', 'Active'),
('Prof. Sara Ali', 'sara.ali@lms.edu', 'Web Development', 'Active'),
('Dr. Usman Tariq', 'usman.tariq@lms.edu', 'Database Systems', 'Active'),
('Engr. Fatima Noor', 'fatima.noor@lms.edu', 'Cyber Security', 'Active'),
('Bilal Qureshi', 'bilal.qureshi@lms.edu', 'Mobile App Development', 'Inactive');

-- 2. Insert Courses
INSERT INTO courses (course_name, description, instructor_id, duration, fee, status) VALUES
('Python for Data Science', 'Complete Python from basics to data analysis and visualization', 1, '8 Weeks', 15000.00, 'Active'),
('Machine Learning Fundamentals', 'Supervised and unsupervised learning with scikit-learn', 1, '10 Weeks', 20000.00, 'Active'),
('Full Stack Web Development', 'HTML, CSS, JavaScript, React and Node.js', 2, '12 Weeks', 25000.00, 'Active'),
('Relational Databases with MySQL', 'Schema design, complex queries, indexing and optimization', 3, '6 Weeks', 12000.00, 'Active'),
('Network Defense & Ethical Hacking', 'Hands-on penetration testing and security fundamentals', 4, '8 Weeks', 18000.00, 'Active'),
('Cloud Computing with AWS', 'Cloud architecture, EC2, S3, RDS and deployment', 3, '6 Weeks', 16000.00, 'Active');

-- 3. Insert Students
INSERT INTO students (name, email, phone, enrollment_date, status) VALUES
('Ali Raza', 'ali.raza@gmail.com', '03001234567', '2024-01-15', 'Active'),
('Ayesha Malik', 'ayesha.malik@gmail.com', '03129876543', '2024-02-01', 'Active'),
('Hamza Javed', 'hamza.javed@gmail.com', '03214567890', '2024-02-10', 'Active'),
('Zainab Bibi', 'zainab.bibi@gmail.com', '03331122334', '2024-03-05', 'Active'),
('Omer Farooq', 'omer.farooq@gmail.com', '03455566778', '2024-01-20', 'Active'),
('Hina Tariq', 'hina.tariq@gmail.com', '03019988776', '2023-11-10', 'Inactive');

-- 4. Insert Enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date, status) VALUES
(1, 1, '2024-01-16', 'Completed'),
(1, 2, '2024-02-15', 'Enrolled'),
(2, 1, '2024-02-02', 'Enrolled'),
(2, 3, '2024-02-05', 'Enrolled'),
(3, 3, '2024-02-11', 'Completed'),
(3, 4, '2024-02-12', 'Dropped'),
(4, 4, '2024-03-06', 'Enrolled'),
(5, 1, '2024-01-22', 'Enrolled'),
(5, 5, '2024-01-25', 'Completed');

-- 5. Insert Grades
INSERT INTO grades (enrollment_id, assignment_marks, quiz_marks, final_exam_marks, total_marks) VALUES
(1, 28.50, 18.00, 47.00, 93.50),
(2, 25.00, 15.00, 42.00, 82.00),
(3, 22.00, 14.00, 38.00, 74.00),
(4, 27.00, 19.00, 49.00, 95.00),
(5, 29.00, 20.00, 48.00, 97.00),
(6, 10.00, 08.00, 00.00, 18.00),
(7, 24.00, 16.00, 40.00, 80.00),
(8, 26.50, 17.50, 43.00, 87.00),
(9, 30.00, 19.50, 46.50, 96.00);

select * from students;

select c.course_id,c.course_name,count(e.enrollment_id) as total_enrollments from enrollments as e 
inner join 
courses as c on e.course_id=c.course_id 
group by c.course_id, c.course_name 
order by total_enrollments DESC;

-- BR-02: How many courses is each instructor teaching?
SELECT 
    i.instructor_id,
    i.name AS instructor_name,
    COUNT(c.course_id) AS total_courses_teaching
FROM instructors i
LEFT JOIN courses c ON i.instructor_id = c.instructor_id
GROUP BY i.instructor_id, i.name
ORDER BY total_courses_teaching DESC;

select s.student_id,s.name, g.total_marks,e.course_id,c.course_name from students as s 
left join enrollments as e
on s.student_id=e.student_id 
inner join grades as g
on
e.enrollment_id=g.enrollment_id
inner join courses as c
on
e.course_id=c.course_id
order by s.student_id asc;

select count(student_id) from students
where status = 'Active';

select 
e.status,count(e.enrollment_id) as total_count from enrollments as e
group by status;

-- BR-06: Which courses have no students enrolled?
SELECT 
    c.course_id,
    c.course_name,
    c.fee,
    c.status
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL;



