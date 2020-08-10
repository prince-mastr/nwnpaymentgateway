from django.shortcuts import render
from .serializer import payment_check
from rest_framework.views import APIView
from .payment_service import paymenthandler
from rest_framework.response import Response
import logging
from rest_framework import status

logger = logging.getLogger(__name__)
# Create your views here.
class Create_Transaction(APIView):
    """Associates requested connections to groups"""

    def post(self, request):
        try:
            requested_data = request.data
            serializer = payment_check(
                data=requested_data,
                context={"request": request}
            )
            if serializer.is_valid():
                try:
                    new_payment, msg = paymenthandler().create_payment(request, serializer.data)
                    if new_payment:
                        return Response({
                            "status": 200,
                            "data": msg
                        }, status=status.HTTP_200_OK)
                    else:
                        return Response({
                            "status": 400,
                            "data": msg
                        }, status=status.HTTP_200_OK)

                except Exception as e:
                    logger.exception(str(e))
                    return Response({
                        "status": 400,
                        "data": "Service_exception"
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({
                    "status": 400,
                    "data": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(str(e))
            return Response(
                {
                    "status": 500,
                    "data": "Error Creating Transaction"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Get_Transactions(APIView):
    """Associates requested connections to groups"""

    def get(self, request):
        try:
            try:
                new_payment, msg = paymenthandler().get_transactions(request)
                if new_payment:
                    return Response({
                        "status": 200,
                        "data": msg
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({
                        "status": 400,
                        "data": msg
                    }, status=status.HTTP_200_OK)

            except Exception as e:
                logger.exception(str(e))
                return Response({
                    "status": 400,
                    "data": "Service_exception"
                }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception(str(e))
            return Response(
                {
                    "status": 500,
                    "data": "Error Get  Transaction"
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                