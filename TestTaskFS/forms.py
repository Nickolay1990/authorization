from django import forms
import re


class LoginForm(forms.Form):
    name = forms.CharField(min_length=4,
                           widget=forms.TextInput(attrs={'placeholder': 'min 4 symbols and without space'}),
                           label='Login')
    password = forms.CharField(min_length=4,
                               widget=forms.PasswordInput(attrs={'placeholder': 'min 4 symbols and without space'}),
                               label='Password')

    def check_valid(self):
        self.check_valid_name()
        self.check_valid_password()

    def check_valid_name(self):
        check_slash = self.data['name'].replace('_', '')
        if len(self.data['name']) >= 4 and check_slash.isalnum():
            return True
        self.add_error('name', 'Login is invalid. Login must contain minimum 4 only letters or numbers.')

    def check_valid_password(self):
        check_slash = self.data['password'].replace('_', '')
        if len(self.data['password']) >= 4 and check_slash.isalnum():
            return True
        self.add_error('password', 'Password is invalid. Password must contain minimum 4 only letters or numbers.')


class RegisterForm(forms.Form):
    name = forms.CharField(label='Login',
                           widget=forms.TextInput(attrs={'placeholder': 'min 4 symbols and without space'}),
                           min_length=4)
    email = forms.EmailField(label='Email', widget=forms.EmailInput())
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'min 4 symbols and without space'}),
                                min_length=4)
    password2 = forms.CharField(label='Confirm password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'min 4 symbols and without space'}),
                                min_length=4)

    def check_valid(self):
        self.check_valid_name()
        self.check_valid_email()
        self.check_valid_password()
        self.check_confirm_password()

    def check_valid_name(self):
        check_slash = self.data['name'].replace('_', '')
        if len(self.data['name']) >= 4 and check_slash.isalnum():
            return True
        self.add_error('name', 'Login is invalid. Login must contain minimum 4 only letters or numbers.')

    def check_valid_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, self.data['email']):
            return True
        self.add_error('email', 'Email is invalid')

    def check_valid_password(self):
        check_slash = self.data['name'].replace('_', '')
        if len(self.data['password1']) >= 4 and check_slash.isalnum():
            return True
        self.add_error('password2', 'Password is invalid. Password must contain minimum 4 only letters or numbers.')

    def check_confirm_password(self):
        if self.data['password1'] == self.data['password2']:
            return True
        self.add_error('password2', 'Passwords are not identical')
