from django.shortcuts import render
from FormsApp import forms

# Create your views here.

def index(request):
    return render(request,'FormsApp/index.html')


def form_name_view(request):
    form = forms.SupportTicketForm()
    if request.method=='POST':
        form = forms.SupportTicketForm(request.POST)

        if form.is_valid():
            print("Validation Successful!")
            print('Name:'+form.cleaned_data['name'])
            print('Email:'+form.cleaned_data['email'])
            print('Text:'+form.cleaned_data['text'])
            print("Category:", form.cleaned_data.get('category'))

        # Optional: reset form after success
            form = forms.SupportTicketForm()
    return render(request,'FormsApp/form_page.html',{'form':form})

