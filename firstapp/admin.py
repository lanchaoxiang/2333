from django.contrib import admin

# Register your models here.
from firstapp.models import *

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tickets)
admin.site.register(Comment_New)
admin.site.register(UserProfile)
admin.site.register(Buy)
admin.site.register(InstationMessage)