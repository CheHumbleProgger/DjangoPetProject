from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from notes.models import Note
from django.urls import reverse_lazy


class NoteListView(LoginRequiredMixin, ListView):
    model = Note

    def get_queryset(self):
        qs = super(NoteListView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class NoteDetailView(LoginRequiredMixin, DetailView):
    model = Note

    def get_queryset(self):
        qs = super(NoteDetailView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'text']
    success_url = reverse_lazy('notes:all')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.save()
        return super(NoteCreateView, self).form_valid(form)


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'text']
    success_url = reverse_lazy('notes:all')

    def get_queryset(self):
        qs = super(NoteUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    model = Note

    def get_queryset(self):
        qs = super(NoteDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)