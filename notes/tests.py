from django.test import TestCase, Client
from notes.models import Note
from django.contrib.auth.models import User
from django.urls import reverse


class NoteTest(TestCase):

    def create_user(self, username='Tester', password='Tester'):
        return User.objects.create_user(username=username, password=password)

    def create_note(self, title='NoteTest test title', text='This is a NoteTest test Note'):
        return Note.objects.create(title=title, text=text, owner=self.create_user())

    def test_note_creation(self):
        note = self.create_note()
        self.assertTrue(isinstance(note, Note))
        self.assertEqual('NoteTest test title', note.title)

    def test_note_detail_view(self):
        note = self.create_note()
        self.client.login(username='Tester', password='Tester')
        url = reverse('notes:note_detail', args=[note.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(note.title.encode(), resp.content)
        self.assertIn(note.text.encode(), resp.content)

    def test_users_division(self):
        note = self.create_note()
        self.create_user(username='Tester2', password='Tester2')
        self.client.login(username='Tester2', password='Tester2')
        url = reverse('notes:note_detail', args=[note.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
