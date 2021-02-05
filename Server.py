from flask import Flask 
from flask_restful import Api,Resource,reqparse, abort
from datetime import datetime
from predictionLogic import predictGateway
app = Flask(__name__)
api = Api(app)

# argument Parser for requesting the Server
put_args=reqparse.RequestParser()
put_args.add_argument("cCardNumber",type=str,help="Error: Credit Card Number is required!",required=True)
put_args.add_argument("holderName",type=str,help="Error: Card Holder Name is required!",required=True)
put_args.add_argument("expirationDate",type=str,help="Error: Date is required!",required=True)
put_args.add_argument("securityCode",type=str,help="Security Code is optional!")
put_args.add_argument("Amount",type=float,help="Error: Amount is required!",required=True)

#helping Functions...........
def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

# validation of the input parameters

class validating():
    def expiryDate(dateObj):
        if(datetime.now()>dateObj):
            abort(400,message="Error: Expiry Date has Passed")
    def CreditCardNumber(cc_num):  # Luhn Algorithm check to validate the credit Card NUmber
        cc_num = cc_num[::-1]
        cc_num = [int(x) for x in cc_num]
        doubled_second_digit_list = list()
        digits = list(enumerate(cc_num, start=1))
        for index, digit in digits:
            if index % 2 == 0:
                doubled_second_digit_list.append(digit * 2)
            else:
                doubled_second_digit_list.append(digit)
        doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
        sum_of_digits = sum(doubled_second_digit_list)
        return sum_of_digits % 10 == 0
    def SecurityCode(secCode):
        if(secCode):
            if(len(str(secCode))!= 3):
                abort(400,message="Error:Invalid length of Security Code!")
    def Amount(am):
        if(am<0 or not (isinstance(am, float))):
            abort(400,message="Error: Invalid Amount has been Entered!")

class ProcessPayment(Resource):  # Process payment method to handle the clients request....
    def put(self):
        args=put_args.parse_args()
        validating.expiryDate(datetime.strptime(args["expirationDate"],"%m-%y"))
        if(not (validating.CreditCardNumber(args["cCardNumber"]))):
            abort(400,message="Error: Credit Card Number is not Valid!")
        validating.SecurityCode(args["securityCode"])
        validating.Amount(args["Amount"]) 
        print(predictGateway.predict(args["Amount"]))
        return args

api.add_resource(ProcessPayment,"/ProcessPayment")
if __name__ == "__main__":
    app.run(debug=True)