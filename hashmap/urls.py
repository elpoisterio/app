__author__ = 'rishabh'
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from views import UserList,UserDetail, PlaceDetails, PlaceList

urlpatterns = [
    url(r'^api/v1/user/$',UserList.as_view()),
    url(r'^api/v1/user/details/$',UserDetail.as_view()),
    url(r'^api/v1/place/$',PlaceList.as_view()),
    url(r'^api/v1/place/details/$',PlaceDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
