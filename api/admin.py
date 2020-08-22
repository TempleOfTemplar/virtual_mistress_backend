from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin

from .models import Suggestion, Item, Deviation


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
    prepopulated_fields = {'slug': ('title',)}


class DeviationAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover',)
    prepopulated_fields = {'slug': ('title',)}


class SuggestionAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    body = forms.CharField(label="Текст", widget=CKEditorUploadingWidget())

    class Meta:
        model = Suggestion
        fields = '__all__'


class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'cover')
    list_filter = ("categories", "toys")
    form = SuggestionAdminForm


admin.site.register(Item, ItemAdmin)
admin.site.register(Deviation, DeviationAdmin)
admin.site.register(Suggestion, SuggestionAdmin)
