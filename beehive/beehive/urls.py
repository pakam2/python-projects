"""beehive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hives.views import MainView, AddHiveView, HiveListView, HiveListDetailedView, AddDataDisplayHives, AddData, ShowListOfHives, ShowData, LoginView, SignUp, LogOutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', LogOutView.as_view(), name="logout"),
    url(r'^signup/', SignUp.as_view(), name="signup"),
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^main/$', MainView.as_view(), name="main"),
    url(r'^addHive/$', AddHiveView.as_view(), name="add-hive"),
    url(r'^hiveList/$', HiveListView.as_view(), name="hive-list"),
    url(r'^displayHives/$', AddDataDisplayHives.as_view(), name="display-hives"),
    url(r'^historicData/$', ShowListOfHives.as_view(), name="show-hive-list"),
    url(r'^historicData/(?P<num>(\d)+)/$', ShowData.as_view(), name="show-data"),
    url(r'^addHivesData/(?P<num>(\d)+)/$', AddData.as_view(), name="hive-data-add"),
    url(r'^detailed/(?P<num>(\d)+)/$', HiveListDetailedView.as_view(), name="detailed"),

]
