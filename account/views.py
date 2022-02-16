from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create(username=username, email=email, password1=password1, first_name=first_name, last_name=last_name)
        user.save()

        return redirect('leads:leadList')

    return render(request, 'account/register.html')
