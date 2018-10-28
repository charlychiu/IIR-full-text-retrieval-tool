from django.db import models


class Document(models.Model):
    checksum = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Content(models.Model):
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='contents')
    title = models.TextField()
    abstract = models.TextField()
    is_raw = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RawIndex(models.Model):
    word = models.CharField(max_length=255)
    contents = models.ManyToManyField(Content)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PorterIndex(models.Model):
    word = models.CharField(max_length=255)
    contents = models.ManyToManyField(Content)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RawIndexTwitter(models.Model):
    word = models.CharField(max_length=255)
    contents = models.ManyToManyField(Content)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PorterIndexTwitter(models.Model):
    word = models.CharField(max_length=255)
    contents = models.ManyToManyField(Content)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
