from django.conf.urls import url,include
from django.views.generic import ListView,DetailView
from .models import Post
from . import views

from django.contrib.syndication.views import Feed

class BlogFeed(Feed):
    title="Mysite"
    description='My writings'
    link='/blog/feed/'

    def items(self):
        return Post.objects.all().order_by('-created')
    def item_title(self,item):
        return item.title
    def item_description(self, item):
        return item.body
    def item_link(self, item):
        return u'/blog/%d' % item.id

urlpatterns = [
    url(r'^$',ListView.as_view(
        queryset = Post.objects.all().order_by("-created"),
        template_name = 'blog.html'
    )),

    url(r'^(?P<pk>[0-9]+)/$',DetailView.as_view(
        model = Post,
        template_name = 'post.html'
    )),

    url(r'^archives/$', ListView.as_view(
        queryset = Post.objects.all().order_by("-created"),
        template_name='archives.html'
    )),

    url(r'^tag/(?P<tag>\w+)$',views.tagpage),
    url(r'^feed/$',BlogFeed()),

]