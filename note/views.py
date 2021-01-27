from rest_framework import viewsets
from note.models import Notes
from note.serializer import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
