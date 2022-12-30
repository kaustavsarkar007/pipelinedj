from functools import cache
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    djtext = request.GET.get('text','default')

    #Check checkbox values
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    capitaliz =   request.GET.get('capitaliz','off')
    newlineremover =   request.GET.get('newlineremover','off')
    spaceremover =   request.GET.get('spaceremover','off')
    charactercounter =   request.GET.get('charactercounter','off')
    

    #Check with checkbox is on
    if removepunc =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
            
        params = {'Purpose': 'Remove Punctuation',
        'analyzed_text': analyzed}
        djtext = analyzed
    
    if fullcaps =="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
            params = {'Purpose': 'UPPERCASE',
        'analyzed_text': analyzed}
        djtext = analyzed

    if charactercounter =="on":
        analyzed  = len(djtext)
        params = {'Purpose': 'Character Counter',
        'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover  =="on":
        analyzed = ""
        
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char
        params = {'Purpose': 'Remove newlines','analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover  =="on":
        analyzed = ""
        
        for char in djtext:
            if char != " ":
                analyzed = analyzed+char
    params = {'Purpose': 'Remove newlines',
    'analyzed_text': analyzed}
    djtext = analyzed
    
    if capitaliz == "on":
        a = djtext.capitalize()
        
        params = {'Purpose': 'Capitalize',
        'analyzed_text': a}
        djtext =  analyzed
    

    return render(request,'analyze.html',params)
