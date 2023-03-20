
import csv
from flask import Blueprint
import jsonify


tasks_app = Blueprint("task", __name__, url_prefix="/task")

@tasks_app.route("/salary")
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
    return employees

