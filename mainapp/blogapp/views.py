from django.shortcuts import render
from django.views.generic import TemplateView
from blogapp.models import BlogPost

#debugging
import sys
from pprint import pprint

# Create your views here.

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class CreateBlogPageView(TemplateView):
    template_name="createblog.html"


#find out how to create blog post with Django
# class BlogPageView(TemplateView):
#     def get(self, request, **kwargs):
#         return render(request, 'blogpost.html', context=None)

class BlogPageView(TemplateView):
    def get(self, request, **kwargs):
        posts = BlogPost.objects.all()
        print >>sys.stderr, BlogPost.objects.all()
        for test in BlogPost.objects.all():
            print >>sys.stderr, pprint(vars(test))
        post_body_list = [post.body for post in posts]
        for post in post_body_list:
            print >>sys.stderr, post
        return render(request, 'blogpost.html', {'posts':posts})
        #return BlogPageView.as_view()
    #template_name = "blogpost.html"
