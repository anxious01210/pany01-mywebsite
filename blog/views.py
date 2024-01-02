from django.shortcuts import render


# Create your views here.
def post_list(request):
    context = {}
    return render(request, "blog/post_list.html", context)


def post_detail(request, id):
    context = {}
    return render(request, "blog/post_detail.html", context)
