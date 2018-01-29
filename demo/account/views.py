from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from publicphotos.models import PublicPhotos

#this will show a page, asking to either login or register?
def index(request):
    return render(request, 'account/login.html')

def detail(request, username):
    try:
        account = User.objects.get(username=username)
        all_photos = PublicPhotos.objects.filter(username__username__icontains=username)
    except User.DoesNotExist:
        raise Http404("Nope")
    context = {
        'account':account,
        'all_photos':all_photos,
    }
    return render(request, 'account/detail.html', context)


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'account/login.html'
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('website:index')
            else:
                return ("Try again!")
        return render(request, self.template_name, {'form': form})

def logout_view(request):
    logout(request)
    return redirect('website:index')

def register(request):
    return render(request, 'account/register.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('website:index')

        return render(request, self.template_name, {'form': form})
