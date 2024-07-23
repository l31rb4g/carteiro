from django.db import models


class Message(models.Model):
    from_email = models.CharField(max_length=512)
    from_name = models.CharField(max_length=512, null=True)
    to = models.CharField(max_length=512)
    subject = models.CharField(max_length=512)
    read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class MessagePart(models.Model):
    message = models.ForeignKey(Message, on_delete=models.DO_NOTHING)
    content_type = models.CharField(max_length=128)
    content = models.TextField()

