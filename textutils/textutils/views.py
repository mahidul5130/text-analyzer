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
        params = {'purpose': '', 'analyzed_text': analyzed}

        if removepunc:
            analyzed = ''.join(char for char in analyzed if char not in string.punctuation)
            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

        if fullcaps:
            analyzed = analyzed.upper()
            params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

        if extraspaceremover:
            analyzed = ' '.join(analyzed.split())
            params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}

        if newlineremover:
            analyzed = analyzed.replace('\n', '').replace('\r', '')
            params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}

        if numberremover:
            analyzed = ''.join(char for char in analyzed if not char.isdigit())
            params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}

        if reversetext:
            analyzed = analyzed[::-1]
            params = {'purpose': 'Reversed Text', 'analyzed_text': analyzed}

        if allspaceremover:
            analyzed = analyzed.replace(' ', '')
            params = {'purpose': 'Removed All Spaces', 'analyzed_text': analyzed}

        if lowercase:
            analyzed = analyzed.lower()
            params = {'purpose': 'Converted to Lowercase', 'analyzed_text': analyzed}

        if not (removepunc or fullcaps or extraspaceremover or newlineremover or numberremover or reversetext or allspaceremover or lowercase):
            return HttpResponse("Please select any operation and try again")

        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Invalid request method")

def about(request):
    return render(request, 'about.html')