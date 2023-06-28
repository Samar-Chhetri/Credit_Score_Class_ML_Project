import os, sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = 'artifacts\model.pkl'
            preprocessor_path = 'artifacts\preprocessor.pkl'
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)

            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)

class CustomData:
    def __init__(self, Age:int, Occupation:str, Annual_Income:float, Monthly_Inhand_Salary:float, Num_Bank_Accounts:int, Num_Credit_Card:int, 
                 Interest_Rate:float, Num_of_Loan:int, Delay_from_due_date:int, Num_of_Delayed_Payment:int, Changed_Credit_Limit:float,
                 Num_Credit_Inquiries:int, Credit_Mix:str, Outstanding_Debt:float, Credit_Utilization_Ratio:float, Payment_of_Min_Amount:str, 
                 Total_EMI_per_month:float, Amount_invested_monthly:float, Payment_Behaviour:str, Monthly_Balance:float):
        
        self.Age = Age
        self.Occupation = Occupation
        self.Annual_Income = Annual_Income
        self.Monthly_Inhand_Salary = Monthly_Inhand_Salary
        self.Num_Bank_Accounts = Num_Bank_Accounts
        self.Num_Credit_Card = Num_Credit_Card
        self.Interest_Rate = Interest_Rate
        self.Num_of_Loan = Num_of_Loan
        self.Delay_from_due_date = Delay_from_due_date
        self.Num_of_Delayed_Payment = Num_of_Delayed_Payment
        self.Changed_Credit_Limit = Changed_Credit_Limit
        self.Num_Credit_Inquiries = Num_Credit_Inquiries
        self.Credit_Mix = Credit_Mix
        self.Outstanding_Debt = Outstanding_Debt
        self.Credit_Utilization_Ratio = Credit_Utilization_Ratio
        self.Payment_of_Min_Amount = Payment_of_Min_Amount
        self.Total_EMI_per_month = Total_EMI_per_month
        self.Amount_invested_monthly = Amount_invested_monthly
        self.Payment_Behaviour = Payment_Behaviour
        self.Monthly_Balance = Monthly_Balance



    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "Age": [self.Age],
                "Occupation": [self.Occupation],
                "Annual_Income": [self.Annual_Income],
                "Monthly_Inhand_Salary": [self.Monthly_Inhand_Salary],
                "Num_Bank_Accounts": [self.Num_Bank_Accounts],
                "Num_Credit_Card": [self.Num_Credit_Card],
                "Interest_Rate": [self.Interest_Rate],
                "Num_of_Loan": [self.Num_of_Loan],
                "Delay_from_due_date": [self.Delay_from_due_date],
                "Num_of_Delayed_Payment": [self.Num_of_Delayed_Payment],
                "Changed_Credit_Limit": [self.Changed_Credit_Limit],
                "Num_Credit_Inquiries": [self.Num_Credit_Inquiries],
                "Credit_Mix": [self.Credit_Mix],
                "Outstanding_Debt": [self.Outstanding_Debt],
                "Credit_Utilization_Ratio": [self.Credit_Utilization_Ratio],
                "Payment_of_Min_Amount": [self.Payment_of_Min_Amount],
                "Total_EMI_per_month": [self.Total_EMI_per_month],
                "Amount_invested_monthly": [self.Amount_invested_monthly],
                "Payment_Behaviour": [self.Payment_Behaviour],
                "Monthly_Balance": [self.Monthly_Balance]      
            }

            return pd.DataFrame(custom_data_input_dict)


        except Exception as e:
            raise CustomException(e, sys)












