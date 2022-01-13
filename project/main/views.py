from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import ProblemSolve
from .serializers import ProblemSolveSerializer


class PSViewSet(ModelViewSet):
    queryset = ProblemSolve.objects.all()
    serializer_class = ProblemSolveSerializer

def all_problems(request):
    probs_list = ProblemSolve.objects.all().order_by('dateProblem')
    return render(request, "forum/base.html", {'probs_list': probs_list})

def main_page(request):
    return render(request, "main/mainPage.html")
