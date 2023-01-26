from django.urls import reverse_lazy, reverse
from sbl.models import Products, Blog
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# Create your views here.


def contacts(request):
    return render(request, 'sbl/contacts.html')


class BlogListView(ListView):
    model = Blog


class HomeListView(ListView):
    model = Products


class BlogCreateView(CreateView):
    model = Blog
    fields = ('heading', 'content', 'image')
    success_url = reverse_lazy('sbl:blog')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('heading', 'content', 'image', 'status')
    success_url = reverse_lazy('sbl:blog')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('sbl:blog')


class BlogDetailView(DetailView):
    model = Blog
    fields = ('heading', 'content', 'image')

