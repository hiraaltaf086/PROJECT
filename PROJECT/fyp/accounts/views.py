from django import views
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


class Signup(views.View):
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('eyesion:upload')
        return render(request, 'accounts/signup.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})
