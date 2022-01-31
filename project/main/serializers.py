from rest_framework.serializers import ModelSerializer
from .models import ProblemSolve


class ProblemSolveSerializer(ModelSerializer):
    class Meta:
        model = ProblemSolve
        fields = '__all__'
