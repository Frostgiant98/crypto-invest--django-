from django.contrib import admin
from .models import deposits_table, withdrawal_table, wallet_table, notifications_table, history_table
# Register your models here.

@admin.register(deposits_table)
class depositsAdmin(admin.ModelAdmin):
    pass

@admin.register(withdrawal_table)
class depositsAdmin(admin.ModelAdmin):
    pass

@admin.register(wallet_table)
class depositsAdmin(admin.ModelAdmin):
    pass

@admin.register(notifications_table)
class depositsAdmin(admin.ModelAdmin):
    pass

@admin.register(history_table)
class depositsAdmin(admin.ModelAdmin):
    pass

