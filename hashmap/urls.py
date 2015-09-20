__author__ = 'rishabh'
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url
from views import UserList,UserDetail


urlpatterns = [
    url(r'^user/$',UserDetail.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$',UserList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
