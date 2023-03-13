from flask import  Flask,jsonify
import csv

app = Flask(__name__)

@app.route("/wholeCSV")
def HandleCSV():
    filename = "E:/employees.csv"
    with open(filename, "r") as foo:
        return jsonify(foo.readlines())

@app.route('/employee_names')
def get_employee_names():
    employee_names = []
    with open('E:/employees.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the header row
        for row in reader:
            employee_names.append(row[1] + " " + row[2])
    return jsonify(employee_names)


# hand = HandleCSV()
# print(hand.read_entire_csv())
# print(hand.get_emp_name())
# # print(hand.read_csv_line_by_line())
