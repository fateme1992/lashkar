from django.shortcuts import render

# Create your views here.
def home(reauest):
    return render(reauest, 'book/home2.html')
