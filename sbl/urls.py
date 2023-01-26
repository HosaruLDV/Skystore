from django.urls import path
from sbl.views import contacts, BlogListView, HomeListView, BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView
from sbl.apps import SblConfig

app_name = SblConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),

    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail')
]
