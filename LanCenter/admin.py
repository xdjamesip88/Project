from django.contrib import admin

from .models import cuenta, producto, stockdetalle, UserProfile

# Register your models here.

class stockdetalleInline(admin.TabularInline):
    model = stockdetalle

class cuentaAdmin(admin.ModelAdmin):
    inlines = (stockdetalleInline,)

admin.site.register(stockdetalle)
admin.site.register(producto)

admin.site.register(UserProfile)
admin.site.register(cuenta,cuentaAdmin)
