# https://www.django-rest-framework.org/api-guide/testing/
from django.test import TestCase
from rest_framework.test import RequestsClient
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import mixins, viewsets

from artifacts.models import Artifact
from people.models import Person
from vehicles.models import Vehicle
from people.serializers import PersonSerializer
from vehicles.serializers import VehicleSerializer

client = RequestsClient()

class ApiTest(TestCase):
    fixtures = ["accounts.json",
                'artifacts.json',
                'books.json',
                'people.json',
                'vehicles.json',
                ]

    def test_receipt(self):
        response = client.get('http/api/v1/listing/')
        print(response)
        # self.assertEqual(expected, total)
