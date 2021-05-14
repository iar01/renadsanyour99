from django.contrib import admin
from .models import *


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'Client_Name', 'Phone_number', 'Email', 'Time')


admin.site.register(ContactUs)
admin.site.register(portfolio)
admin.site.register(Package)
admin.site.register(Carousel)
admin.site.register(Service)
admin.site.register(Statistics)
admin.site.register(Review)
admin.site.register(SocialMedia)
admin.site.register(Reservation, ReservationAdmin)
