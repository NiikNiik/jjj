from django.shortcuts import render, redirect
from .forms import SubscriberForm
import os
# from twilio.rest import Client
from twilio.rest import Client
from django.conf import settings

# Create your views here.
twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

def landing_page(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)

        if form.is_valid():
            form.save()
            client = Client(settings.TWILIO_ACCOUNT_SID, twilio_auth_token)
            message = client.messages.create(
                body = "Thank you for subscribing! \U0001F680",
                from_ = settings.TWILIO_PHONE_NUMBER,
                to = form.cleaned_data['phone_number'] 
            )
            print(message.sid)
            return redirect("/vibes/")
        else:
            return redirect("/vibes/")
    else:
        form = SubscriberForm()
    context = {'form':form}
    return render(request, 'index.html', context)