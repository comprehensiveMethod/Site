from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from .models import ProblemSolve
from .serializers import ProblemSolveSerializer
from .forms import ProblemSolveForm


class PSViewSet(ModelViewSet):
    queryset = ProblemSolve.objects.all()
    serializer_class = ProblemSolveSerializer


def all_problems(request):
    probs_list = ProblemSolve.objects.all().order_by('dateProblem')
    return render(request, "forum/base.html", {'probs_list': probs_list})


def main_page(request):
    return render(request, "main/mainPage.html")


def add(request):
    error = ''
    if request.method == 'POST':
        form = ProblemSolveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Неверная форма'

    form = ProblemSolveForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, "add/add.html", data)


class Search(ListView):
    model = ProblemSolve
    template_name = 'main/searchResult.html'

    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = ProblemSolve.objects.filter(
            Q(problem__icontains=query) | Q(dateProblem__icontains=query)
        )
        return object_list

