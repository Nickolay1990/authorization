from django import forms
import re


class LoginForm(forms.Form):
    name = forms.CharField(max_length=16, min_length=8, widget=forms.TextInput, label='Login')
    password = forms.CharField(max_length=16, min_length=8, widget=forms.PasswordInput, label='Password')

    def check_valid(self):
        self.check_valid_name()
        self.check_valid_password()

    def check_valid_name(self):
        if 16 >= len(self.data['name']) >= 8 and self.data['name'].isalnum():
            return True
        self.add_error('name', 'Login is invalid. Login must contain 8 - 16 letters or numbers.')

    def check_valid_password(self):
        if 16 >= len(self.data['password']) >= 8:
            return True
        self.add_error('password', 'Password is invalid. Password must contain 8 - 16 characters.')


class RegisterForm(forms.Form):
    name = forms.CharField(label='Login', widget=forms.TextInput(), max_length=16, min_length=8)
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=16, min_length=8)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(), max_length=16, min_length=8)

    def check_valid(self):
        self.check_valid_name()
        self.check_valid_email()
        self.check_valid_password()
        self.check_confirm_password()

    def check_valid_name(self):
        if 16 >= len(self.data['name']) >= 8 and self.data['name'].isalnum():
            return True
        self.add_error('name', 'Login is invalid. Login must contain 8 - 16 letters or numbers.')

    def check_valid_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, self.data['email']):
            return True
        self.add_error('email', 'Email is invalid')

    def check_valid_password(self):
        if 16 >= len(self.data['password1']) >= 8:
            return True
        self.add_error('password2', 'Password is invalid. Password must contain 8 - 16 characters.')

    def check_confirm_password(self):
        if self.data['password1'] == self.data['password2']:
            return True
        self.add_error('password2', 'Passwords are not identical')
