from django.contrib import admin

from .models import Answer,UserAnswer,MyUser,Question

admin.site.register(Answer)
admin.site.register(UserAnswer)
admin.site.register(MyUser)
admin.site.register(Question)

