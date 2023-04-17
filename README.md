Loan Prediction with EMI Calculation

This is a machine learning project that predicts whether a loan application will be approved or not based on various features such as income, credit score, loan amount, etc. Additionally, the project also calculates the EMI (Equated Monthly Installment) for the approved loan amount.
Getting Started

To get started with this project, you'll need to install the required dependencies:

shell

pip install -r requirements.txt

Once you have installed the dependencies, you can run the Flask web application:

shell

python app.py

This will start the web application on http://localhost:5000/.
Usage

To use the loan prediction model, navigate to the home page and fill out the loan application form with the required details such as income, credit score, loan amount, and loan term. Then, click the "Calculate EMI" button to submit the form.

The machine learning model will then process the input and predict whether the loan application will be approved or not. If the loan is approved, the EMI will be calculated and displayed on the result page along with the loan amount and total amount payable.
Data

The loan prediction model was trained on a dataset of past loan applications and their outcomes. The dataset includes various features such as income, credit score, loan amount, loan term, etc.
Model

The loan prediction model is built using a Random Forest Classifier algorithm. The model achieves an accuracy of around 80% on the training and testing data.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    The dataset used for training the model was obtained from Kaggle.
    The machine learning model was built using scikit-learn.
    The web application was built using Flask.
