from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import json
import re
from datetime import datetime

from extentions import db
from models import InputsProduct1

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///finnish.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")


# TODO: q6q7
# TODO: define function and use it here to generate output
# TODO: add output to database
@app.route("/generate", methods=['POST'])
def generate():
    data = request.get_json()

    q1, q2 = data.get("q1"), data.get("q2"), 
    q3, q4, q5 = data.get("q3"), data.get("q4"), data.get("q5")
    q6, q7 = data.get("q6"), data.get("q7")
    datetimenow = datetime.now()

    input = InputsProduct1( 
                Userid=1, 
                DataCreated = datetimenow,
                Industry = q1,
                ProductDescription = q2,
                BusinessModel = q3,
                TargetAudience = q4,
                MonthlyBudget = q5,
                PreferredChannel = q6,
                PrimaryGoal = q7,
            )
    db.session.add(input)
    db.session.commit()
    return jsonify({'fourP':"Welcome to first app", 'model':'result.inserted_id'})


@app.before_request
def db_connectoin():
    db.create_all()
    print('database was connected!')

if __name__ == "__main__":
    app.run(debug=True)
