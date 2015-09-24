__author__ = 'rishabh'
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from views import UserList,UserDetail, PlaceDetails, PlaceList

urlpatterns = [
    url(r'^api/v1/user/$',UserDetail.as_view()),
    url(r'^api/v1/user/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z])/$',UserList.as_view()),
    url(r'^api/v1/place/$',PlaceDetails.as_view()),
    url(r'^api/v1/place/(?P<pk>[0-9])/$',PlaceList.as_view()),


]
urlpatterns = format_suffix_patterns(urlpatterns)
