from django.shortcuts import render
from django.http import HttpResponse


def home_page_view(request, *args, **kwargs):
    my_title = "My Home"
    my_content = {
        "page_title": my_title
    }
    html_template = "home.html"
    return render(request, html_template, my_content)


def about_page_view(request, *args, **kwargs):
    my_text = "My about"
    my_content = {
        "page_title": my_text
    }
    html_template = "about.html"
    return render(request, html_template, my_content)
