from django.shortcuts import render
from .models import Category
from django.views.generic import View

class IndexView(View):
    def get(self, request):
        essay_objects = Category.objects.filter(is_pass=True)

