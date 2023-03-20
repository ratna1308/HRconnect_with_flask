from flask import Flask

from task_three_blue import tasks_app
from sub_three_blue import hire_app
from sub_three_next import full_app


app = Flask(__name__)

app.register_blueprint(tasks_app)
app.register_blueprint(hire_app)
app.register_blueprint(full_app)