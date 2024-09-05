from django.shortcuts import render

def home(request):
    return render(request, 'hometest_modified.html', {})

