from django.db.models import Q

from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .serializers import NoteSerializer, NoteSerializerShort

from notes import models
from notes.api import permissions


class NoteListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = models.Note.objects.all()
    serializer_class = NoteSerializerShort

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        qs = models.Note.objects.all()

        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(categories__name=category)

        author = self.request.query_params.get('author')
        if author:
            qs = qs.filter(author__name=author)
        return qs


class NoteRetrieveView(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = models.Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (permissions.IsAuthorOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get_serializer_class(self):
        if not self.request.user.is_authenticated:
            return NoteSerializerShort
        if self.get_object() in self.request.user.unlocks.all() or self.get_object().author == self.request.user:
            return NoteSerializer
        return NoteSerializerShort
