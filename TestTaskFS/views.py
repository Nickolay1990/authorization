from django.shortcuts import render
from TestTaskFS.forms import LoginForm, RegisterForm
from TestTaskFS.models import UserModel


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.check_valid()
        if not form.errors:
            try:
                user = UserModel.objects.get(name=form.data['name'])
                if user.password == form.data['password']:
                    return success(request, 'login')
                form.add_error(None, 'Account was not found')
            except:
                form.add_error(None, 'Account was not found')
    else:
        form = LoginForm()
    return render(request, 'TestTaskFS/form_page.html',
                  context={'form': form, 'title': 'Login', 'url_form_name': 'login_page', 'link_name': 'Registration',
                           'url_link_name': 'register_page'})


def registration(request) -> object:
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        form.check_valid()
        if not form.errors:
            try:
                UserModel.objects.create(name=form.data['name'], password=form.data['password1'],
                                         email=form.data['email'])
                return success(request, 'registration')
            except:
                form.add_error(None,
                               'User with this login or email already exists. Try creating account with different data')
    else:
        form = RegisterForm()
    return render(request, 'TestTaskFS/form_page.html',
                  context={'form': form, 'title': 'Registration', 'url_form_name': 'register_page',
                           'link_name': 'Login',
                           'url_link_name': 'login_page'})


def success(request, form):
    return render(request, 'TestTaskFS/success.html',
                  context={'form': form, 'title': 'Success', 'url_login': 'login_page',
                           'url_register': 'register_page'})


def index(request):
    return render(request, 'TestTaskFS/base.html', context={'title': 'Index page'})
