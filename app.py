from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import json
import re
from datetime import datetime

from extentions import db
from models import InputsProduct1
from utils import functions as fc
from utils import tests as tst
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

    Industry, ProductDescription = data.get("q1"), data.get("q2"), 
    BusinessModel, TargetAudience, MonthlyBudget = data.get("q3"), data.get("q4"), data.get("q5")
    PreferredChannel, PrimaryGoal = data.get("q6"), data.get("q7")
    datetimenow = datetime.now()

    input = InputsProduct1( 
                Userid=1, 
                DataCreated = datetimenow,
                Industry = Industry,
                ProductDescription = ProductDescription,
                BusinessModel = BusinessModel,
                TargetAudience = TargetAudience,
                MonthlyBudget = MonthlyBudget,
                PreferredChannel = PreferredChannel,
                PrimaryGoal = PrimaryGoal,
            )
    db.session.add(input)
    db.session.commit()

    if not tst.product1_inputcheck(data):
        return 'input product 1 is not ok'
    
    response_product1_agent = fc.product1_agent(               
                                    Industry,
                                    ProductDescription,
                                    BusinessModel,
                                    TargetAudience,
                                    MonthlyBudget,
                                    PreferredChannel,
                                    PrimaryGoal)
    
    
    if not tst.product1_outputcheck(response_product1_agent):
        return 'output product 1 is not ok'
    



    return jsonify({'fourP':"Welcome to first app", 'model':f'{response_product1_agent}'})




@app.before_request
def db_connectoin():
    db.create_all()
    print('database was connected!')

if __name__ == "__main__":
    app.run(debug=True)
