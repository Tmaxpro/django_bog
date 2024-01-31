from django.shortcuts import render


def index(request):
    return render(request, "DocBlog/index.html", context={"prenom" : "Curtis"})