from rest_framework import viewsets
from .serializers import *
from rest_framework.filters import SearchFilter
from .permissions import *

class DocumentModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUserOrReadOnly, FilterObjectPermission]
    serializer_class = DocumentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def get_queryset(self):

        try:
            group = self.request.user.groups.all()[0].name
        except IndexError:
            return Document.objects.filter(document_root='Public', status='Active')

        if group == 'user':
            doc = Document.objects.filter(document_root__in=['Public'], status='Active')
            return doc
        if group == 'sergeant':
            doc = Document.objects.filter(document_root__in=['Public', 'Private'], status='Active')
            return doc
        if group == 'general':
            doc = Document.objects.filter(document_root__in=['Public', 'Private', 'Secret'], status='Active')
            return doc
        if group == 'president':
            doc = Document.objects.all()
            return doc
