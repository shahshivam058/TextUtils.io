from django.http import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    return render(request,"index.html")

def analyze(request):
    dj_text = request.POST.get("text","default")
    removepunc = request.POST.get("removepunc","off")
    fullcaps = request.POST.get("fullcaps","off")
    newlineremover = request.POST.get("newlineremover","off")
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc == "on":
        analyzed = ""
        for char in dj_text:
            if char not in punctuations:
                analyzed = analyzed + char
        context = {
            "purpose" : "Remove Punctuation",
            "analyzed_text" : analyzed
        }
        return render(request,"analyze.html",context)
    elif fullcaps == "on":
        analyzed = ""
        for char in dj_text:
            analyzed = analyzed + char.upper()
        context = {
            "purpose" : "Full Capitalize",
            "analyzed_text" : analyzed
        }
        return render(request,"analyze.html",context)
    elif newlineremover == "on":
        analyzed = ""
        for char in dj_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        context = {
            "purpose" : "New Line Removal",
            "analyzed_text" : analyzed
        }
        return render(request,"analyze.html",context)
    else :
        return HttpResponse("error")