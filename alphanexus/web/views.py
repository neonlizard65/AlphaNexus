from multiprocessing import context
from django.shortcuts import render

def index(request):
    context = {"n": range(0, 20)}
    return render(request, "index.html", context=context)