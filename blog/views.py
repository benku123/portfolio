from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email  = form.cleaned_data["email"]
            message  = form.cleaned_data["message"]
            send_mail('The contact form subject',
                      message + name,
                      "youremail@gmail.com", [email], fail_silently=False )
            return redirect("home")
    context = Portfolio.objects.all()
    return render(request, "index.html", {"portfolios": context, "form": form})