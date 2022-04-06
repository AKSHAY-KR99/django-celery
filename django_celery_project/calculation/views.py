from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Calculations
from .serializers import FibonacciSerializer
from calculation.tasks import fibonacci_task
from rest_framework.generics import GenericAPIView


# Create your views here.

class FibonacciView(APIView):

    def post(self, request):
        n = request.data['fib_num']
        calculation = Calculations.objects.create(
            equation=Calculations.EQUATION_FIBONACCI,
            input=int(n),
            status=Calculations.STATUSES
        )
        fibonacci_task.delay(calculation.id)
        return Response({'detail': "Fib created"}, status=status.HTTP_201_CREATED)


class FibonacciList(APIView):
    def get(self, request):
        calc = Calculations.objects.filter(mode=True)
        serializer_data = FibonacciSerializer(calc, many=True)
        return Response({'data': serializer_data.data}, status=status.HTTP_200_OK)
