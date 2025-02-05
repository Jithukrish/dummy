from django.contrib import admin
from .models import User,Skill,jobseeker_Profile,Profile
from Company.models import Company
from Resume.models import Resume
from Job.models import Apply_Job, Skills_job,Education,JobPost
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()
@admin.action(description='Block selected users')
def block_users(modeladmin, request, queryset):
    updated = queryset.update(is_blocked=True)
    messages.success(request, f'{updated} users were successfully blocked.')

@admin.action(description='Unblock selected users')
def unblock_users(modeladmin, request, queryset):
    updated = queryset.update(is_blocked=False)
    messages.success(request, f'{updated} users were successfully unblocked.')

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('is_employer', 'is_jobseeker', 'has_resume', 'has_company', 'is_verified', 'verification_token', 'is_blocked')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email'),
        }),
    )
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser', 'is_blocked')
    search_fields = ('username', 'email')
    ordering = ('username',)
    actions = [block_users, unblock_users]

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(jobseeker_Profile)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Skills_job)
admin.site.register(JobPost)
admin.site.register(Apply_Job)