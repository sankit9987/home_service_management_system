from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(service_category)
admin.site.register(subcategory)
admin.site.register(service)
admin.site.register(Booking)
admin.site.register(Service_provider)
admin.site.register(Feedback)