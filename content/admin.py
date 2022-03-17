from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(User)
admin.site.register(UserProfile)