from django.contrib import admin

# Register your models here.
from akinwunmi_nathanielscrumy.models import ScrumyGoals, ScrumyHistory, GoalStatus, Post, Comment


admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
admin.site.register(GoalStatus)
admin.site.register(Post)
admin.site.register(Comment)