from django.shortcuts import render
import datetime
from django.utils.safestring import mark_safe

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_str = "<h1>Wasd</h1>"
    my_context = {
        "my_text": "this is me",
        "my_number": 123,
        "my_list": [123, 321, 213, "abc", datetime.datetime.now()],
        "my_html": mark_safe(my_str),
    }
    return render(request, "about.html", my_context)
