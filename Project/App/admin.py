from django.contrib import admin
from .models import FeedbackMessage
# Register your models here.

@admin.register(FeedbackMessage)
class FeedbackMessage(admin.ModelAdmin):
    pass