from django.shortcuts import render
from .forms import FeedbackForm

# Create your views here.

def index(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'index.html')
