from django.shortcuts import render
from django.views.generic import CreateView

# Core imports
from .models import Contact
from .forms import ContactForm
from .service import send
from .tasks import send_spam_email


# Create your views here.
class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = "main/contact.html"

    def form_valid(self, form):
        print(f"Email: {form.instance.email}")  # Отладка email
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)
