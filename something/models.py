from django.db import models

# Create your models here.

class Document(models.Model):
        name = models.CharField( max_length=64, blank=True, null=True, default=None)
        created = models.DateTimeField(auto_now_add=True, auto_now=False)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        urlDownload = models.CharField( max_length=36, blank=True, null=True, default=None)
        class Meta:
            verbose_name = 'документ'
            verbose_name_plural = 'документы'

class UploadFile(models.Model):
        upload  =  models.FileField()
        download = models.CharField( max_length=64, blank=True, null=True, default=None)
        created = models.DateTimeField(auto_now_add=True, auto_now=False)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        class Meta:
            verbose_name = 'загр. док'
            verbose_name_plural = 'загр. доки'

class Person(models.Model):
        file = models.ForeignKey('Document',null=True, related_name="file", on_delete=models.CASCADE)
        FIO = models.TextField( blank=True, null=True, default=None)
        created = models.DateTimeField(auto_now_add=True, auto_now=False)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        class Meta:
            verbose_name = 'человек'
            verbose_name_plural = 'люди'
