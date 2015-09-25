# Create your views here.
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.status import is_success
from rest_framework.views import APIView
from models import User, Places
from rest_framework.response import Response
from serializers import UserSerializers, PlacesSerializers


class UserList(APIView):
    def get(self, request, format=None):
        # users = self.get_object(self,pk)
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data, content_type='application/json')
        # return Response(serializer.data, content_type='application/json', status =status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self,email ):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        email = request.GET.get('email', False)
        users = self.get_object(email)
        serializer = UserSerializers(users)
        return Response(serializer.data, content_type='application/json')
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request,format=None):
        email = request.GET.get('email', False)
        user = self.get_object(email)
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,format=None):
        email = request.GET.get('email', False)
        user = self.get_object(email)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PlaceList(APIView):
    def get(self):
        places = Places.objects.all()
        serializer = PlacesSerializers(places, many=True)
        return Response(serializer.data, content_type='application/json')

    def post(self, request, format=None):
        serializer = PlacesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type='application/json', status=status.HTTP_201_CREATED)
        return Response(serializer.errors, content_type='application/json', status=status.HTTP_400_BAD_REQUEST)

class PlaceDetails(APIView):
    def get_object(self, email):
        try:
            return Places.objects.filter(email = email)
        except Places.DoesNotExist:
            raise Http404

    def get(self, request,format=None):
        email = request.GET.get('email', False)
        places = self.get_object(email)
        serializer = PlacesSerializers(places)
        if serializer.is_valid():
            return Response(serializer.data, content_type='application/json')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None):
        email = request.GET.get('email', False)
        places = self.get_object(email)
        serializer = PlacesSerializers(places, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,format=None):
        email = request.GET.get('email', False)
        place = self.get_object(email)
        place.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)