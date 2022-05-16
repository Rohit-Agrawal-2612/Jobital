from django.http import HttpResponse
from django.shortcuts import redirect, render
from requests import request
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from myapp.models import job, registration,team,testimonial,contactUs,newsLetter
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
# Create your views here.

def signup(request):
    if request.method == 'POST':
        print(
            request.POST['firstname'],
            request.POST['lastname'],
            request.POST['username'],
            request.POST['email'],
            request.POST['password']
        )
        email = request.POST['email']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = make_password(request.POST['password'])
        flag1,flag2 = False,False
        try:
            User.objects.get(email=email)
        except:
            flag1 = True
        try:
            User.objects.get(username=username)
        except:
            flag2 = True
        if flag1 and flag2:
            user = User(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
            user.save()
            return redirect('signin')
        else:
            context = {
                'message':'User with that email or username already exists !!'
            }
            return render(request, 'index.html', context)
    return render(request,'index.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pswrd = request.POST['password']
        user = authenticate(username=uname,password=pswrd)
        if user:
            login(request, user)
            # return render(request, 'home.html')
            if 'next' in request.GET:
                return redirect(request.GET.get('next'))
            return redirect('home')
        else:
            context = {
                'message' : 'Invalid username or password !!'
            }
            return render(request, 'login.html', context)
    return render(request, 'login.html')

def home(request):
    jobs = job.objects.all()[0:3]
    testimonials = testimonial.objects.all()[0:6]
    for t in testimonials:
        t.stars = range(t.stars)
    context = {
        'jobs' : jobs,
        'testimonials' : testimonials
    }
    return render(request, 'home.html', context)

def aboutus(request):
    return render(request, 'about-us.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = contactUs(name=name,email=email,message=message)
        print(contact)
        contact.save()
        subject = 'welcome to Jobital'
        message = f'Hi {name}, \nWe have successfully received your message.\nWe will get back to you soon.\n\n\n\nThanks\nAdmin\nJobital.com.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('home')

    return render(request, 'contact.html')

def jobdetails(request,id):
    jobs = job.objects.get(id=id)
    context = {
        'job' : jobs
    }
    return render(request, 'job-details.html', context)

def joblisting(request):
    jobs = job.objects.all()
    context = {
        'jobs' : jobs
    }
    return render(request, 'job-listing.html', context)

def team(request):
    return render(request, 'team.html')

def terms(request):
    return render(request, 'terms.html')

def testimonials(request):
    testimonials = testimonial.objects.all()[0:6]
    context = {
        'testimonials' : testimonials
    }
    print(testimonials)
    return render(request, 'testimonials.html',context)

def jobs(request):
    return HttpResponse('working on it')

def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            newsLetter.objects.get(email=email)
        except:
            subscriber = newsLetter(email=email)
            subscriber.save()
        else:
            jobs = job.objects.all()[0:3]
            testimonials = testimonial.objects.all()[0:6]
            for t in testimonials:
                t.stars = range(t.stars)
            context = {
                'jobs' : jobs,
                'testimonials' : testimonials,
                'already_subscribed' : 'You are already suscribed to our newsletter.'
            }
            return render(request, 'home.html', context)
        subject = 'Newsletter subscription confirmation'
        message = f'Hi,\n\n\nYou are successfully subscribed to our newsletter.\nWe will get back to you soon.\n\n\n\nThanks\nAdmin\nJobital.com.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('home')
    return redirect('home')

@login_required(login_url='/signin')
def register(request,id):
    jobs = job.objects.get(id=id)
    context = {
        'job' : jobs
    }
    if request.method == 'POST' or request.method == 'FILES':
        if request.POST['button'] == 'submit':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            company_name = request.POST['company_name']
            open_to_relocate = request.POST['open_to_relocate']
            resume = request.FILES['resume']
            profile_picture = request.FILES['profile_picture']
            current_ctc = request.POST['current_ctc']
            notice_period = request.POST['notice_period']
            role = request.POST['role']
            area_code = request.POST['area_code']
            contact_number = request.POST['contact_number']
            work_mode_preference = request.POST['work_mode_preference']
            expected_ctc = request.POST['expected_ctc']
            user = request.user
            register = registration(
                first_name=first_name, last_name=last_name, company_name=company_name,open_to_relocate=open_to_relocate, 
                contact_number=contact_number, expected_ctc=expected_ctc,
                resume=resume, profile_picture=profile_picture, email=email,
                current_ctc=current_ctc,work_mode_preference=work_mode_preference,
                notice_period=notice_period, role=role, area_code=area_code, user=user
            )
            register.save()
            subject = 'Job Application Confirmation'
            message = f'Hi,\n\n\nWe have immense pleasure in informing that you have successfully applied in {company_name} for the role of {role}.\nWe will Keep updating you about your application status.\nBest of luck.\n\n\n\nThanks\nAdmin\nJobital.com.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('dashboard')
        return render(request, 'register.html', context)
    return render(request, 'register.html', context)

@login_required(login_url='/signin')
def dashboard(request):
    registrations = registration.objects.filter(user=request.user)
    for r in registrations:
        if r.status == 'under process':
            r.stage = 1
        else:
            r.stage = 0
    context = {
        'registerations' : registrations
    }
    return render(request, 'dashboard.html', context)

def signout(request):
    logout(request)
    return redirect('home')

def withdraw(request,id):
    record = registration.objects.get(id=id)
    record.delete()
    return redirect('dashboard')

def edit(request,id):
    registeration = registration.objects.get(id=id)
    context = {
        'registeration' : registeration
    }
    if request.method == 'POST' or request.method == 'FILES':
        if request.POST['button'] == 'submit':
            registeration.first_name = request.POST['first_name']
            registeration.last_name = request.POST['last_name']
            registeration.email = request.POST['email']
            registeration.company_name = request.POST['company_name']
            registeration.open_to_relocate = request.POST['open_to_relocate']
            registeration.resume = request.FILES['resume']
            registeration.profile_picture = request.FILES['profile_picture']
            registeration.current_ctc = request.POST['current_ctc']
            registeration.notice_period = request.POST['notice_period']
            registeration.role = request.POST['role']
            registeration.area_code = request.POST['area_code']
            registeration.contact_number = request.POST['contact_number']
            registeration.work_mode_preference = request.POST['work_mode_preference']
            registeration.expected_ctc = request.POST['expected_ctc']
            registeration.user = request.user
            registeration.save()
            return redirect('dashboard')
        return render(request, 'edit.html', context)
    return render(request, 'edit.html', context)

def careers(request):
    return render(request, 'careers.html')