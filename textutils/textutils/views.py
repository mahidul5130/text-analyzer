# views.py
# I have created this file - Harry
from django.http import HttpResponse

# Code for video: 6
def index(request):
    return HttpResponse('''<h1>Welcome Home</h1> <a href="links">Visit Links</a>''')

def about(request):
    return HttpResponse("About Harry Bhai")

def links(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))