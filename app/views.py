from django.shortcuts import render, redirect
from django.core.mail import send_mail , EmailMessage
from company import settings
from django.contrib import messages
from django.template.loader import render_to_string
# Create your views here.

def Homepage(request):
    return render(request, 'app/index.html' )

def Email_Send(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        to_email =["akinwumikaliyanu@gmail.com"]
        template = render_to_string('app/email_template.html',{'name':name, 'contact':email , 'message':message})
        send_mail(subject, template , 'akinwumikaliyanu@gmail.com' ,to_email ,  fail_silently=False,)
        messages.success(request, "Email Successfully Sent")
        return redirect('home')
    else:
        None

