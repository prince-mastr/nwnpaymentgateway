# Welcome to NWNPayment

Here I Have Tried to Create a Payment Gateway With Valid Inputs like the Following <br />
amount Should be Integer<br />
currency should present in constant.py currency_list = ["USD","INR"] <br />
at place of "type" I Used "paytype" <br />
paytype should be either "creditcard" or "debitcard" <br />
but can be added by adding to variable in list constant.py payment_method = ["debitcard", "creditcard"] <br />

Futher variable are:<br />
Card number it's Length should 16 Further Validation Is done by our code <br />
Card expiry month it should be in range 1-12 Further Validation Is done by our code <br />
Card expiry Year it's length should be 4 Further Validation Is done by our code <br />
Card expiry cvv it's length should be 3 Further Validation Is done by our code <br />

So Let's Start <br />
<br />
<br /> 
# Getting Started <br />

$ git clone <br />
$ source nwnpaymentgateway/bin/activate <br />
$ cd nwnpaymentgateway <br />
$ pip install -r requirements.txt<br />
$ python manage.py makemigrations <br />
$ python manage.py migrate <br />
$ python manage.py runserver <br />


## How to Use: <br />

**Just Hit Url** = "http://127.0.0.1:8000/admin/pay/cards/add/" in any Browser <br />
Username = "prince" <br />
Passord = "9653" <br />
Add the cards <br />


Now For Manual Testing  <br />
**Just Hit Url** = "http://127.0.0.1:8000/payment/" with POST Method using API testing Software:<br />
Payload = <br />
    {
    "amount": "Any Integer",<br />
    "currency": Any from  ["USD","INR"],<br />
    "paytype": Any from ["debitcard", "creditcard"],<br />
    "card":{<br />
        "number": "Any number from Register Card",<br />
        "expirationMonth": "Any month w.r.t Card",<br />
        "expirationYear": "Any Year w.r.t Card",<br />
        "cvv": "CVV w.r.t Card"<br />
    }<br />

    }<br />
Payload Example = <br />
    {
    "amount": "1244",<br />
    "currency": "INR",<br />
    "paytype": "debitcard",<br />
    "card":{<br />
        "number": "4111111111112111",<br />
        "expirationMonth": "12",<br />
        "expirationYear": "2025",<br />
        "cvv": "104"<br />
    }<br />
    
    }<br />


**Just Hit Url** = "http://127.0.0.1:8000/payment/get/" with GET Method using API testing Software: <br />

from above url all Transaction details will be visible <br />

## Running the tests <br />

$ python mange.py test <br />

## Authors <br />
Prince Agarwal 
