from django.contrib import admin
from clients.models import Client
from services.models import Plan, Subscription, Service


admin.site.register(Client)
admin.site.register(Plan)
admin.site.register(Service)
admin.site.register(Subscription)
