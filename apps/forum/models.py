from django.db import models


class ForumMessage(models.Model):
    content = models.CharField(max_length=256)
    sender_id = models.ForeignKey(
        'users.User', on_delete=models.PROTECT
    )
    creation_date = models.DateTimeField(auto_now=True)
