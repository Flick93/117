from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def test_view(request):
    return render(request, "pages/test.html")

def about_view(request):
    return render(request, "pages/about.html")

def contact_view(request):
    if request.method == "POST":
        #send the message
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Sending email")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data["message"]

            full_message = f"This is an email from your portfoliopage\nName:{name}\nEmail:{email}\nMessage:{message}"

            send_mail(
                "Email from" + name,
                full_message,
                email,
                ['Paul.Afflick@sdgku.edu']
            )
            
            print("Email sennt")

            #send the user to thank you page

        else:
            print("Invalid data on the form")
    else:
        # display page
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})