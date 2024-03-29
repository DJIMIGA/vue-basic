from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accounts.models import CustomUser


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password")
        password2 = request.POST.get("password")
        if password1 != password2:
            return render(request, "accounts/signup.html", {"error": "les mots de passe ne corespondent pas."})
        CustomUser.objects.create_user(username=username, password=password1)
        return HttpResponse(f"bienvenue {username}")

    return render(request, "accounts/signup.html")