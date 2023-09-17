from django.shortcuts import render, redirect
from .forms import SubscriberForm
# from twilio.rest import Client
from twilio.rest import Client
from django.conf import settings

# Create your views here.

def landing_page(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)

        if form.is_valid():
            form.save()
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message = client.messages.create(
                body = "Thank you for subscribing!",
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