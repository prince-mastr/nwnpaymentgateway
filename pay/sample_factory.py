from django.contrib.auth.models import User
from pay.models import Cards
from faker import Faker
from abc import ABC, abstractmethod
from typing import List
import string
import datetime
import random


class IDefaultMockPaymentGen(ABC):

    @abstractmethod
    def generate_single_record(self, user: User) -> Cards:
        pass

    @abstractmethod
    def generate_multiple_record(self, user: User) -> Cards:
        pass


class DefaultMockPaymentGen(IDefaultMockPaymentGen):
    def __init__(self,):
        self.faker = Faker()

    def generate_single_record(self, user: User):
        fake_card_obj = Cards.objects.create(
            number = random.randint(1000000000000000,9999999999999999),
            expirationMonth= random.randint(1,12),
            expirationYear = random.randint(2016,2050),
            cvv = random.randint(100,999)
        )
        fake_card_obj.save()

        return fake_card_obj

    def generate_multiple_record(
        self,
        user: User,
        count_of_mocks: int
    ) -> List[Cards]:
        mock_items = []
        count = 0
        for i in range(count_of_mocks):
            mock_items.append(
                Cards(
                    number = random.randint(2000000000000000,9999999999999999),
                    expirationMonth= random.randint(1,12),
                    expirationYear = random.randint(2021,2050),
                    cvv = random.randint(100,999)
                    
                )
            )
            count = count+1
        Cards.objects.bulk_create(mock_items)
        return mock_items


class SampleRoleRecordsFactory():
    def __init__(self,):
        self.faker = Faker()

    def create_records_default(
        self,
        user: User,
        multiple: False,
        count_of_mocks: 0,
        mock_data_ins: IDefaultMockPaymentGen
    ):
        """Creates sample Payment records"""
        if multiple:
            return mock_data_ins.generate_multiple_record(
                user,
                count_of_mocks
            )
        else:
            return mock_data_ins.generate_single_record(
                user
            )
