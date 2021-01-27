from django.db import models


class Notes(models.Model):
    topic = models.CharField(
        "Topic",
        max_length=80,
    )
    note_text = models.TextField(
        "Note",
        max_length=1000,
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.topic.title()
