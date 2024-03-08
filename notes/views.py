from django.shortcuts import render

from .forms import NoteForm
from .models import Note
from django.http import Http404, HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView
)


class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/notes_form.html'
    success_url = '/smart/notes'


class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()


class NoteDetailView(DetailView):
    model = Note
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    success_url = '/smart/notes'
    template_name = 'notes/notes_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
