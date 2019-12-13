from django.contrib import admin
from .models import PublicKey
from .domain import save_key


@admin.register(PublicKey)
class PublicKeyAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_active', 'created_date', 'updated_date']
    readonly_fields = ['is_active',]
    actions = ['toggle_active',]

    def toggle_active(self, request, queryset):
        for key in queryset:
            if key.is_active:
                key.is_active = False
            else:
                key.is_active = True
            key.save()
        save_key()

