from django.urls import path
from .views import NoteViewSet,BoardViewSet


board_create = BoardViewSet.as_view({'post': 'create'})
board_list = BoardViewSet.as_view({'get': 'list'})
board_detail = BoardViewSet.as_view({'get': 'retrieve'})
board_delete = BoardViewSet.as_view({'delete': 'destroy'})

note_create = NoteViewSet.as_view({'post': 'create'})
note_list = NoteViewSet.as_view({'get': 'list'})
note_detail = NoteViewSet.as_view({'get': 'retrieve'})
note_update = NoteViewSet.as_view({'put': 'update'})
note_partial_update = NoteViewSet.as_view({'patch': 'partial_update'})
note_delete = NoteViewSet.as_view({'delete': 'destroy'})

urlpatterns = [
    path('boards/create/', board_create, name='board-create'),
    path('boards/list/', board_list, name='board-list'),
    path('boards/detail/<uuid:pk>/', board_detail, name='board-detail'),
    path('boards/delete/<uuid:pk>/', board_delete, name='board-delete'),

    path('notes/create/',note_create,name='note-create'),
    path('notes/list/',note_list,name='note-list'),
    path('notes/detail/<uuid:pk>/',note_detail,name='note-detail'),
    path('notes/update/<uuid:pk>/',note_update,name='note-update'),
    path('notes/partial_update/<uuid:pk>/',note_partial_update,name='note-partial-update'),
    path('notes/delete/<uuid:pk>/',note_delete,name='note-delete'),
]
