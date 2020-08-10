NWNPayment
Here I Have Tried to Create a Payment Gateway With Valid Inputs like the Following
amount Should be Integer
currency should present in constant.py currency_list = ["USD","INR"]
at place of "type" I Used "paytype"
paytype should be either "creditcard" or "debitcard"
but can be added by adding to variable in list constant.py payment_method = ["debitcard", "creditcard"]

Futher variable are:
Card number it's Length should 16 Further Validation Is done by our code
Card expiry month it should be in range 1-12 Further Validation Is done by our code
Card expiry Year it's length should be 4 Further Validation Is done by our code
Card expiry cvv it's length should be 3 Further Validation Is done by our code

So Let's Start


Getting Started
$ git clone 
$ source nwnpaymentgateway/bin/activate
$ cd nwnpaymentgateway
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver

How to Use:
Just Hit Url = "http://127.0.0.1:8000/admin/pay/cards/add/" in any Browser
Username = "prince"
Passord = "9653"
Add the cards


Now For Manual Testing 
Just Hit Url = "http://127.0.0.1:8000/payment/" with POST Method using API testing Software:
Payload = 
    {
    "amount": "Any INteger",
    "currency": Any from  ["USD","INR"],
    "paytype": Any from ["debitcard", "creditcard"],
    "card":{
        "number": "Any number from Register Card",
        "expirationMonth": "Any month w.r.t Card",
        "expirationYear": "Any Year w.r.t Card",
        "cvv": "CVV w.r.t Card"
    }

    }
Payload Example =
    {
    "amount": "1244",
    "currency": "INR",
    "paytype": "debitcard",
    "card":{
        "number": "4111111111112111",
        "expirationMonth": "12",
        "expirationYear": "2025",
        "cvv": "104"
    }

    }


Just Hit Url = "http://127.0.0.1:8000/payment/get/" with GET Method using API testing Software:

from above url all Transaction details will be visible

Running the tests
$ python mange.py test 

Authors
Prince Agarwal
