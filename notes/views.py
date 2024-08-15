from django.shortcuts import render
from .serializers import NotesSerializer,BoardSerializer
from .models import Note,Board
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser
)
# Create your views here.


class NoteViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NotesSerializer

    def list(self,request:Request):
        try:
            notes = Note.objects.all()
            serializer = self.serializer_class(instance=notes, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self,request:Request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(str(e))
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self,request:Request,pk=None):
        try:
            note = Note.objects.get(pk=pk,board__user = request.user)
            serializer = self.serializer_class(note)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(data={'error':'Not Found'}, status=status.HTTP_404_NOT_FOUND)


    def update(self,request:Request,pk=None):
        try:
            note = Note.objects.get(pk=pk,board__user = request.user)
            serializer = self.serializer_class(data=request.data,instance=note)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request: Request, pk=None):
        try:
            note = Note.objects.get(pk=pk,board__user = request.user)
            serializer = self.serializer_class(data=request.data, instance=note,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self,request:Request,pk=None):
        try:
            note = Note.objects.get(pk=pk,board__user = request.user)
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(data={'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)


class BoardViewSet(viewsets.ViewSet):
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    def list(self,request:Request):
        try:
            boards = Board.objects.filter(user=request.user)
            serializer = self.serializer_class(instance=boards, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def create(self,request:Request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(data=serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data={'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def retrieve(self,request:Request,pk=None):
        try:
            board = Board.objects.get(pk=pk,user=request.user)
            serializer = self.serializer_class(board)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(data={'error':'Not Found'}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self,request:Request,pk=None):
        try:
            board = Board.objects.get(pk=pk,user=request.user)
            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response(data={'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)