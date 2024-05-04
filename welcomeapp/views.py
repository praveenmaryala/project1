from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor="cyan"><center><h1>welcome lokeshit</h1></center></body></html>""")
    return res