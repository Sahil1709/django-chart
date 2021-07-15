from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import login,logout
from .models import Club

# Create your views here.
class ClubChartView(TemplateView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chartname"] = "Clubs Chart"
        context["pagename"] = "Clubs"
        context["qs"] = Club.objects.all()
        return context

def home(request):
    return render(request,'home.html',{"pagename":"Homepage", "author":"Sahil Gupta"})

def register(request):
    return render(request, 'register.html', {"pagename":"SignUp","author":"Sahil Gupta"})   

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/register")