from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class DossierModelViewSet(APIView):

    def get(self, request, *args, **kwargs):
        try:
            dossier = Dossier.objects.get(user=request.user)
        except Dossier.DoesNotExist:
            return Response({"data": "Dossier doesnt exist!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DossierSerializer(dossier)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):

        dossier = Dossier.objects.get(user=request.user)
        serializer = DossierSerializer(dossier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, *args, **kwargs):
        dossier = Dossier.objects.get(user=request.user)
        dossier.delete()
        return Response({"data": "Delete successful!"})


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
