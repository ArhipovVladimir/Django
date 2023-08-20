from django.shortcuts import render
from django.http import HttpResponse
from random import randint
import logging

logger = logging.getLogger(__name__)


def index(response):
    logger.info(f'HttpResponse Index OK')
    return HttpResponse('<h1>Учебный проект <h1>'
                        '<h3>по изучению  фреймворка Django<h3>')


def about(response):
    logger.info(f'HttpResponse seite OK')
    return HttpResponse('<h1>Обо мне <h1>'
                        '<h3>Архипов Владимир<h3>'
                        '<h4>студент GB  <h4>'
                        '<h4>Алтайский край  <h4>')