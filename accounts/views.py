from django.shortcuts import render, redirect
from django.views import View
from .forms import UserAuthenticationForm

from django.contrib.auth import login, logout


class LoginView(View):
    form_class = UserAuthenticationForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class()
        context ={
            'form' : form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home_page')
        context ={
            'form' : form,
        }
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('home_page')