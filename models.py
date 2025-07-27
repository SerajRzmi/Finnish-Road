from datetime import datetime
from extentions import db



# TODO:USE MONGODB
class InputsProduct1(db.Model):
    __tablename__ = 'inputs_product1'
    ID = db.Column(db.Integer, primary_key=True)
    Userid = db.Column(db.String(50))
    DataCreated = db.Column(db.DateTime, default=datetime.now())
    Industry = db.Column(db.String(150))
    ProductDescription = db.Column(db.String(500))
    BusinessModel = db.Column(db.String(150))
    TargetAudience = db.Column(db.String(150))
    MonthlyBudget = db.Column(db.String(150))
    PreferredChannel = db.Column(db.String(150))
    PrimaryGoal = db.Column(db.String(150))


# TODO:USE NOGODB
class OutputsProduct1(db.Model):
    __tablename__ = 'outputs_product1'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(50))
    dataCreated = db.Column(db.DateTime, default=datetime.now())
    p1q1_Industry = db.Column(db.String(150))
    p1q2_ProductDescription = db.Column(db.String(500))
    p1q3_BusinessModel = db.Column(db.String(150))
    p1q4_targetAudience = db.Column(db.String(150))
    p1q5_monthlyBudget = db.Column(db.String(150))
    p1q6_preferred = db.Column(db.String(150))
    p1q7_primaryGoal = db.Column(db.String(150))