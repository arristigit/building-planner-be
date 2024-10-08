from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Drawing
from .serializers import DrawingSerializer

class DrawingListCreateView(APIView):
    def get(self, request):
        drawings = Drawing.objects.all()
        serializer = DrawingSerializer(drawings, many=True)
        return Response(serializer.data)

    def post(self, request):
        title = request.data.get('title', 'Untitled Drawing')
        data = request.data.get('data', {})
        serializer = DrawingSerializer(data={'title': title, 'data': data})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DrawingRetrieveView(APIView):
    def get(self, request, pk):
        try:
            drawing = Drawing.objects.get(pk=pk)
        except Drawing.DoesNotExist:
            return Response({'error': 'Drawing not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DrawingSerializer(drawing)
        return Response(serializer.data)
