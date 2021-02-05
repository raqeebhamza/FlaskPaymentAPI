import requests
from datetime import datetime
# local host 
BASE = "http://127.0.0.1:5000/"

# client is getting ready to send the input on server.....
dateString = "March-2021"
dateObj=datetime.strptime(dateString,"%B-%Y")
print(dateObj)
response = requests.put(BASE + "ProcessPayment",
{"cCardNumber":"030203042340335","holderName":"Raqh","expirationDate":dateObj.strftime("%m-%y"),"securityCode":124,"Amount":80.1})
print(response.json())

