# django default imports
from django.contrib import admin

# django required package imports
from django.contrib.auth.admin import UserAdmin

# local imports
from auth_app.models import User

# create admin model here
class UserModelAdmin(UserAdmin):
    list_display = ('id', 'email', 'name', 'is_admin', 'is_staff', 'is_active',)
    
    readonly_fields = ('created_at', 'updated_at', 'last_login')
    
    fieldsets = (
        ("USER PROFILE DETAILS",
        {
            'fields': ('email', 'name', 'password',)
        }),
        ("PERMISSIONS",
         {
          'fields': ('is_admin', 'is_staff',)   
         }),
        ("Dates", 
         {
            "fields": ("last_login","created_at","updated_at",),
         }),
    )
    
    add_fieldset = (
        ("UPDATE CREDIENTIALS", 
         {
             'fields': ("email", "name", "password", "password2")
         }),
    )
    
    filter_horizontal = ()
    
    search_fields = ('email',)
    list_filter = ('email', 'is_admin',)
    ordering = ('email', 'id',)
        
# Register your models here.
admin.site.register(User, UserModelAdmin)
