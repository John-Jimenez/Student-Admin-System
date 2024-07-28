from flask import Flask, jsonify, request
import mysql.connector


app = Flask(__name__)


# Function for connecting to database
def database_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="dbadmin",
        database="xyzuniversitydb"
    )
    return mydb

# Post method for Student table
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    student_id = data['student_id']
    name = data['name']
    address = data['address']
    phone_number = data['phone_number']
    email_address = data['email_address']
    date_of_birth = data['date_of_birth']
    
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "INSERT INTO student (`Student ID`, Name, Address, `Phone Number`, `Email Address`, `Date of Birth`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (student_id, name, address, phone_number, email_address, date_of_birth)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    
    return jsonify({'message': 'Student created successfully.'}), 201


# Function to update the student
@app.route('/students/<student_id>', methods=['PUT'])
def update_student(student_id):
    mydb = database_connection()
    mycursor = mydb.cursor()

    # Get the existing student
    sql = "SELECT * FROM student WHERE `Student ID` = %s"
    val = (student_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        # Update the student's information
        data = request.json
        name = data.get('name', result[1])
        address = data.get('address', result[2])
        phone_number = data.get('phone_number', result[3])
        email_address = data.get('email_address', result[4])
        date_of_birth = data.get('date_of_birth', result[5])

        # Update the student in the database
        sql = "UPDATE student SET Name = %s, Address = %s, `Phone Number` = %s, `Email Address` = %s, `Date of Birth` = %s WHERE `Student ID` = %s"
        val = (name, address, phone_number, email_address, date_of_birth, student_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        return jsonify({'message': 'Student updated successfully.'}), 200
    else:
        return jsonify({'message': 'Student not found.'}), 404


# Function for getting a list of all the students
@app.route('/students', methods=['GET'])
def get_all_students():
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM student"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    mydb.close()

    students = []
    for result in results:
        student = {
            'student_id': result[0],
            'name': result[1],
            'address': result[2],
            'phone_number': result[3],
            'email_address': result[4],
            'date_of_birth': result[5]
        }
        students.append(student)

    return jsonify(students)


# Function for getting a list of all the student IDs
@app.route('/students/ids', methods=['GET'])
def get_all_student_ids():
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT `Student ID` FROM student"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    mydb.close()

    student_ids = []
    for result in results:
        student_ids.append(result[0])

    return jsonify(student_ids)


# Function for getting a student by their ID
@app.route('/students/<student_id>', methods=['GET'])
def get_student(student_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM student WHERE `Student ID` = %s"
    val = (student_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()
    
    if result:
        student = {
            'student_id': result[0],
            'name': result[1],
            'address': result[2],
            'phone_number': result[3],
            'email_address': result[4],
            'date_of_birth': result[5]
        }
        return jsonify(student), 200
    else:
        return jsonify({'message': 'Student not found.'}), 404
    

# DELETE method for deleting a student by their ID
@app.route('/students/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM student WHERE `Student ID` = %s"
    val = (student_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        sql = "DELETE FROM student WHERE `Student ID` = %s"
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        return jsonify({'message': 'Student deleted successfully.'}), 200
    else:
        mydb.close()
        return jsonify({'message': 'Student not found.'}), 404 


# Post method for Professor table
@app.route('/professors', methods=['POST'])
def create_professor():
    data = request.json
    professor_id = data['professor_id']
    department_id = data['department_id']
    name = data['name']
    address = data['address']
    phone_number = data['phone_number']
    email_address = data['email_address']
    
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "INSERT INTO professor (`Professor ID`, `Department ID`, Name, Address, `Phone Number`, `Email Address`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (professor_id, department_id, name, address, phone_number, email_address)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    
    return jsonify({'message': 'Professor created successfully.'}), 201


# Function to update the professor
@app.route('/professors/<professor_id>', methods=['PUT'])
def update_professor(professor_id):
    mydb = database_connection()
    mycursor = mydb.cursor()

    # Get the existing professor
    sql = "SELECT * FROM professor WHERE `Professor ID` = %s"
    val = (professor_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        # Update the professor's information
        data = request.json
        department_id = data.get('department_id', result[1])
        name = data.get('name', result[2])
        address = data.get('address', result[3])
        phone_number = data.get('phone_number', result[4])
        email_address = data.get('email_address', result[5])

        # Update the professor in the database
        sql = "UPDATE professor SET `Department ID` = %s, Name = %s, Address = %s, `Phone Number` = %s, `Email Address` = %s WHERE `Professor ID` = %s"
        val = (department_id, name, address, phone_number, email_address, professor_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        return jsonify({'message': 'Professor updated successfully.'}), 200
    else:
        return jsonify({'message': 'Professor not found.'}), 404


# Function for getting a list of all the professors
@app.route('/professors', methods=['GET'])
def get_all_professors():
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM professor"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    mydb.close()

    professors = []
    for result in results:
        professor = {
            'professor_id': result[0],
            'department_id': result[1],
            'name': result[2],
            'address': result[3],
            'phone_number': result[4],
            'email_address': result[5]            
        }
        professors.append(professor)

    return jsonify(professors)


# Function for getting a professor by their ID
@app.route('/professors/<professor_id>', methods=['GET'])
def get_professor(professor_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM professor WHERE `Professor ID` = %s"
    val = (professor_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()
    
    if result:
        professor = {
            'professor_id': result[0],
            'department_id': result[1],
            'name': result[2],
            'address': result[3],
            'phone_number': result[4],
            'email_address': result[5],
        }
        return jsonify(professor), 200
    else:
        return jsonify({'message': 'Professor not found.'}), 404


# DELETE method for deleting a student by their ID
@app.route('/professors/<professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM professor WHERE `Professor ID` = %s"
    val = (professor_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        sql = "DELETE FROM professor WHERE `Professor ID` = %s"
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        return jsonify({'message': 'Professor deleted successfully.'}), 200
    else:
        mydb.close()
        return jsonify({'message': 'Professor not found.'}), 404
    

# Post method for Department table
@app.route('/departments', methods=['POST'])
def create_departments():
    data = request.json
    department_id = data['department_id']
    department_name = data['department_name']
    
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "INSERT INTO department (`Department ID`, `Department Name`) VALUES (%s, %s)"
    val = (department_id, department_name)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    
    return jsonify({'message': 'Department created successfully.'}), 201

# Function to update the department
@app.route('/departments/<department_id>', methods=['PUT'])
def update_department(department_id):
    mydb = database_connection()
    mycursor = mydb.cursor()

    # Get the existing department
    sql = "SELECT * FROM department WHERE `Department ID` = %s"
    val = (department_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        # Update the department's information
        data = request.json
        department_name = data.get('department_name', result[1])

        # Update the student in the database
        sql = "UPDATE department SET `Department Name` = %s WHERE `Department ID` = %s"
        val = (department_name, department_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        return jsonify({'message': 'Department updated successfully.'}), 200
    else:
        return jsonify({'message': 'Department not found.'}), 404

# Function for getting a list of all the departments
@app.route('/departments', methods=['GET'])
def get_all_departments():
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM department"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    mydb.close()

    departments = []
    for result in results:
        department = {
            'department_id': result[0],
            'department_name': result[1]          
        }
        departments.append(department)

    return jsonify(departments)


# Function for getting a departments by their ID
@app.route('/departments/<department_id>', methods=['GET'])
def get_department(department_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM department WHERE `Department ID` = %s"
    val = (department_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()
    
    if result:
        department = {
            'department_id': result[0],
            'department_name': result[1]
        }
        return jsonify(department), 200
    else:
        return jsonify({'message': 'Department not found.'}), 404


# DELETE method for deleting a student by their ID
@app.route('/departments/<department_id>', methods=['DELETE'])
def delete_department(department_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM department WHERE `Department ID` = %s"
    val = (department_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        sql = "DELETE FROM department WHERE `Department ID` = %s"
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        return jsonify({'message': 'Department deleted successfully.'}), 200
    else:
        mydb.close()
        return jsonify({'message': 'Department not found.'}), 404


# POST method for creating a new course
@app.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    course_id = data['course_id']
    course_name = data['course_name']
    professor_id = data['professor_id']
    instructor_name = data['instructor_name']
    start_time = data['start_time']
    end_time = data['end_time']
    days = data['days']
    room_number = data['room_number']

    mydb = database_connection()
    mycursor = mydb.cursor()

    # Check if the given professor_id and instructor_name match in the Professor table
    sql = "SELECT * FROM professor WHERE `Professor ID` = %s AND Name = %s"
    val = (professor_id, instructor_name)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        # Insert the course into the database
        sql = "INSERT INTO course (`Course ID`, `Course Name`, `Professor ID`, `Instructor Name`, `Start Time`, `End Time`, Days, `Room Number`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (course_id, course_name, professor_id, instructor_name, start_time, end_time, days, room_number)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        return jsonify({'message': 'Course created successfully.'}), 201
    else:
        return jsonify({'message': 'Invalid professor_id or instructor_name.'}), 400


# PUT method for updating an existing course
@app.route('/courses/<course_id>', methods=['PUT'])
def update_course(course_id):
    mydb = database_connection()
    mycursor = mydb.cursor()

    # Get the existing course
    sql = "SELECT * FROM course WHERE `Course ID` = %s"
    val = (course_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        # Update the course's information
        data = request.json
        course_name = data.get('course_name', result[1])
        professor_id = data.get('professor_id', result[2])
        instructor_name = data.get('instructor_name', result[3])
        start_time = data.get('start_time', result[4])
        end_time = data.get('end_time', result[5])
        days = data.get('days', result[6])
        room_number = data.get('room_number', result[7])

        # Check if the given professor_id and instructor_name match in the Professor table
        sql = "SELECT * FROM professor WHERE `Professor ID` = %s AND Name = %s"
        val = (professor_id, instructor_name)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result:
            # Update the course in the database
            sql = "UPDATE course SET `Course Name` = %s, `Professor ID` = %s, `Instructor Name` = %s, `Start Time` = %s, `End Time` = %s, Days = %s, `Room Number` = %s WHERE `Course ID` = %s"
            val = (course_name, professor_id, instructor_name, start_time, end_time, days, room_number, course_id)
            mycursor.execute(sql, val)
            mydb.commit()
            mydb.close()

            return jsonify({'message': 'Course updated successfully.'}), 200
        else:
            return jsonify({'message': 'Invalid professor_id or instructor_name.'}), 400
    else:
        return jsonify({'message': 'Course not found.'}), 404


# Function for getting a list of all courses
@app.route('/courses', methods=['GET'])
def get_all_courses():
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM course"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    mydb.close()

    courses = []
    for result in results:
        course = {
            'course_id': result[0],
            'course_name': result[1],
            'professor_id': result[2],
            'instructor_name': result[3],
            'start_time': result[4],
            'end_time': result[5],
            'days': result[6],
            'room_number': result[7]
        }
        courses.append(course)

    return jsonify(courses)


# Function for getting a course by its ID
@app.route('/courses/<course_id>', methods=['GET'])
def get_course(course_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM course WHERE `Course ID` = %s"
    val = (course_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()
    
    if result:
        course = {
            'course_id': result[0],
            'course_name': result[1],
            'professor_id': result[2],
            'instructor_name': result[3],
            'start_time': result[4],
            'end_time': result[5],
            'days': result[6],
            'room_number': result[7]
        }
        return jsonify(course), 200
    else:
        return jsonify({'message': 'Course not found.'}), 404
    

# DELETE method for deleting a course by its ID
@app.route('/courses/<course_id>', methods=['DELETE'])
def delete_course(course_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM course WHERE `Course ID` = %s"
    val = (course_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        sql = "DELETE FROM course WHERE `Course ID` = %s"
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        return jsonify({'message': 'Course deleted successfully.'}), 200
    else:
        mydb.close()
        return jsonify({'message': 'Course not found.'}), 404
    

# POST method for enrolling a student into a course
@app.route('/enrollments', methods=['POST'])
def create_enrollment():
    data = request.json
    enrollment_id = data['enrollment_id']
    student_id = data['student_id']
    course_id = data['course_id']
    grade = data['grade']
    
    mydb = database_connection()
    mycursor = mydb.cursor()
    
    # Check if the given student_id and course_id exist in the database
    sql = "SELECT * FROM student WHERE `Student ID` = %s"
    val = (student_id,)
    mycursor.execute(sql, val)
    student_exists = mycursor.fetchone() is not None
    
    sql = "SELECT * FROM course WHERE `Course ID` = %s"
    val = (course_id,)
    mycursor.execute(sql, val)
    course_exists = mycursor.fetchone() is not None
    
    if student_exists and course_exists:
        # Insert the course into the database
        sql = "INSERT INTO enrollment (`Enrollment ID`, `Student ID`, `Course ID`, `Grade`) VALUES (%s, %s, %s, %s)"
        val = (enrollment_id, student_id, course_id, grade)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        return jsonify({'message': 'Student enrolled successfully.'}), 201
    else:
        return jsonify({'message': 'Invalid Student ID or Course ID.'}), 400


# Function to update the enrollment
@app.route('/enrollments/<enrollment_id>', methods=['PUT'])
def update_enrollment(enrollment_id):
    mydb = database_connection()
    mycursor = mydb.cursor()

    # Check if the enrollment_id exists in the database
    sql = "SELECT * FROM enrollment WHERE `Enrollment ID` = %s"
    val = (enrollment_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result is None:
        mydb.close()
        return jsonify({'message': 'Enrollment ID does not exist.'}), 400

    # Update the course's information
    data = request.json
    student_id = data.get('student_id', result[1])
    course_id = data.get('course_id', result[2])
    grade = data.get('grade', result[3])

    # Check if the given student_id and course_id exist in the database
    sql = "SELECT * FROM student WHERE `Student ID` = %s"
    val = (student_id,)
    mycursor.execute(sql, val)
    student_exists = mycursor.fetchone() is not None
    
    sql = "SELECT * FROM course WHERE `Course ID` = %s"
    val = (course_id,)
    mycursor.execute(sql, val)
    course_exists = mycursor.fetchone() is not None
    
    if student_exists and course_exists:
        # Update the enrollment in the database
        sql = "UPDATE enrollment SET `Student ID` = %s, `Course ID` = %s, Grade = %s WHERE `Enrollment ID` = %s"
        val = (student_id, course_id, grade, enrollment_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        return jsonify({'message': 'Enrollment updated successfully.'}), 201
    else:
        mydb.close()
        return jsonify({'message': 'Invalid Student ID or Course ID.'}), 400


# Function for getting a list of all enrollments
@app.route('/enrollments', methods=['GET'])
def get_all_enrollments():
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM enrollment"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    mydb.close()

    enrollments = []
    for result in results:
        enrollment = {
            'enrollment_id': result[0],
            'student_id': result[1],
            'course_id': result[2],
            'grade': result[3]
        }
        enrollments.append(enrollment)

    return jsonify(enrollments)


# Function for getting an enrollment by the ID
@app.route('/enrollments/<enrollment_id>', methods=['GET'])
def get_enrollment(enrollment_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM enrollment WHERE `Enrollment ID` = %s"
    val = (enrollment_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()

    if result:
        enrollment = {
            'enrollment_id': result[0],
            'student_id': result[1],
            'course_id': result[2],
            'grade': result[3]
        }
        return jsonify(enrollment), 200
    else:
        return jsonify({'message': 'Enrollment not found.'}), 404
    

# DELETE method for deleting a enrollment by its ID
@app.route('/enrollments/<enrollment_id>', methods=['DELETE'])
def delete_enrollment(enrollment_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM enrollment WHERE `Enrollment ID` = %s"
    val = (enrollment_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        sql = "DELETE FROM enrollment WHERE `Enrollment ID` = %s"
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        return jsonify({'message': 'Enrollment deleted successfully.'}), 200
    else:
        mydb.close()
        return jsonify({'message': 'Enrollment not found.'}), 404


# POST method for creating a schedule for a student
@app.route('/schedules', methods=['POST'])
def create_schedule():
    data = request.json
    schedule_id = data['schedule_id']
    student_id = data['student_id']
    course_id = data['course_id']
    start_time = data['start_time']
    end_time = data['end_time']
    room_number = data['room_number']
    
    mydb = database_connection()
    mycursor = mydb.cursor()
    
    # Check if the given student_id and course_id exist in the database
    sql = "SELECT * FROM student WHERE `Student ID` = %s"
    val = (student_id,)
    mycursor.execute(sql, val)
    student_exists = mycursor.fetchone() is not None
    
    sql = "SELECT * FROM course WHERE `Course ID` = %s"
    val = (course_id,)
    mycursor.execute(sql, val)
    course_exists = mycursor.fetchone() is not None
    
    if student_exists and course_exists:
        # Insert the course into the database
        sql = "INSERT INTO schedule (`Schedule ID`, `Student ID`, `Course ID`, `Start Time`, `End Time`, `Room Number`) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (schedule_id, student_id, course_id, start_time, end_time, room_number)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        return jsonify({'message': 'Schedule created successfully.'}), 201
    else:
        return jsonify({'message': 'Invalid Student ID or Course ID.'}), 400


# Function to update the enrollment
@app.route('/schedules/<schedule_id>', methods=['PUT'])
def update_schedule(schedule_id):
    mydb = database_connection()
    mycursor = mydb.cursor()

    # Check if the schedule exists in the database
    sql = "SELECT * FROM schedule WHERE `Schedule ID` = %s"
    val = (schedule_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    if result is None:
        mydb.close()
        return jsonify({'message': 'Enrollment ID does not exist.'}), 400

    # Update the course's information
    data = request.json
    student_id = data.get('student_id', result[1])
    course_id = data.get('course_id', result[2])
    start_time = data.get('start_time', result[3])
    end_time = data.get('end_time', result[4])
    room_number = data.get('room_number', result[5])

    # Check if the given student_id and course_id exist in the database
    sql = "SELECT * FROM student WHERE `Student ID` = %s"
    val = (student_id,)
    mycursor.execute(sql, val)
    student_exists = mycursor.fetchone() is not None
    
    sql = "SELECT * FROM course WHERE `Course ID` = %s"
    val = (course_id,)
    mycursor.execute(sql, val)
    course_exists = mycursor.fetchone() is not None
    
    if student_exists and course_exists:
        # Update the schedule in the database
        sql = "UPDATE schedule SET `Student ID` = %s, `Course ID` = %s, `Start Time` = %s, `End Time` = %s, `Room Number` = %s WHERE `Schedule ID` = %s"
        val = (student_id, course_id, start_time, end_time, room_number, schedule_id)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()

        return jsonify({'message': 'Enrollment updated successfully.'}), 201
    else:
        mydb.close()
        return jsonify({'message': 'Invalid Student ID or Course ID.'}), 400


# Function for getting a list of all schedules 
@app.route('/schedules', methods=['GET'])
def get_all_schedules():
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM schedule"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    mydb.close()

    schedules = []
    for result in results:
        schedule = {
            'schedule_id': result[0],
            'student_id': result[1],
            'course_id': result[2],
            'start_time': result[3],
            'end_time': result[4],
            'room_number': result[5]
        }
        schedules.append(schedule)

    return jsonify(schedules)


# Function for getting an enrollment by the ID
@app.route('/schedules/<schedule_id>', methods=['GET'])
def get_schedule(schedule_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM schedule WHERE `Schedule ID` = %s"
    val = (schedule_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    mydb.close()

    if result:
        schedule = {
            'schedule_id': result[0],
            'student_id': result[1],
            'course_id': result[2],
            'start_time': result[3],
            'end_time': result[4],
            'room_number': result[5]
        }
        return jsonify(schedule), 200
    else:
        return jsonify({'message': 'Schedule not found.'}), 404


# DELETE method for deleting a schedule by its ID
@app.route('/schedules/<schedule_id>', methods=['DELETE'])
def delete_schedule(schedule_id):
    mydb = database_connection()
    mycursor = mydb.cursor()
    sql = "SELECT * FROM schedule WHERE `Schedule ID` = %s"
    val = (schedule_id,)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result:
        sql = "DELETE FROM schedule WHERE `Schedule ID` = %s"
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        return jsonify({'message': 'Schedule deleted successfully.'}), 200
    else:
        mydb.close()
        return jsonify({'message': 'Schedule not found.'}), 404


if __name__ == '__main__':
    app.run(debug=True)