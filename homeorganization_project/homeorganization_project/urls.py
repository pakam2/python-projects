"""homeorganization_project URL Configuration

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
from homeorganization.views import LoginView, MainSite, LogoutView, \
                                    ShoppingListView, AddExpense, AddRepeatable, \
                                    MonthlyStatistics, IncomeView, ChooseMonthlyStatistics, ToDoView




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view(), name="login-view"),
    url(r'^main/', MainSite.as_view(), name="main-view"),
    url(r'^logout/', LogoutView.as_view(), name="logout-view"),
    url(r'^shoppinglist/', ShoppingListView.as_view(), name="shoppinglist-view"),
    url(r'^addexpense/$', AddExpense.as_view()),
    url(r'^addincome/$', IncomeView.as_view()),
    url(r'^addrepeatable/$', AddRepeatable.as_view()),
    url(r'^monthlystatistics/$', MonthlyStatistics.as_view()),
    url(r'^choosemonthlystatistics/$', ChooseMonthlyStatistics.as_view()),
    url(r'^todo/$', ToDoView.as_view(), name='todo-view'),
]
