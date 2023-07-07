from flask import Flask, render_template, request
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/creditdata', methods=['GET', 'POST'])
def predict_credit_score():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            Age = int(request.form.get('Age')),
            Occupation = request.form.get('Occupation'),
            Annual_Income = float(request.form.get('Annual_Income')),
            Monthly_Inhand_Salary = float(request.form.get('Monthly_Inhand_Salary')),
            Num_Bank_Accounts = int(request.form.get('Num_Bank_Accounts')),
            Num_Credit_Card = int(request.form.get('Num_Credit_Card')),
            Interest_Rate = float(request.form.get('Interest_Rate')),
            Num_of_Loan = int(request.form.get('Num_of_Loan')),
            Delay_from_due_date = int(request.form.get('Delay_from_due_date')),
            Num_of_Delayed_Payment = int(request.form.get('Num_of_Delayed_Payment')),
            Changed_Credit_Limit = float(request.form.get('Changed_Credit_Limit')),
            Num_Credit_Inquiries = int(request.form.get('Num_Credit_Inquiries')),
            Credit_Mix = request.form.get('Credit_Mix'),
            Outstanding_Debt = float(request.form.get('Outstanding_Debt')),
            Credit_Utilization_Ratio = float(request.form.get('Credit_Utilization_Ratio')),
            Payment_of_Min_Amount = request.form.get('Payment_of_Min_Amount'),
            Total_EMI_per_month = float(request.form.get('Total_EMI_per_month')),
            Amount_invested_monthly = float(request.form.get('Amount_invested_monthly')),
            Payment_Behaviour = request.form.get('Payment_Behaviour'),
            Monthly_Balance = float(request.form.get('Monthly_Balance'))
            )
        
        pred_df = data.get_data_as_dataframe()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        result = results[0]

        if result == 0.0:
            result = "The credit score is 'Good'"
        elif result ==1.0:
            result = "The credit score is 'POOR'"
        else:
            result = "The credit score is 'STANDARD'"

        return render_template('home.html', result= result)
    

if __name__=="__main__":
    app.run(host='0.0.0.0')