from django.contrib import admin

from .models import ProjectType, Project, EntryType, Entry, UserInfo

admin.site.register(ProjectType)
admin.site.register(Project)
admin.site.register(EntryType)
admin.site.register(Entry)
admin.site.register(UserInfo)
