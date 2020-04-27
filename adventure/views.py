from django.shortcuts import render
from .models import Room, Player
from django.http import HttpResponse


def testing(req):
  return HttpResponse("<html><body>content</body></html>")

