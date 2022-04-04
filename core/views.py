from django.shortcuts import redirect
from django.views.generic import View
from django.shortcuts import render, redirect



class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'new_index.html', context)
        