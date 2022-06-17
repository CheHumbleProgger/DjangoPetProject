from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='all'),
    path('note/<int:pk>', views.NoteDetailView.as_view(), name='note_detail'),
    path('note/create', views.NoteCreateView.as_view(success_url=reverse_lazy('notes:all')), name='note_create'),
    path('note/<int:pk>/update', views.NoteUpdateView.as_view(success_url=reverse_lazy('notes:all')), name='note_update'),
    path('note/<int:pk>/delete', views.NoteDeleteView.as_view(success_url=reverse_lazy('notes:all')), name='note_delete'),
]
