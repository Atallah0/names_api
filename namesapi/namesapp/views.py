from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import NamesSerializer
from .models import Names

class NamesView(APIView):
    def get(self, request):
        names = Names.objects.all()
        serializer = NamesSerializer(names, many=True)
        return Response(serializer.data)

class AddName(APIView):
    def post(self, request):
        serializer = NamesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class Name(APIView):
    def get(self, request, id):
        try:
            name = Names.objects.get(id=id)
        except:
            return Response({
                'error': 'Name does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        serializer = NamesSerializer(name)
        return Response(serializer.data)

    def put(self, request, id):
        name = Names.objects.get(id=id)
        serializer = NamesSerializer(name, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        name = Names.objects.get(id=id)
        name.delete()
        return Response('Name deleted successfully')