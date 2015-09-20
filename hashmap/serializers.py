__author__ = 'rishabh'
from models import User, Places

from rest_framework import serializers

class UserSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=False,default=None)
    number = serializers.IntegerField(required=False,default=None)
    latitude = serializers.DecimalField(max_digits=51, decimal_places=2)
    longitude = serializers.DecimalField(max_digits=15, decimal_places=2)
    address = serializers.CharField(required=False,default='null')
    #tags = serializers.CharField(required=False)

    class Meta:
        model = User
        fields =('id','user_id','name','number','imei','email','latitude','longitude','address','tags')

    def create(self,validated_data):

         return User.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.email = validated_data.get('email',instance.email)
        instance.number = validated_data.get('number',instance.number)
        instance.name = validated_data.get('name',instance.name)
        instance.latitude = validated_data.get('latitude',instance.latitude)
        instance.longitude = validated_data.get('longitude',instance.longitude)
        instance.address = validated_data.get('address',instance.address)
        instance.save()
        return instance

class PlacesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = ('id','user_id','latitude','longitude','address','name','number','category','description',
                  'website','tag','place_id')

    def create(self,validated_data):

         return Places.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.number = validated_data.get('number',instance.number)
        instance.address = validated_data.get('address',instance.address)
        instance.latitude = validated_data.get('latitude',instance.latitude)
        instance.longitude = validated_data.get('longitude',instance.longitude)
        instance.category = validated_data.get('category',instance.category)
        instance.description = validated_data.get('description',instance.description)
        instance.website = validated_data.get('website',instance.website)
        instance.tag= validated_data.get('tag',instance.tag)
        instance.place_id = validated_data.get('place_id',instance.place_id)
        instance.save()
        return instance
