import pickle
import numpy as np
import json

def get_loan_status(Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,Credit_History,Property_Area):
    mobile_path = r"Loan...KNN_clf_model.pkl"
    mobile_path_J = r'colum_data1.json'

    with open(mobile_path, 'rb') as f:
      model = pickle.load(f)

      with open(mobile_path_J, "r") as f:
       data = json.load(f)
       Gender = data["Gender"][Gender]
       Married = data["Married"][Married]
       Education = data["Education"][Education]
       Self_Employed = data["Self_Employed"][Self_Employed]
       Property_Area = data["Property_Area"][Property_Area]



       test_array = np.zeros((1,model.n_features_in_))
      # test_array = [Gender, Married, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,Credit_History,Property_Area]
       
       
       test_array[0][0] = Gender
       test_array[0][1] = Married
       test_array[0][2] = Education
       test_array[0][3] = Self_Employed
       test_array[0][9] = Property_Area
       predicted_class = model.predict(test_array)[0]
      # print("predicted_class :",predicted_class)


      Loan_status = "Approved" if predicted_class == 1 else "Not Approved"
      print("Loan Prediction:", Loan_status)

      
      return Loan_status

