# from mptt.admin import DraggableMPTTAdmin
from heriarchical_data.models import File
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from heriarchical_data.forms import LoginForm, CreateFile
from django.contrib.auth.models import User
from django.views import View
from django.views.generic.edit import CreateView


@login_required
def homeview(request):
    html = 'index.html'
    data = File.objects.all()
    fileuser = User.objects.all()
    return render(request, html, {'data': data, 'fileuser': fileuser})


def loginview(request):
    html = 'login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, html, {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


class ViewProfile(View):
    def get(self, request, id):
        html = 'profile.html'
        fileuser = User.objects.filter(id=id).first()
        data = File.objects.filter(user=fileuser)
        return render(request, html, {
            'data': data, 'fileuser': fileuser})


class FileCreateView(CreateView):
    html = 'createfile.html'

    def get(self, request):
        form = CreateFile()
        return render(request, self.html, {'form': form})

    def post(self, request):
        form = CreateFile(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            File.objects.create(
                name=data['name'],
                user=request.user
            )
            return HttpResponseRedirect(reverse('homepage'))
        form = CreateFile()
        return render(request, self.html, {'form': form})
