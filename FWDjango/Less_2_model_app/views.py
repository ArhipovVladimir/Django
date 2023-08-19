from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index Less 2')
    return HttpResponse("Hello, world! Less 2")

# Create your views here.
