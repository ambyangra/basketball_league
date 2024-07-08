from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Player
from ..serializers import PlayerSerializer

class PlayerView(APIView):

    def get(self, request):
        """
        Retrieves the details of the current player.
        """
        player = Player.objects.get(name='player 01') #name=request.user
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def put(self, request):
        """
        Updates the details of the current player.
        """
        player = Player.objects.get(user=request.user)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class CreatePlayerView(APIView):    
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)