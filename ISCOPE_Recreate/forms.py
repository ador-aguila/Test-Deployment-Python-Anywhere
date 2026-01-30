

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from django.forms import ModelForm
from .models import *


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={
        'class':'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500',
        'placeholder':'Username'}))
    first_name = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={
        'class':'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500',
        'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=40, widget=forms.TextInput(attrs={
        'class':'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500',
        'placeholder':'Last Name'}))

    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500'
    }))
    
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500'
    }))
    
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500'
    }))

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm,self).__init__(*args,**kwargs)




class StudentForm(ModelForm):
    name = forms.CharField(label="Name", max_length=40, widget=forms.TextInput(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500','placeholder':'Full Name'}))
    email = forms.CharField(label="Email", max_length=40, widget=forms.TextInput(attrs={'class':'w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500','placeholder':'Email'}))
    profile_pic = forms.ImageField(
        label="Profile Pic",
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-purple-500 text-gray-700 bg-[#FFF1D5] file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-purple-50 file:text-purple-700 hover:file:bg-purple-100',
        })
    )

    class Meta:
        model = Student
        fields = ('name','email','profile_pic',)
        exclude = ['user']
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' '
            field.label_suffix = ""

               
        self.fields['profile_pic'].widget.initial_text = 'Currently uploaded'
        self.fields['profile_pic'].widget.input_text = 'Change'
