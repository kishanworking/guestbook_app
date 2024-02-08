from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
                    # same from urls 
def profile(request,number="default User"):
    return HttpResponse('<h1> this is profile page {}.</h1>'.format(number))


def article(request, article_value):
    return HttpResponse('<h1>the article name is {}'.format(article_value))

