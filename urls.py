from django.conf.urls import url, include
from .views import *
urlpatterns = [
    # url(r'^$', homePageView, name="home-page"),
    url(r'^$', registerPhase1, name='user_api_registration'),
    # url(r'^register-phase2/', registerPhase2, name='register-phase2')
     url(r'^create_user/$', CustomRegistrationView.as_view(), name='register_user'),
    url(r'^step2/$', registerPhase2, name='register-phase2'),
]