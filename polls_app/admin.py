from django.contrib import admin
from polls_app.models import *

# Register your models here.

admin.site.register(Question)
admin.site.register(Choices)
