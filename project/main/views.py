from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ProblemSolve
from .serializers import ProblemSolveSerializer


class PSViewSet(ModelViewSet):
    queryset = ProblemSolve.objects.all()
    serializer_class = ProblemSolveSerializer


def main_page(request):
    return render(request, "main/mainPage.html")
