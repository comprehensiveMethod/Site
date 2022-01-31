from django.contrib import admin

from .models import ProblemSolve


class PSAdmin(admin.ModelAdmin):
    list_display = ("problem", "solve", "dateProblem", "dateSolve")


admin.site.register(ProblemSolve, PSAdmin)
