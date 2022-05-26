from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from app1.models import newUser
from django.views.decorators.csrf import csrf_protect 

# Create your views here.

def registration(request):
   if request.method=="POST":
      firstname = request.POST.get('firstname')
      lastname = request.POST.get('lastname')
      emailAddress = request.POST.get('email')
      dateOfBirth = request.POST.get('dob')
      city = request.POST.get('city')
      state = request.POST.get('state')
      zipcode = request.POST.get('zip')
      password = request.POST.get('password')
      confirmPassword = request.POST.get('confirmPassword')
      createPassword = ""
      if password == confirmPassword:
         createPassword = password
      data = newUser(firstname=firstname,lastname=lastname,emailAddress=emailAddress,dateOfBirth=dateOfBirth,city=city,state=state,zipcode=zipcode,createPassword=createPassword)
      data.save()   
   # template = loader.get_template('index.html')
   # return HttpResponse(template.render())
   return render(request,'index.html')


