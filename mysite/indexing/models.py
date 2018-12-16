from django.db import models


# Create your models here.

class Document(models.Model):
    title = models.TextField()
    abstract = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BSBI(models.Model):
    word = models.CharField(max_length=255)
    documents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BSBI_Map(models.Model):
    hash = models.CharField(max_length=255)
    word = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BSBI_Merge(models.Model):
    word = models.CharField(max_length=255)
    documents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SPIMI(models.Model):
    word = models.CharField(max_length=255)
    documents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
