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

        analyzed = djtext
        params = {'purpose': '', 'analyzed_text': analyzed}

        if removepunc:
            analyzed = ''.join(
                char for char in analyzed if char not in string.punctuation)
            params = {'purpose': 'Removed Punctuations',
                      'analyzed_text': analyzed}

        if fullcaps:
            analyzed = analyzed.upper()
            params = {'purpose': 'Changed to Uppercase',
                      'analyzed_text': analyzed}

        if extraspaceremover:
            analyzed = ' '.join(analyzed.split())
            params = {'purpose': 'Removed Extra Spaces',
                      'analyzed_text': analyzed}

        if newlineremover:
            analyzed = analyzed.replace('\n', '').replace('\r', '')
            params = {'purpose': 'Removed Newlines', 'analyzed_text': analyzed}

        if numberremover:
            analyzed = ''.join(char for char in analyzed if not char.isdigit())
            params = {'purpose': 'Removed Numbers', 'analyzed_text': analyzed}

        if not (removepunc or fullcaps or extraspaceremover or newlineremover or numberremover):
            return HttpResponse("Please select any operation and try again")

        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Invalid request method")


def about(request):
    return render(request, 'about.html')