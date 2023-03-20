import csv
from flask import Blueprint
import jsonify


hire_app = Blueprint("hire", __name__, url_prefix="/hire")

@hire_app.route("/hire_date")
def file_reader():
    employees = []
    with open("E:/employees.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            deparment = row[10]
            name = row[1] + " " + row[2]
            salary = int(row[7])
            HIRE_DATE = row[5]
            if 30 <= int(row[10]) <= 110 and int(row[7]) > 4200:
                date = row[5]
                employee = {
                    "name": name,
                    "deparment": deparment,
                    "HIRE_DATE": HIRE_DATE,
                    "salary": salary
                }
                employees.append(employee)
    return employees