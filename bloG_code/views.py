from django.shortcuts import render
from .models import Blog_code
from django.views.generic import (ListView,DetailView)
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.


class Blog_list(ListView):
    queryset=Blog_code.objects.all()
    template_name="blog_list.html"


class Blog_detail(DetailView):
    queryset=Blog_code.objects.all()
    template_name="blog_details.html"
    context_object_name="detail_of_a_blog"

    def get_object(self):
        return get_object_or_404(Blog_code,id=self.kwargs.get("id"))
