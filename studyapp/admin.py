from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Lead  # Import Model

# Lead model ko admin panel me register karna
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'country', 'created_at')  # Admin panel me columns show honge
    search_fields = ('name', 'email', 'phone')  # Search functionality
    list_filter = ('country', 'created_at')  # Filter sidebar me ye fields aayengi
