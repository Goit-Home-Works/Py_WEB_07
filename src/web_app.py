
from flask import Flask, render_template, request, jsonify
import psycopg2
from psycopg2 import Error

class MyApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        self.app.route('/')(self.index)
        self.app.route('/grades')(self.grades)
        self.app.route('/groups')(self.groups)
        self.app.route('/students')(self.students)
        self.app.route('/subjects')(self.subjects)
        self.app.route('/teachers')(self.teachers)
        
    def run(self):
        self.app.run(debug=True, port=5005)

    def db_connection(self):
        try:
            return psycopg2.connect(user='postgres', password='sergio', host='localhost', port='5432', dbname='postgres')
        except Error as e:
            print(f"Error connecting to PostgreSQL: {e}")
            return None


        
    def query_db(self, query):
        conn = self.db_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(query)
                result = cur.fetchall()
                cur.close()
                conn.close()
                return result
            except Error as e:
                print(f"Error executing query: {e}")
                return None

    def index(self):
        return render_template('index.html')

    def grades(self):
        query = 'SELECT * FROM grades'
        grades = self.query_db(query)
        
        message = 'No grades available' if not grades else None
        return render_template('grades.html', grades=grades, message=message)

    def groups(self):
        query = 'SELECT * FROM groups'
        groups = self.query_db(query)
        message = 'No groups available' if not groups else None
        return render_template('groups.html', groups=groups, message=message)

    def students(self):
        query = 'SELECT * FROM students'
        
        students = self.query_db(query)
        
        message = 'No students available' if not students else None
        return render_template('students.html', students=students, message=message)

    def subjects(self):
        query = 'SELECT * FROM subjects'
        subjects = self.query_db(query)
        
        message = 'No subjects available' if not subjects else None
        return render_template('subjects.html', subjects=subjects, message=message)

    def teachers(self):
        query = 'SELECT * FROM teachers'
        teachers = self.query_db(query)
        
        message = 'No teachers available' if not teachers else None
        return render_template('teachers.html', teachers=teachers, message=message)
    
if __name__ == '__main__':
    my_app = MyApp()
    my_app.run()
