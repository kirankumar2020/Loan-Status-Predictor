from flask import Flask,request,render_template,url_for,jsonify
import numpy as np
import pickle,json
from utils import get_loan_status
from config import PORT_NUMBER



app = Flask(__name__)

@app.route("/home",methods = ["GET","POST"])
def home():

    return render_template("index.html")



@app.route("/loan_status",methods = ["GET","POST"])
def loan_status():
    result  = None
    if request.method == "POST":
      data_f = request.form
      Gender = data_f["Gender"]
      Married = data_f["Married"]
      Education = data_f["Education"]
      Self_Employed = data_f["Self_Employed"]
      ApplicantIncome = int(data_f["ApplicantIncome"])
      CoapplicantIncome = int(data_f["CoapplicantIncome"])
      LoanAmount = int(data_f["LoanAmount"])
      Loan_Amount_Term = int(data_f["Loan_Amount_Term"])
      Credit_History = float(data_f["Credit_History"])
      Property_Area = data_f["Property_Area"]


      result = get_loan_status(Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,Credit_History,Property_Area)
    
      return render_template("index.html",prediction = f"{result}")
    

    return render_template("index.html")
  


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=PORT_NUMBER,debug=False)