from django.shortcuts import render
from django.http import HttpResponse
import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse("<h1>Главная</h1>"
                        "<p>первая страница на Django</p>")

def about(request):
    logger.debug('About page accessed')
    return HttpResponse("<h1>О себе</h1>"
                        "<p>Истомин Кирилл студент Geekbrains</p>")
