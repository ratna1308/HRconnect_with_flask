import csv
from flask import Blueprint
import jsonify

full_app = Blueprint("full", __name__, url_prefix="/full")


@full_app.route("/wholeCSV")
def HandleCSV():
    filename = "E:/employees.csv"
    with open(filename, "r") as foo:
        return foo.readlines()
