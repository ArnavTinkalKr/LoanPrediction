# save this as app.py
# pylint: disable=unused-import
import numpy as np
import sklearn
from flask import Flask, request, render_template
import pickle
import joblib


model = joblib.load('/home/tinkal/Desktop/LoanPredictionProject/model.pkl')

# model1 = joblib.load('/home/tinkal/Desktop/LoanPredictionProject/model1.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method ==  'POST':
        gender = request.form['gender']
        married = request.form['married']
        dependents = request.form['dependents']
        education = request.form['education']
        employed = request.form['employed']
        credit = float(request.form['credit'])
        area = request.form['area']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])

        # gender
        if (gender == "Male"):
            male=1
        else:
            male=0
        
        # married
        if(married=="Yes"):
            married_yes = 1
        else:
            married_yes=0

        # dependents
        if(dependents=='1'):
            dependents_1 = 1
            dependents_2 = 0
            dependents_3 = 0
        elif(dependents == '2'):
            dependents_1 = 0
            dependents_2 = 1
            dependents_3 = 0
        elif(dependents=="3+"):
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 1
        else:
            dependents_1 = 0
            dependents_2 = 0
            dependents_3 = 0  

        # education
        if (education=="Not Graduate"):
            not_graduate=1
        else:
            not_graduate=0

        # employed
        if (employed == "Yes"):
            employed_yes=1
        else:
            employed_yes=0

        # property area

        if(area=="Semiurban"):
            semiurban=1
            urban=0
        elif(area=="Urban"):
            semiurban=0
            urban=1
        else:
            semiurban=0
            urban=0

        ApplicantIncomelog = np.log(ApplicantIncome)
        totalincomelog = np.log(ApplicantIncome+CoapplicantIncome)
        LoanAmountlog = np.log(LoanAmount)
        Loan_Amount_Termlog = np.log(Loan_Amount_Term)


        prediction = model.predict([[credit, ApplicantIncomelog,LoanAmountlog, Loan_Amount_Termlog, totalincomelog, male, married_yes, dependents_1, dependents_2, dependents_3, not_graduate, employed_yes,semiurban, urban ]])

        # print(prediction)

        if(prediction=="N"):
            prediction="No"
        else:
            prediction="Yes"


        return render_template("prediction.html", prediction_text="loan status is {}".format(prediction))




    else:
        return render_template("prediction.html")
    
# define route for the about page
@app.route('/about')
def about():
    return render_template('aboutus.html')


"""
# define route to handle loan calculation
@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        # validate loan data from form
        p = request.form.get("PrincipalAmount")
        R = request.form.get("AnnualInterestRate")
        n = request.form.get("EntarNumberOfMounth")

        if p and R and n:
            # All form fields are present and non-empty
            p = float(p)
            R = float(R)
            n = int(n)

            # calculate interest rate per month
            r = R / (12 * 100)

            # calculate equated monthly installment (EMI)
            emi = p * r * ((1+r)**n) / ((1+r)**n - 1)
            
            # determine loan status based on EMI
            if emi <= 0:
                status = "Invalid input"
            elif emi <= 10000:
                status = "Approved"
            else:
                status = "Rejected"
            
        # render result template with EMI and prediction
        #return render_template("result.html", result_text="EMI is {} and loan status is {}".format(emi, status))
    else:
        return render_template("result.html")

"""


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST': 
       loan_amount = int(request.form.get('loan_amount'))
       tenure = int(request.form.get('tenure'))
       interest_rate = float(request.form.get('interest_rate'))
       monthly_interest_rate = interest_rate/(12*100)
       monthly_emi = (loan_amount*monthly_interest_rate*((1+monthly_interest_rate)**tenure))/(((1+monthly_interest_rate)**tenure)-1)
       total_amount_payable = monthly_emi*tenure

       
       #return render_template("result.html", result_text="monthly_emi is {}, loan_amount is {}, total_amount_payable is {}".format(round(monthly_emi, 2), loan_amount, round(total_amount_payable, 2)))
       #return render_template("result.html", result_text="EMI is {} and loan status is {}.format(emi, status))
    
    
       return render_template("result.html", emi_text ="Monthly EMI is: {}".format(round(monthly_emi, 2)), loanamount_text ="Loan Amount Is: {}".format(loan_amount), totalpayble_text ="Total Amount Pyable Is: {}".format(round(total_amount_payable, 2)))
    return render_template("result.html")
    


if __name__ == "__main__":
    app.run(debug=True, port=5000)







 
 