from django.test import TestCase

# Create your tests here.
from .sample_factory import SampleRoleRecordsFactory, DefaultMockPaymentGen
from django.test import TestCase
from django.contrib.auth.models import User
from faker import Faker
from faker.providers import misc
from django.test import tag
from django.test import Client
from .models import Cards
import json


class TestPaymentOperations(TestCase):

    def setUp(self,):
        self.c = Client(HTTP_USER_AGENT='Mozilla/5.0')
        self.faker = Faker()
        self.faker.add_provider(misc)
        self.mock_user = User.objects.create(
            username=self.faker.name()[:19],
            email=self.faker.email(),
        )
        self.mock_user.set_password(
            self.faker.password()
        )
        self.mock_user.save()
        self.c.force_login(self.mock_user)

        self.mock_md_objects = SampleRoleRecordsFactory()\
            .create_records_default(
                user=self.mock_user,
                multiple=True,
                mock_data_ins=DefaultMockPaymentGen(),
                count_of_mocks=100
            )

    @tag("roles")
    def test_mock_dat_create(self,):
        mock_obj = Cards.objects.filter().first()
        payjson = {
                "amount": "1244",
                "currency": "INR",
                "paytype": "debitcard",
                "card":{
                    "number": mock_obj.number,
                    "expirationMonth": mock_obj.expirationMonth,
                    "expirationYear":  mock_obj.expirationYear,
                    "cvv":  mock_obj.cvv
                }

            }
        result = self.c.post(
            "/payment/", data = json.dumps(payjson),
            content_type='application/json'
            
        )
        # Expect that model is created inside database
        self.assertEquals(
            result.json()["data"]["status"],
            "Sucess".upper()
        )
        self.assertEquals(
            result.status_code,
            200
        )
    
    def test_mock_dat_Wrong_Card(self,):
        mock_obj = Cards.objects.filter().first()
        payjson = {
                "amount": "1244",
                "currency": "INR",
                "paytype": "debitcard",
                "card":{
                    "number": 1111111111111111,
                    "expirationMonth": mock_obj.expirationMonth,
                    "expirationYear":  mock_obj.expirationYear,
                    "cvv":  mock_obj.cvv + 1
                }

            }
        result = self.c.post(
            "/payment/", data = json.dumps(payjson),
            content_type='application/json'
            
        )
        # Expect that model is created inside database
        self.assertEquals(
            result.json()["data"]["status"],
            "Card Does Not Exists".upper()
        )
        self.assertEquals(
            result.status_code,
            200
        )
    def test_mock_dat_Wrong_Cvv(self,):
        mock_obj = Cards.objects.filter().first()
        payjson = {
                "amount": "1244",
                "currency": "INR",
                "paytype": "debitcard",
                "card":{
                    "number": mock_obj.number,
                    "expirationMonth": mock_obj.expirationMonth,
                    "expirationYear":  mock_obj.expirationYear,
                    "cvv":  mock_obj.cvv + 1
                }

            }
        result = self.c.post(
            "/payment/", data = json.dumps(payjson),
            content_type='application/json'
            
        )
        # Expect that model is created inside database
        self.assertEquals(
            result.json()["data"]["status"],
            "wrong Cvv".upper()
        )
        self.assertEquals(
            result.status_code,
            200
        )

    def test_mock_dat_Wrong_date(self,):
        mock_obj = Cards.objects.filter().first()
        payjson = {
                "amount": "1244",
                "currency": "INR",
                "paytype": "debitcard",
                "card":{
                    "number": mock_obj.number,
                    "expirationMonth": mock_obj.expirationMonth +1,
                    "expirationYear":  mock_obj.expirationYear,
                    "cvv":  mock_obj.cvv 
                }

            }
        result = self.c.post(
            "/payment/", data = json.dumps(payjson),
            content_type='application/json'
            
        )
        # Expect that model is created inside database
        self.assertEquals(
            result.json()["data"]["status"],
            "wrong Date".upper()
        )
        self.assertEquals(
            result.status_code,
            200
        )
    def tearDown(self,):
        Cards.objects.all().delete()
        User.objects.all().delete()
    
       
