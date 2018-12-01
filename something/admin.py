from django.contrib import admin
from .models import Document
from .models import Person, UploadFile

class PersonAdmin(admin.ModelAdmin):
    class Meta:
        model = Person

admin.site.register(Person, PersonAdmin)

class DocumentAdmin(admin.ModelAdmin):
    class Meta:
        model = Document

admin.site.register(Document, DocumentAdmin)

class UploadFileAdmin(admin.ModelAdmin):
    class Meta:
        model = UploadFile

admin.site.register(UploadFile, UploadFileAdmin)
