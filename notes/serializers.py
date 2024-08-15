from rest_framework import serializers
from .models import Note,Board

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id","body","colors","position","board"]
        extra_kwargs = {
            'board': {
                'write_only': True,
            },
        }


class BoardSerializer(serializers.ModelSerializer):
    notes = NotesSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = ['id','name','notes','user']
        extra_kwargs = {
            'user': {
                'read_only': True,
            },
        }





