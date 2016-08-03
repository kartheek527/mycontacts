from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from connection import models
from django.forms import ModelForm


class ContactForm(ModelForm):
    class Meta:
        model = models.Contact
        fields = ['first_name', 'last_name', 'iban']


@login_required(login_url='/')
def home(request, template_name='home.html'):
    """This view is to access the list of contacts user created.

    Args:
        request : HttpRequest Object
        template_name : Template to render or dispay data.
    Returns:
        HttpResponse: Render the respose to template as contacts data as context.
    """
    contacts = models.Contact.objects.filter(admin = request.user.id)
    data = {}
    data['contacts'] = contacts
    return render(request, template_name, data)


@login_required(login_url='/')
def save_contact(request, template_name='add_contact.html'):
    """This is common view for GET/POST request.
    
    If request is POST, it validate and save data in Contact table
    else it will render the form to create new contact.

    Args:
        request : HttpRequest Object
        template_name : Template to render or dispay data.
    Returns:
        HttpResponse: Redirects to contacts list after saving data otherwise
        render the respose to template with contact form as context.
    """
    form = ContactForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.admin = User.objects.get(email = request.user.email)
        obj.save()

        return redirect('contact_list')
    return render(request, template_name, {'form':form})


def update_contact(request, pk, template_name='add_contact.html'):
    """This is common view for GET/POST request.
    
    If request is POST, it validate and updates the Contact datails
    else it will render the form to update selected contact.

    Args:
        request : HttpRequest Object
        template_name : Template to render or dispay data.
    Returns:
        HttpResponse: Redirects to contacts list page updating details otherwise
        render the respose to template with contact form as context.
    """
    contact = get_object_or_404(models.Contact, pk=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('contact_list')
    return render(request, template_name, {'form':form})


def delete_contact(request, pk, template_name='delete.html'):
    """This is common view for GET/POST request.
    
    If request is POST, it will delete contact datails on user request
    else it will render the form to delete selected contact.

    Args:
        request : HttpRequest Object
        template_name : Template to render or dispay data.
    Returns:
        HttpResponse: Redirects to contacts list page updating details otherwise
        render the respose to template with contact form as context.
    """
    contact = get_object_or_404(models.Contact, pk=pk)    
    if request.method=='POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, template_name, {'object':contact})
