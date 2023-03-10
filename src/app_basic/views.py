from django.http import HttpResponse


def index(request):
    return HttpResponse(b"Hello, world. You're at the app_basic index.")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s " % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
