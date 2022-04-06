from rest_framework import serializers

from calculation.models import Calculations


class FibonacciSerializer(serializers.ModelSerializer):
    """
    test
    """
    class Meta:
        model = Calculations
        fields = '__all__'
