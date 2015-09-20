# Create your views here.
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.status import is_success
from rest_framework.views import APIView
from models import User
from rest_framework.response import Response
from serializers import UserSerializers


class UserDetail(APIView):

    def get(self,request,format=None):
        #users = self.get_object(self,pk)
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data, content_type='application/json')
       # return Response(serializer.data, content_type='application/json', status =status.HTTP_400_BAD_REQUEST)


    def post(self,request,format=None):
        serializer = UserSerializers(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, content_type='application/json', status=status.HTTP_201_CREATED)
    	return Response(serializer.errors,  content_type='application/json',status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        users = self.get_object(pk)
        serializer = UserSerializers(users)
        return Response(serializer.data, content_type='application/json')

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)