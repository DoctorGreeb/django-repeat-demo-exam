from django.contrib import admin

# Register your models here.
from .models import Zayavka, Review, User

admin.site.site_header='Конференции РФ - Панель администратора'

admin.site.register(Zayavka)
admin.site.register(Review)
admin.site.register(User)