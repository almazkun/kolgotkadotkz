from django.urls import path


from .views import HomepageListView, HomepageDetailView


urlpatterns = [
    path('post/<int:pk>/', HomepageDetailView.as_view(), name='post_detail'),
    path('', HomepageListView.as_view(), name='home'),
]