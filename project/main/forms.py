from .models import ProblemSolve
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ProblemSolveForm(ModelForm):
    class Meta:
        model = ProblemSolve
        fields = ['problem', 'solve', 'dateProblem', 'dateSolve']
        widjets = {
            "problem": TextInput(attrs= {
                'class': 'form_control',
                'placeholder': 'Проблема'
            }),
            "solve": Textarea(attrs={
                'class': 'form_control',
                'placeholder': 'Решение'
            }),
            "dateProblem": DateTimeInput(attrs={
                'class': 'form_control',
                'placeholder': 'Дата проблемы'
            }),
            "dateSolve": DateTimeInput(attrs={
                'class': 'form_control',
                'placeholder': 'Дата решения'
            })
        }