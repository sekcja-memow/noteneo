from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        ordering = ('name',)


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)

    categories = models.ManyToManyField('Category', related_name='notes', blank=True)
    bookmarks = models.ManyToManyField('users.User', related_name='bookmarks', blank=True)
    likes = models.ManyToManyField('users.User', related_name='likes', blank=True)

    class Meta:
        ordering = ('title',)

    def like(self, user: User):
        self.likes.add(user)

    def bookmark(self, user: User):
        self.bookmarks.add(user)

    def categorize(self, category: Category):
        self.categories.add(category)

