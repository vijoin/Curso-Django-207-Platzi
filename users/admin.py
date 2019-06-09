from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from users.models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    #Mostrar los campos especificados
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture') 
    
    #Hacer clickables los campos especificados
    list_display_links = ('pk', 'user')
    
    #Editar los campos especificados desde la lista
    list_editable = ('phone_number', 'website', 'picture')

    #Buscar por múltiples campos
    search_fields = ('user__email',
                     'user__username',
                     'user__first_name',
                     'user__last_name',
                     'phone_number',
                     )

    #Agrega opciones de filtrado
    list_filter = ('created', 
        'modified', 
        'user__is_active', 
        'user__is_staff')

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
            }),
        ('Extra Info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
                )
            }),
        ('Metadata', {
            'fields': (('created', 'modified'),)
            })
        )

    readonly_fields = ('created', 'modified')

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
