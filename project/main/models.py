from django.db import models


class ProblemSolve(models.Model):
    problem = models.CharField(max_length=500)
    solve = models.CharField(max_length=1000)
    dateProblem = models.DateField()
    dateSolve = models.DateField()
