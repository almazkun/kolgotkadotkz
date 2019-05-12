from django.urls import path


from .views import HomepageListView


urlrpatterns = [
    path('', HomepageListView.as_view(), name='home')
]