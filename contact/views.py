from django.shortcuts import render, get_object_or_404, redirect
from contact.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.
def contact_view(request):
    context = {}
    if request.method == 'GET':
        form = ContactForm()

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            phone_number = form.cleaned_data['phone_number']
            subject = form.cleaned_data['subject']
            message    = form.cleaned_data['message']
            try:
                full = message 
                send_mail(
                    name,
                    full,
                    from_email,
                    ['shopeyinwale@gmail.com']
                )
                print(subject,from_email,message,phone_number,name)
                context['success_message'] = 'Your message has been sent.You will receive a reply ASAP'
                form = ContactForm()

            except BadHeaderError:
                return HttpResponse('Invalid Header found')
    return render(request, 'contact/contact.html', {})


    