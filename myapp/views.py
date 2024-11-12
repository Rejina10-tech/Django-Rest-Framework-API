from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def sample_request_view(request):
    if request.method == 'GET':
        # Handle GET request
        query_param = request.query_params.get('query', 'default')
        return Response({"method": "GET", "query": query_param})
    elif request.method == 'POST':
        # Handle POST request
        data = request.data.get('data')
        user = request.user if request.user.is_authenticated else 'Anonymous'
        return Response({"method": "POST", "user": user, "data": data})
    
    
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]