from django.contrib import admin

# Register your models here.
from .models import Users,Topic,Opinion,Tag

admin.site.register(Users)
admin.site.register(Topic)
admin.site.register(Opinion)
admin.site.register(Tag)

