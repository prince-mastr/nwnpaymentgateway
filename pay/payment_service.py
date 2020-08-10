from django.db import models
import logging
import datetime
from .models import Transaction, Cards
from django.db.models import Q
from uuid import uuid4
from .constants import month_leap_list,month_list
from .serializer import ReadTransaction



logger = logging.getLogger(__name__)


class paymenthandler:

    logger.info("Inside Config Handler")
    def leap(a):
        if (a%4 == 0 and a%100 != 0) or (a%400 == 0) :
            return True
        return False

    def create_payment(self, request, data):
        try:
            correct_cvv = 0
            correct_date = 0
            error_card = 0
            msg = ""
            card = Cards.objects.get(number = data["card"]["number"])
            if card.cvv == int(data["card"]["cvv"]):
                correct_cvv =1
            else:
                msg="wrong Cvv"

            
            if paymenthandler.leap(int(data["card"]["expirationYear"])):
                given_date = datetime.date(int(data["card"]["expirationYear"]), int(data["card"]["expirationMonth"]), month_leap_list[int(data["card"]["expirationMonth"])-1] )
                expiry_date = datetime.date(int(card.expirationYear),int(card.expirationMonth),month_leap_list[int(card.expirationMonth)-1])
                if  expiry_date >= datetime.date.today():
                    if given_date <= expiry_date:
                        correct_date =1
                    else:
                        msg = "wrong date"
                else:
                    msg = "Card Expired"
            else:
                given_date = datetime.date(int(data["card"]["expirationYear"]), int(data["card"]["expirationMonth"]), month_list[int(data["card"]["expirationMonth"])-1] )
                expiry_date = datetime.date(int(card.expirationYear),int(card.expirationMonth),month_list[int(card.expirationMonth)-1])
                if  expiry_date >= datetime.date.today():
                    if given_date <= expiry_date:
                        correct_date =1
                    else:
                        msg = "wrong date"
                else:
                    msg = "Card Expired"
            

        except Cards.DoesNotExist:
            msg = "Card Does Not Exists"
            error_card=1
        except Exception as e:
            logger.exception(str(e))
            msg = "Error in Card Finding"
            error_card = 1

        try:
            if correct_cvv:
                if correct_date:
                    msg = "Sucess"
            if  error_card:
                context = {
                    "amount": data["amount"],
                    "currency": data["currency"],
                    "type": data["paytype"],
                    "card": {
                    "number": data["card"]["number"],
                        },
                    "status": msg.upper(),
                    "authorization_code": "1234567812345678",
                    "time": "000000000000"
                }
                return False, context

            new_payment = Transaction.objects.create(
                amount = data["amount"],
                currency = data["currency"],
                paytype = data["paytype"],
                number=card,
                status = msg.upper(),
            )
        
            
            new_payment.authorization_code = str(uuid4())[:8].upper()
            new_payment.save()

            context = {
                    "amount": new_payment.amount,
                    "currency": new_payment.currency,
                    "type": new_payment.paytype,
                    "card": {
                    "number": new_payment.number.number
                        },
                    "status": new_payment.status,
                    "authorization_code": new_payment.authorization_code,
                    "time": new_payment.create_datetime
            }

            return True, context

        except Exception as e:
            logger.error(str(e))
            msg = "Create Role Failed"
            logger.exception(msg=f"Create Role Failed. {str(e)}")

            return False, msg
    
    def get_transactions(self, request):
        try:
            Transaction_list = Transaction.objects.all()
            if len (Transaction_list):
                payment_list = []
                for payment in Transaction_list:
                    context = ReadTransaction(payment)
                    payment_list.append(context.data)
                return True , payment_list
            return True , "No Transaction has been Made"
        
        except Transaction.DoesNotExist :
            return True , "No Transaction has been Made"
        except Exception as e:
            logger.exception(str(e))
            return False, "Service Falied"




