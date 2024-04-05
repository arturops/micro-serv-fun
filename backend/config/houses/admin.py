from django.contrib import admin

from .models import Checker
from .models import House

# Register your models here.
admin.site.register(Checker)
admin.site.register(House)
