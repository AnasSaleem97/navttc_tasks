import streamlit as st
import pandas as pd
from datetime import date
import db

st.set_page_config(page_title="Learning Management System", layout="wide")

# Sidebar navigation
st.sidebar.title("LMS Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Students", "Instructors", "Courses", "Enrollments", "Grades", "Reports"]
)


# Page 1: Dashboard
if page == "Dashboard":
    st.title("LMS Academic Dashboard")
    st.write("Overview of students, instructors, courses, and active enrollments.")

    kpis = db.get_dashboard_kpis()
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Students", kpis["total_students"])
    c2.metric("Active Students", kpis["active_students"])
    c3.metric("Instructors", kpis["active_instructors"])
    c4.metric("Active Courses", kpis["active_courses"])
    c5.metric("Enrollments", kpis["total_enrollments"])

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Enrollments per Course")
        course_data = db.get_enrollments_per_course()
        if course_data:
            df_course = pd.DataFrame(course_data)
            st.bar_chart(df_course.set_index("course_name")["total_enrollments"])
        else:
            st.info("No course enrollment data found.")

    with col2:
        st.subheader("Enrollment Status Breakdown")
        status_data = db.get_enrollment_status_summary()
        if status_data:
            df_status = pd.DataFrame(status_data)
            st.bar_chart(df_status.set_index("status")["count"])
        else:
            st.info("No enrollment status data found.")

    st.markdown("---")
    st.subheader("Recent Enrollments")
    enrollments = db.get_all_enrollments()
    if enrollments:
        df_enr = pd.DataFrame(enrollments)
        st.dataframe(df_enr.tail(6)[["student_name", "course_name", "enrollment_date", "status"]], use_container_width=True, hide_index=True)


# Page 2: Students
elif page == "Students":
    st.title("Students Directory")

    tab_view, tab_add, tab_edit, tab_del = st.tabs(["View Students", "Add Student", "Edit Student", "Delete Student"])

    with tab_view:
        search = st.text_input("Search by student name or email:", "")
        students = db.get_all_students(search)
        if students:
            df_std = pd.DataFrame(students)
            st.dataframe(df_std, use_container_width=True, hide_index=True)
            st.caption(f"Total students: {len(students)}")
        else:
            st.info("No students found.")

    with tab_add:
        st.subheader("Add New Student")
        with st.form("add_student_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input("Student Name")
                email = st.text_input("Email")
            with c2:
                phone = st.text_input("Phone Number")
                enr_date = st.date_input("Enrollment Date", value=date.today())
                status = st.selectbox("Status", ["Active", "Inactive"])

            if st.form_submit_button("Submit"):
                if not name.strip() or not email.strip():
                    st.warning("Please provide name and email.")
                else:
                    ok, msg = db.add_student(name, email, phone, enr_date, status)
                    if ok:
                        st.success(f"Student '{name}' added successfully.")
                        st.rerun()
                    else:
                        st.error(msg)

    with tab_edit:
        st.subheader("Edit Student Details")
        all_students = db.get_all_students()
        if all_students:
            std_options = {f"{s['student_id']} - {s['name']}": s for s in all_students}
            selected_student = st.selectbox("Select student to update", list(std_options.keys()))
            std = std_options[selected_student]

            with st.form("edit_student_form"):
                c1, c2 = st.columns(2)
                with c1:
                    new_name = st.text_input("Name", value=std["name"])
                    new_email = st.text_input("Email", value=std["email"])
                with c2:
                    new_phone = st.text_input("Phone", value=std["phone"] or "")
                    new_date = st.date_input("Enrollment Date", value=std["enrollment_date"])
                    new_status = st.selectbox("Status", ["Active", "Inactive"], index=0 if std["status"] == "Active" else 1)

                if st.form_submit_button("Save Updates"):
                    ok, msg = db.update_student(std["student_id"], new_name, new_email, new_phone, new_date, new_status)
                    if ok:
                        st.success("Student updated successfully.")
                        st.rerun()
                    else:
                        st.error(msg)
        else:
            st.info("No student records available.")

    with tab_del:
        st.subheader("Delete Student")
        all_students = db.get_all_students()
        if all_students:
            std_options = {f"{s['student_id']} - {s['name']}": s for s in all_students}
            chosen = st.selectbox("Select student to remove", list(std_options.keys()), key="del_std")
            std_del = std_options[chosen]

            st.warning(f"This will delete student **{std_del['name']}** along with their enrollments and grades.")
            confirm = st.checkbox("Confirm deletion")
            if st.button("Delete", disabled=not confirm):
                ok, msg = db.delete_student(std_del["student_id"])
                if ok:
                    st.success("Student deleted.")
                    st.rerun()
                else:
                    st.error(msg)


# Page 3: Instructors
elif page == "Instructors":
    st.title("Instructors Directory")

    tab_view, tab_add, tab_edit, tab_del = st.tabs(["View Instructors", "Add Instructor", "Edit Instructor", "Delete Instructor"])

    with tab_view:
        instructors = db.get_all_instructors()
        if instructors:
            df_inst = pd.DataFrame(instructors)
            st.dataframe(df_inst, use_container_width=True, hide_index=True)
        else:
            st.info("No instructors registered.")

    with tab_add:
        st.subheader("Add New Instructor")
        with st.form("add_instructor_form", clear_on_submit=True):
            name = st.text_input("Instructor Name")
            email = st.text_input("Email")
            specialization = st.text_input("Specialization (e.g. Data Science, Web Development)")
            status = st.selectbox("Status", ["Active", "Inactive"])

            if st.form_submit_button("Submit"):
                if not name.strip() or not email.strip():
                    st.warning("Please provide name and email.")
                else:
                    ok, msg = db.add_instructor(name, email, specialization, status)
                    if ok:
                        st.success(f"Instructor '{name}' registered.")
                        st.rerun()
                    else:
                        st.error(msg)

    with tab_edit:
        st.subheader("Edit Instructor Details")
        instructors = db.get_all_instructors()
        if instructors:
            inst_options = {f"{i['instructor_id']} - {i['name']}": i for i in instructors}
            chosen_inst = st.selectbox("Select instructor", list(inst_options.keys()))
            inst = inst_options[chosen_inst]

            with st.form("edit_instructor_form"):
                new_name = st.text_input("Name", value=inst["name"])
                new_email = st.text_input("Email", value=inst["email"])
                new_spec = st.text_input("Specialization", value=inst["specialization"] or "")
                new_status = st.selectbox("Status", ["Active", "Inactive"], index=0 if inst["status"] == "Active" else 1)

                if st.form_submit_button("Save Updates"):
                    ok, msg = db.update_instructor(inst["instructor_id"], new_name, new_email, new_spec, new_status)
                    if ok:
                        st.success("Instructor updated.")
                        st.rerun()
                    else:
                        st.error(msg)

    with tab_del:
        st.subheader("Delete Instructor")
        instructors = db.get_all_instructors()
        if instructors:
            inst_options = {f"{i['instructor_id']} - {i['name']}": i for i in instructors}
            chosen = st.selectbox("Select instructor to remove", list(inst_options.keys()), key="del_inst")
            inst_del = inst_options[chosen]

            confirm = st.checkbox("Confirm deletion")
            if st.button("Delete", disabled=not confirm):
                ok, msg = db.delete_instructor(inst_del["instructor_id"])
                if ok:
                    st.success("Instructor removed.")
                    st.rerun()
                else:
                    st.error(msg)


# Page 4: Courses
elif page == "Courses":
    st.title("Course Management")

    tab_view, tab_add, tab_edit, tab_del = st.tabs(["View Courses", "Add Course", "Edit Course", "Delete Course"])

    with tab_view:
        courses = db.get_all_courses()
        if courses:
            df_crs = pd.DataFrame(courses)
            st.dataframe(df_crs[["course_id", "course_name", "instructor_name", "duration", "fee", "status", "description"]], use_container_width=True, hide_index=True)
        else:
            st.info("No courses found.")

    with tab_add:
        st.subheader("Create New Course")
        instructors = db.get_all_instructors()
        inst_options = {f"{i['name']} ({i['specialization']})": i['instructor_id'] for i in instructors}
        inst_options["None (Unassigned)"] = None

        with st.form("add_course_form", clear_on_submit=True):
            course_name = st.text_input("Course Title")
            description = st.text_area("Description")
            c1, c2 = st.columns(2)
            with c1:
                assigned_inst = st.selectbox("Instructor", list(inst_options.keys()))
                duration = st.text_input("Duration", "8 Weeks")
            with c2:
                fee = st.number_input("Fee (PKR)", min_value=0.0, step=1000.0, value=15000.0)
                status = st.selectbox("Status", ["Active", "Inactive"])

            if st.form_submit_button("Create Course"):
                if not course_name.strip():
                    st.warning("Course title is required.")
                else:
                    inst_id = inst_options[assigned_inst]
                    ok, msg = db.add_course(course_name, description, inst_id, duration, fee, status)
                    if ok:
                        st.success(f"Course '{course_name}' created.")
                        st.rerun()
                    else:
                        st.error(msg)

    with tab_edit:
        st.subheader("Edit Course")
        courses = db.get_all_courses()
        instructors = db.get_all_instructors()
        inst_options = {f"{i['name']} ({i['specialization']})": i['instructor_id'] for i in instructors}
        inst_options["None (Unassigned)"] = None

        if courses:
            crs_options = {f"{c['course_id']} - {c['course_name']}": c for c in courses}
            chosen = st.selectbox("Select course", list(crs_options.keys()))
            crs = crs_options[chosen]

            with st.form("edit_course_form"):
                new_title = st.text_input("Title", value=crs["course_name"])
                new_desc = st.text_area("Description", value=crs["description"] or "")
                c1, c2 = st.columns(2)
                with c1:
                    inst_keys = list(inst_options.keys())
                    inst_idx = 0
                    for idx, key in enumerate(inst_keys):
                        if inst_options[key] == crs["instructor_id"]:
                            inst_idx = idx
                            break
                    new_inst = st.selectbox("Instructor", inst_keys, index=inst_idx)
                    new_dur = st.text_input("Duration", value=crs["duration"] or "")
                with c2:
                    new_fee = st.number_input("Fee (PKR)", value=float(crs["fee"]), min_value=0.0, step=500.0)
                    new_status = st.selectbox("Status", ["Active", "Inactive"], index=0 if crs["status"] == "Active" else 1)

                if st.form_submit_button("Save"):
                    inst_id = inst_options[new_inst]
                    ok, msg = db.update_course(crs["course_id"], new_title, new_desc, inst_id, new_dur, new_fee, new_status)
                    if ok:
                        st.success("Course updated.")
                        st.rerun()
                    else:
                        st.error(msg)

    with tab_del:
        st.subheader("Delete Course")
        courses = db.get_all_courses()
        if courses:
            crs_options = {f"{c['course_id']} - {c['course_name']}": c for c in courses}
            chosen = st.selectbox("Select course to delete", list(crs_options.keys()), key="del_crs")
            crs_del = crs_options[chosen]

            confirm = st.checkbox("Confirm course deletion")
            if st.button("Delete Course", disabled=not confirm):
                ok, msg = db.delete_course(crs_del["course_id"])
                if ok:
                    st.success("Course deleted.")
                    st.rerun()
                else:
                    st.error(msg)


# Page 5: Enrollments
elif page == "Enrollments":
    st.title("Student Enrollments")

    tab_view, tab_add, tab_edit, tab_del = st.tabs(["View Enrollments", "Enroll Student", "Change Status", "Remove Enrollment"])

    with tab_view:
        enrollments = db.get_all_enrollments()
        if enrollments:
            df_enr = pd.DataFrame(enrollments)
            st.dataframe(df_enr[["enrollment_id", "student_name", "course_name", "enrollment_date", "status"]], use_container_width=True, hide_index=True)
        else:
            st.info("No enrollments found.")

    with tab_add:
        st.subheader("Enroll Student in Course")
        students = db.get_all_students()
        courses = db.get_all_courses()

        if not students or not courses:
            st.warning("Please make sure students and courses exist.")
        else:
            std_options = {f"{s['student_id']} - {s['name']}": s['student_id'] for s in students if s['status'] == 'Active'}
            crs_options = {f"{c['course_id']} - {c['course_name']}": c['course_id'] for c in courses if c['status'] == 'Active'}

            with st.form("enroll_student_form", clear_on_submit=True):
                c1, c2 = st.columns(2)
                with c1:
                    chosen_std = st.selectbox("Student", list(std_options.keys()))
                    enr_date = st.date_input("Enrollment Date", value=date.today())
                with c2:
                    chosen_crs = st.selectbox("Course", list(crs_options.keys()))
                    enr_status = st.selectbox("Status", ["Enrolled", "Completed", "Dropped"])

                if st.form_submit_button("Enroll"):
                    s_id = std_options[chosen_std]
                    c_id = crs_options[chosen_crs]
                    ok, msg = db.add_enrollment(s_id, c_id, enr_date, enr_status)
                    if ok:
                        st.success("Enrollment successful.")
                        st.rerun()
                    else:
                        if "Duplicate" in msg or "1062" in msg:
                            st.error("This student is already enrolled in this course.")
                        else:
                            st.error(msg)

    with tab_edit:
        st.subheader("Update Enrollment Status")
        enrollments = db.get_all_enrollments()
        if enrollments:
            enr_options = {f"#{e['enrollment_id']} - {e['student_name']} -> {e['course_name']} ({e['status']})": e for e in enrollments}
            chosen = st.selectbox("Select enrollment", list(enr_options.keys()))
            enr = enr_options[chosen]

            with st.form("update_enr_form"):
                statuses = ["Enrolled", "Completed", "Dropped"]
                curr_idx = statuses.index(enr["status"]) if enr["status"] in statuses else 0
                new_status = st.selectbox("New Status", statuses, index=curr_idx)

                if st.form_submit_button("Update"):
                    ok, msg = db.update_enrollment_status(enr["enrollment_id"], new_status)
                    if ok:
                        st.success("Enrollment status updated.")
                        st.rerun()
                    else:
                        st.error(msg)

    with tab_del:
        st.subheader("Cancel Enrollment")
        enrollments = db.get_all_enrollments()
        if enrollments:
            enr_options = {f"#{e['enrollment_id']} - {e['student_name']} -> {e['course_name']}": e for e in enrollments}
            chosen = st.selectbox("Select enrollment to delete", list(enr_options.keys()), key="del_enr")
            enr_del = enr_options[chosen]

            confirm = st.checkbox("Confirm removal")
            if st.button("Delete Enrollment", disabled=not confirm):
                ok, msg = db.delete_enrollment(enr_del["enrollment_id"])
                if ok:
                    st.success("Enrollment deleted.")
                    st.rerun()
                else:
                    st.error(msg)


# Page 6: Grades
elif page == "Grades":
    st.title("Student Marks & Gradebook")

    tab_view, tab_record, tab_del = st.tabs(["Gradebook", "Enter / Update Marks", "Delete Grade"])

    with tab_view:
        grades = db.get_all_grades()
        if grades:
            df_grd = pd.DataFrame(grades)
            st.dataframe(df_grd[["student_name", "course_name", "assignment_marks", "quiz_marks", "final_exam_marks", "total_marks"]], use_container_width=True, hide_index=True)
        else:
            st.info("No grades entered yet.")

    with tab_record:
        st.subheader("Enter Marks for Student")
        enrollments = db.get_all_enrollments()
        if enrollments:
            enr_options = {f"#{e['enrollment_id']} - {e['student_name']} ({e['course_name']})": e for e in enrollments}
            chosen = st.selectbox("Select enrollment", list(enr_options.keys()))
            enr = enr_options[chosen]

            with st.form("grades_form"):
                c1, c2, c3 = st.columns(3)
                with c1:
                    assignment = st.number_input("Assignment (Max 30)", min_value=0.0, max_value=30.0, value=25.0, step=0.5)
                with c2:
                    quiz = st.number_input("Quiz (Max 20)", min_value=0.0, max_value=20.0, value=15.0, step=0.5)
                with c3:
                    final_exam = st.number_input("Final Exam (Max 50)", min_value=0.0, max_value=50.0, value=40.0, step=0.5)

                total = assignment + quiz + final_exam
                st.write(f"Total Marks: **{total:.2f} / 100.00**")

                if st.form_submit_button("Save Marks"):
                    ok, msg = db.save_grade(enr["enrollment_id"], assignment, quiz, final_exam)
                    if ok:
                        st.success("Marks saved.")
                        st.rerun()
                    else:
                        st.error(msg)
        else:
            st.info("No enrollments available to grade.")

    with tab_del:
        st.subheader("Delete Grade Record")
        grades = db.get_all_grades()
        if grades:
            grd_options = {f"{g['grade_id']} - {g['student_name']} ({g['course_name']})": g for g in grades}
            chosen = st.selectbox("Select grade entry", list(grd_options.keys()))
            grd_del = grd_options[chosen]

            confirm = st.checkbox("Confirm deletion")
            if st.button("Delete Grade", disabled=not confirm):
                ok, msg = db.delete_grade(grd_del["grade_id"])
                if ok:
                    st.success("Grade record deleted.")
                    st.rerun()
                else:
                    st.error(msg)


# Page 7: Reports
elif page == "Reports":
    st.title("Academic & Management Reports")
    st.write("SQL queries answering key business questions from the project brief.")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "BR-01: Popular Courses",
        "BR-02: Instructor Workload",
        "BR-03: Top Students",
        "BR-04: Active Students",
        "BR-05: Enrollment Status",
        "BR-06: Unenrolled Courses"
    ])

    with tab1:
        st.subheader("BR-01: Courses with highest enrollments")
        r1 = db.get_enrollments_per_course()
        if r1:
            df_r1 = pd.DataFrame(r1)
            st.dataframe(df_r1, use_container_width=True, hide_index=True)
            st.bar_chart(df_r1.set_index("course_name")["total_enrollments"])

    with tab2:
        st.subheader("BR-02: Number of courses per instructor")
        r2 = db.get_courses_per_instructor()
        if r2:
            df_r2 = pd.DataFrame(r2)
            st.dataframe(df_r2, use_container_width=True, hide_index=True)
            st.bar_chart(df_r2.set_index("instructor_name")["total_courses"])

    with tab3:
        st.subheader("BR-03: Students with highest total marks")
        top_students = db.get_top_students()
        if top_students:
            st.dataframe(pd.DataFrame(top_students), use_container_width=True, hide_index=True)

        st.write("**Full Student Grade List**")
        all_grades = db.get_student_grades_report()
        if all_grades:
            st.dataframe(pd.DataFrame(all_grades), use_container_width=True, hide_index=True)

    with tab4:
        st.subheader("BR-04: Active student count")
        kpi = db.get_dashboard_kpis()
        c1, c2 = st.columns(2)
        c1.metric("Active Students", kpi["active_students"])
        c2.metric("Total Registered", kpi["total_students"])

    with tab5:
        st.subheader("BR-05: Enrollments by status")
        r5 = db.get_enrollment_status_summary()
        if r5:
            df_r5 = pd.DataFrame(r5)
            st.dataframe(df_r5, use_container_width=True, hide_index=True)
            st.bar_chart(df_r5.set_index("status")["count"])

    with tab6:
        st.subheader("BR-06: Courses with no students enrolled")
        r6 = db.get_courses_with_no_students()
        if r6:
            st.dataframe(pd.DataFrame(r6), use_container_width=True, hide_index=True)
        else:
            st.info("All courses currently have at least one enrolled student.")
