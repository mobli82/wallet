from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.

admin.site.register(Profile)

class UserAdminSite(admin.ModelAdmin):
    list_display = ['username','email' ,'first_name', 'last_name']
    # fieldsets = [
    #     (None,               {'fields': ['username', 'email']}),
    # ]
    

# admin.site.unregister(User)
# admin.site.register(User, UserAdminSite)

# def show_name(modeladmin, request, queryset):
#     for user in queryset:
#         user.first_name = "nick"
#         user.save()

# show_name.short_description = "show name"

# class UserNameAndSurname(admin.ModelAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     search_fields = ('username', 'first_name', 'last_name', 'email')
#     ordering = ('username',)
#     actions = [show_name]

# admin.site.register(User, UserNameAndSurname)