from django.views.generic import ListView


from .models import Post


class HomepageListView(ListView):
    model = Post
    template_name = 'home.html'
