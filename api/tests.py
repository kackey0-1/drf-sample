# https://www.django-rest-framework.org/api-guide/testing/
from django.test import TestCase
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import mixins, viewsets

from artifacts.models import Artifact
from people.models import Person
from vehicles.models import Vehicle
from people.serializers import PersonSerializer
from vehicles.serializers import VehicleSerializer


class ApiTest(TestCase):
    fixtures = ["receipts.json", ]

    def test_receipt(self):
        pass
        # expected = Decimal("37.55")
        # self.assertEqual(expected, total)
