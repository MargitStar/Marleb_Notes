from rest_framework import serializers
from note.models import Notes


class NoteSerializer(serializers.ModelSerializer):
    topic = serializers.CharField(max_length=80)
    note_text = serializers.CharField(max_length=1000, allow_blank=False)

    class Meta:
        model = Notes
        fields = ['topic', 'note_text']
