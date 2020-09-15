from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.core.mail import BadHeaderError, send_mail,EmailMessage
import smtplib
from django.contrib import messages  
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
 


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
#from datetime import datetime
import datetime
from django.utils import timezone

from django.template import RequestContext
#@login_required
#def index(request):
    #return render(request,'index.html')

#def lousy_logout(request):
    #...
def login(request):  

    if request.user.is_authenticated():
        return redirect('admin_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'main/registration/login.html')



def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'index.html')
    context['form']=form
    return render(request,'main/password/sign_up.html',context)
    
# Create your views here.

#def homepage(request):
	#return render (request=request, template_name="home.html")

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:

						return HttpResponse('Invalid header found.')
					#return redirect ("/password_reset/done/")
	
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("/password_reset/done/")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})

def home(request):
    brands = Brand.objects.all()
    photogallery = Photo.objects.all()
    web = Web.objects.all()
    prints = Print.objects.all()    
    aboutus = AboutMe.objects.all()
    skill = Skills.objects.all()
    services = Service.objects.all()     
    summary = Summary.objects.all()
    experience = Experience.objects.all()
    education = Education.objects.all()
    contact = Contact.objects.all()
    more= EexperienceMore.objects.all()
    links = Socialiconlink.objects.all()
    customer=HappyCustomer.objects.all()  
    testimonial=Testimonial.objects.all()
    intrest=Intrest.objects.all()   
    
    
    #myDate = datetime.now()
     
    # Give a format to the date
    # Displays something like: Aug. 27, 2017, 2:57 p.m.
    #formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
    d=timezone.now() 
    context = {'date':d,'intrest':intrest,'testimonial':testimonial,'customer':customer,'links': links,'brands':brands,'web':web,'skill':skill,'services':services,'summary':summary,'experience':experience,'education':education,'contact':contact,'photogallery':photogallery,'prints':prints,'aboutus':aboutus}
    return render(request, "index.html", context)

 

def portfolioprintview(request):
    prints = Print.objects.all()
    context = {'prints':prints}
    return render(request,'portfolio-details.html',context)

def filter(request):   
    d=datetime.datetime.now()
    context = {'date':d}
    return render(request, "portfolio-details.html", context)
 
def contact(request):
    
    if request.method == "POST":
        #if form.is_valid():
            #form.save()
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_mobile = request.POST['message-mobile']
        message_subject = request.POST['message-subject']
        message = request.POST['message']
        # file_field = request.POST['file-field']
        appoint = "Name :" + message_name + " \n Mobile :" + message_mobile + \
            " \n Subject :" + message_subject + " \n Message :" + message
        # send email
        send_mail(
            'Appoinment Request',  # subject
            appoint,  # message

            'jose06aj@gmail.com',
            ['jose06aj@gmail.com'],  # from_email
            fail_silently=False,

        )

        return render(request, "thank_you.html", {'message_name': message_name, 'message_email': message_email, 'message_mobile': message_mobile, 'message_subject': message_subject, })
    else:

        return render(request, "thank_you.html")

 

 
def error_404_view(request, exception):
    return render(request,'404.html')
def handler500(request):
    return render(request, '500.html', status=500)