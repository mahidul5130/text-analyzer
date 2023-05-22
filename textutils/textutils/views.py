from django.http import HttpResponse

def index(request):
    return HttpResponse('''Harry  Django CodeWithHarry''')

def about(request):
    return HttpResponse("About Harry Bhai")