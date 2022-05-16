from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('home', views.home, name='home'),
    path('jobdetails/<int:id>', views.jobdetails, name='jobdetails'),
    path('joblisting', views.joblisting, name='joblisting'),
    path('team', views.team, name='team'),
    path('terms', views.terms, name='terms'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('jobs', views.jobs, name='jobs'),
    path('signin', views.signin, name='signin'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('register/<int:id>', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('signout', views.signout, name='signout'),
    path('withdraw/<int:id>', views.withdraw, name='withdraw'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('careers', views.careers, name='careers')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)