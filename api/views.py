from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from artifacts.models import Artifact
from people.models import Person
from vehicles.models import Vehicle
from people.serializers import PersonSerializer
from vehicles.serializers import VehicleSerializer


@api_view(['GET'])
def listing(request):
    doctors = Person.objects.filter(title='Dr.')
    vehicles = Vehicle.objects.all()

    context = {
        'request': request,
    }
    vehicles_serializer = VehicleSerializer(vehicles, many=True, context=context)

    results = {
        'doctors': PersonSerializer(doctors, many=True).data,
        'vehicles': vehicles_serializer.data,
    }
    return Response(results)
