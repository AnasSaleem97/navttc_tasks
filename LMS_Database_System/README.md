# Learning Management System (LMS)

A database project built using MySQL, Python, and Streamlit to manage students, instructors, courses, enrollments, and academic grades.

---

## Files in this Project

* `lms_database.sql`: SQL script containing the database schema, table relationships, foreign keys, sample data, and business queries.
* `db.py`: Python module that connects to MySQL and handles all database queries and CRUD operations.
* `app.py`: Streamlit web interface with forms, searchable tables, dashboard charts, and reports.
* `requirements.txt`: Python packages needed to run the app.
* `SQL Mini Project-LMS-Students.pdf`: Original assignment problem statement and requirements.

---

## Features

1. **Dashboard**: Shows live counts for students, instructors, courses, enrollments, and visual bar charts.
2. **Students**: View, search, register, update, and delete student records.
3. **Instructors**: Manage instructor details and their specializations.
4. **Courses**: Create courses, assign instructors, set durations, and track fees.
5. **Enrollments**: Enroll students in courses (with duplicate enrollment check) and update enrollment status (`Enrolled`, `Completed`, `Dropped`).
6. **Grades**: Enter assignment, quiz, and final exam marks with automatic total marks calculation.
7. **Reports**: Implements all 6 required business questions (BR-01 to BR-06) using SQL JOINs and aggregations.

---

## Setup & Running the Project

### 1. Database Setup
Make sure MySQL is running, then import the database:
```bash
mysql -u root -p < lms_database.sql
```
*(Database configuration can be checked or edited in `db.py`)*.

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Application
```bash
streamlit run app.py
```
