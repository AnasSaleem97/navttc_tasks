import mysql.connector
from mysql.connector import Error

# Database connection settings
DB_CONFIG = {
    "host":     "localhost",
    "user":     "root",
    "password": "12345",
    "database": "lms_db"
}


def get_connection():
    """Create and return database connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def run_query(sql: str, params=None):
    """Run a SELECT query and return rows as list of dictionaries."""
    conn = get_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, params or ())
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Query error: {e}")
        return []
    finally:
        cursor.close()
        conn.close()


def execute_dml(sql: str, params=None):
    """Run INSERT, UPDATE, or DELETE query with commit."""
    conn = get_connection()
    if not conn:
        return False, "Could not connect to database."
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params or ())
        conn.commit()
        return True, "Success"
    except Error as e:
        return False, f"Database error: {e}"
    finally:
        cursor.close()
        conn.close()


# --- Students Queries ---

def get_all_students(search=""):
    """Get all students or search by name/email."""
    if search:
        sql = "SELECT * FROM students WHERE name LIKE %s OR email LIKE %s ORDER BY student_id ASC;"
        term = f"%{search}%"
        return run_query(sql, (term, term))
    return run_query("SELECT * FROM students ORDER BY student_id ASC;")


def add_student(name, email, phone, enrollment_date, status="Active"):
    sql = """
        INSERT INTO students (name, email, phone, enrollment_date, status)
        VALUES (%s, %s, %s, %s, %s);
    """
    return execute_dml(sql, (name.strip(), email.strip(), phone.strip(), enrollment_date, status))


def update_student(student_id, name, email, phone, enrollment_date, status):
    sql = """
        UPDATE students
        SET name = %s, email = %s, phone = %s, enrollment_date = %s, status = %s
        WHERE student_id = %s;
    """
    return execute_dml(sql, (name.strip(), email.strip(), phone.strip(), enrollment_date, status, student_id))


def delete_student(student_id):
    return execute_dml("DELETE FROM students WHERE student_id = %s;", (student_id,))


# --- Instructors Queries ---

def get_all_instructors():
    return run_query("SELECT * FROM instructors ORDER BY instructor_id ASC;")


def add_instructor(name, email, specialization, status="Active"):
    sql = """
        INSERT INTO instructors (name, email, specialization, status)
        VALUES (%s, %s, %s, %s);
    """
    return execute_dml(sql, (name.strip(), email.strip(), specialization.strip(), status))


def update_instructor(instructor_id, name, email, specialization, status):
    sql = """
        UPDATE instructors
        SET name = %s, email = %s, specialization = %s, status = %s
        WHERE instructor_id = %s;
    """
    return execute_dml(sql, (name.strip(), email.strip(), specialization.strip(), status, instructor_id))


def delete_instructor(instructor_id):
    return execute_dml("DELETE FROM instructors WHERE instructor_id = %s;", (instructor_id,))


# --- Courses Queries ---

def get_all_courses():
    sql = """
        SELECT c.course_id, c.course_name, c.description, c.instructor_id,
               COALESCE(i.name, 'Unassigned') AS instructor_name,
               c.duration, c.fee, c.status
        FROM courses c
        LEFT JOIN instructors i ON c.instructor_id = i.instructor_id
        ORDER BY c.course_id ASC;
    """
    return run_query(sql)


def add_course(course_name, description, instructor_id, duration, fee, status="Active"):
    sql = """
        INSERT INTO courses (course_name, description, instructor_id, duration, fee, status)
        VALUES (%s, %s, %s, %s, %s, %s);
    """
    return execute_dml(sql, (course_name.strip(), description.strip(), instructor_id, duration.strip(), fee, status))


def update_course(course_id, course_name, description, instructor_id, duration, fee, status):
    sql = """
        UPDATE courses
        SET course_name = %s, description = %s, instructor_id = %s, duration = %s, fee = %s, status = %s
        WHERE course_id = %s;
    """
    return execute_dml(sql, (course_name.strip(), description.strip(), instructor_id, duration.strip(), fee, status, course_id))


def delete_course(course_id):
    return execute_dml("DELETE FROM courses WHERE course_id = %s;", (course_id,))


# --- Enrollments Queries ---

def get_all_enrollments():
    sql = """
        SELECT e.enrollment_id, e.student_id, s.name AS student_name,
               e.course_id, c.course_name, e.enrollment_date, e.status
        FROM enrollments e
        INNER JOIN students s ON e.student_id = s.student_id
        INNER JOIN courses c ON e.course_id = c.course_id
        ORDER BY e.enrollment_id ASC;
    """
    return run_query(sql)


def add_enrollment(student_id, course_id, enrollment_date, status="Enrolled"):
    sql = """
        INSERT INTO enrollments (student_id, course_id, enrollment_date, status)
        VALUES (%s, %s, %s, %s);
    """
    return execute_dml(sql, (student_id, course_id, enrollment_date, status))


def update_enrollment_status(enrollment_id, status):
    sql = "UPDATE enrollments SET status = %s WHERE enrollment_id = %s;"
    return execute_dml(sql, (status, enrollment_id))


def delete_enrollment(enrollment_id):
    return execute_dml("DELETE FROM enrollments WHERE enrollment_id = %s;", (enrollment_id,))


# --- Grades Queries ---

def get_all_grades():
    sql = """
        SELECT g.grade_id, g.enrollment_id, s.name AS student_name, c.course_name,
               g.assignment_marks, g.quiz_marks, g.final_exam_marks, g.total_marks
        FROM grades g
        INNER JOIN enrollments e ON g.enrollment_id = e.enrollment_id
        INNER JOIN students s ON e.student_id = s.student_id
        INNER JOIN courses c ON e.course_id = c.course_id
        ORDER BY g.grade_id ASC;
    """
    return run_query(sql)


def save_grade(enrollment_id, assignment_marks, quiz_marks, final_exam_marks):
    total_marks = assignment_marks + quiz_marks + final_exam_marks
    sql = """
        INSERT INTO grades (enrollment_id, assignment_marks, quiz_marks, final_exam_marks, total_marks)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            assignment_marks = VALUES(assignment_marks),
            quiz_marks = VALUES(quiz_marks),
            final_exam_marks = VALUES(final_exam_marks),
            total_marks = VALUES(total_marks);
    """
    return execute_dml(sql, (enrollment_id, assignment_marks, quiz_marks, final_exam_marks, total_marks))


def delete_grade(grade_id):
    return execute_dml("DELETE FROM grades WHERE grade_id = %s;", (grade_id,))


# --- Dashboard KPIs & Reports (BR-01 to BR-06) ---

def get_dashboard_kpis():
    res_students = run_query("SELECT COUNT(*) AS count FROM students;")
    res_active_students = run_query("SELECT COUNT(*) AS count FROM students WHERE status = 'Active';")
    res_instructors = run_query("SELECT COUNT(*) AS count FROM instructors WHERE status = 'Active';")
    res_courses = run_query("SELECT COUNT(*) AS count FROM courses WHERE status = 'Active';")
    res_enrollments = run_query("SELECT COUNT(*) AS count FROM enrollments;")

    return {
        "total_students": res_students[0]["count"] if res_students else 0,
        "active_students": res_active_students[0]["count"] if res_active_students else 0,
        "active_instructors": res_instructors[0]["count"] if res_instructors else 0,
        "active_courses": res_courses[0]["count"] if res_courses else 0,
        "total_enrollments": res_enrollments[0]["count"] if res_enrollments else 0,
    }


def get_enrollments_per_course():
    """BR-01: Courses with highest number of enrolled students."""
    sql = """
        SELECT c.course_name, COUNT(e.enrollment_id) AS total_enrollments
        FROM courses c
        LEFT JOIN enrollments e ON c.course_id = e.course_id
        GROUP BY c.course_id, c.course_name
        ORDER BY total_enrollments DESC;
    """
    return run_query(sql)


def get_courses_per_instructor():
    """BR-02: Number of courses each instructor teaches."""
    sql = """
        SELECT i.name AS instructor_name, i.specialization,
               COUNT(c.course_id) AS total_courses
        FROM instructors i
        LEFT JOIN courses c ON i.instructor_id = c.instructor_id
        GROUP BY i.instructor_id, i.name, i.specialization
        ORDER BY total_courses DESC;
    """
    return run_query(sql)


def get_student_grades_report():
    """Detailed student gradebook."""
    sql = """
        SELECT s.name AS student_name, c.course_name,
               g.assignment_marks, g.quiz_marks, g.final_exam_marks, g.total_marks
        FROM students s
        INNER JOIN enrollments e ON s.student_id = e.student_id
        INNER JOIN grades g ON e.enrollment_id = g.enrollment_id
        INNER JOIN courses c ON e.course_id = c.course_id
        ORDER BY g.total_marks DESC;
    """
    return run_query(sql)


def get_top_students():
    """BR-03: Students ranked by highest total marks."""
    sql = """
        SELECT s.name AS student_name, SUM(g.total_marks) AS cumulative_marks,
               COUNT(g.grade_id) AS courses_graded
        FROM students s
        INNER JOIN enrollments e ON s.student_id = e.student_id
        INNER JOIN grades g ON e.enrollment_id = g.enrollment_id
        GROUP BY s.student_id, s.name
        ORDER BY cumulative_marks DESC;
    """
    return run_query(sql)


def get_enrollment_status_summary():
    """BR-05: Count of enrollments by status."""
    sql = """
        SELECT status, COUNT(enrollment_id) AS count
        FROM enrollments
        GROUP BY status;
    """
    return run_query(sql)


def get_courses_with_no_students():
    """BR-06: Courses with no enrolled students."""
    sql = """
        SELECT c.course_id, c.course_name, c.fee, c.status
        FROM courses c
        LEFT JOIN enrollments e ON c.course_id = e.course_id
        WHERE e.enrollment_id IS NULL;
    """
    return run_query(sql)
