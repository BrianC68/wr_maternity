from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ContactForm


def contact(request):
    if request.method == 'GET':
        form = ContactForm
    else:
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            message = f"Message from {name}:\n\n{message}"
            to_email = User.objects.get(id=2).email
            try:
                send_mail(subject, message, from_email, [to_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found!')
            return redirect('contact:success')
    return render(request, 'contact_form.html', {'form': form})

def success(request):
    # return HttpResponse('Thank you, your message has been delivered.')
    messages.add_message(request, messages.SUCCESS, 'Thank you, your message has been delivered.')
    return render(request, 'contact_form.html', {'form': ContactForm})
