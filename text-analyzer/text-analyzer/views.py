import string
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    if request.method == 'POST':
        djtext = request.POST.get('text', 'default')
        removepunc = request.POST.get('removepunc', False)
        fullcaps = request.POST.get('fullcaps', False)
        newlineremover = request.POST.get('newlineremover', False)
        extraspaceremover = request.POST.get('extraspaceremover', False)
        numberremover = request.POST.get('numberremover', False)
        reversetext = request.POST.get('reversetext', False)
        allspaceremover = request.POST.get('allspaceremover', False)
        lowercase = request.POST.get('lowercase', False)

        analyzed = djtext
        purposes = []
        
        if removepunc:
            analyzed = ''.join(char for char in analyzed if char not in string.punctuation)
            purposes.append('Removed Punctuations')

        if fullcaps:
            analyzed = analyzed.upper()
            purposes.append('Changed to Uppercase')

        if extraspaceremover:
            analyzed = ' '.join(analyzed.split())
            purposes.append('Removed Extra Spaces')

        if newlineremover:
            analyzed = analyzed.replace('\n', '').replace('\r', '')
            purposes.append('Removed Newlines')

        if numberremover:
            analyzed = ''.join(char for char in analyzed if not char.isdigit())
            purposes.append('Removed Numbers')

        if reversetext:
            analyzed = analyzed[::-1]
            purposes.append('Reversed Text')

        if allspaceremover:
            analyzed = analyzed.replace(' ', '')
            purposes.append('Removed All Spaces')

        if lowercase:
            analyzed = analyzed.lower()
            purposes.append('Converted to Lowercase')

        if not purposes:
            return HttpResponse("Please select any operation and try again")

        params = {'purposes': purposes, 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Invalid request method")

def about(request):
    return render(request, 'about.html')