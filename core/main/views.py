from django.shortcuts import render
from django.views.generics import CreateView

# Core imports
from .models import Contact
from .forms import ContactForm


# Create your views here.
class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = "main/contact.html"

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)
