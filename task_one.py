from flask import Flask , jsonify
# import csv
#
# app = Flask(__name__)
#
# @app.route("/")
# def file_reader():
#     with open("F:\Python\employees.csv", "r") as file:
#         reader = csv.reader(file)
#         next(reader)
#         employee = {}
#         for row in reader:
#             name = row[1] + " " + row[2]
#             email = row[3]
#             phone_number = row[4].replace(".", "")
#             salary = int(row[7])
#             if salary > 9000:
#                 employees = {
#                     print("Employee Name: ", name),
#                     print("Employee email: ", email),
#                     print("Employee phone number: ", phone_number),
#                     print("Salary: ", salary),
#                     print("-------------------"),
#                 }
#                 employees.append(employee)
#     return jsonify(employees)

from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route("/salary")
def file_reader():
    employees = []
    with open("E:/employees.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name = row[1] + " " + row[2]
            email = row[3]
            phone_number = row[4].replace(".", "")
            salary = int(row[7])
            if salary > 9000:
                employee = {
                    "name": name,
                    "email": email,
                    "phone_number": phone_number,
                    "salary": salary
                }
                employees.append(employee)
    return jsonify(employees)