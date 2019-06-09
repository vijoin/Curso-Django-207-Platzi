from django.contrib import admin
from users.models import Profile


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
    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')
