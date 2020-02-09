from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    timestamp = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
    print(timestamp)
    return render(request, 'markov_chatbot.html', dict(timestamp=timestamp))
