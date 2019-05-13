from django.views.generic import ListView, DetailView


from .models import Post


class HomepageListView(ListView):
    model = Post
    template_name = 'home.html'


class HomepageDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
