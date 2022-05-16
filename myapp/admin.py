from django.contrib import admin
from myapp.models import job,team,testimonial,contactUs,newsLetter,registration

# Register your models here.
admin.site.register(job)
admin.site.register(team)
admin.site.register(testimonial)
admin.site.register(contactUs)
admin.site.register(newsLetter)
admin.site.register(registration)