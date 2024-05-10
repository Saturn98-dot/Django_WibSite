from django.shortcuts import render, redirect
from .forms import FeedbackForm

# Create your views here.
def about_me(request):
    context = {}
    return render(request, 'App/about_me.html', context)

def resume(request):
    context = {}
    return render(request, 'App/resume.html', context)

def projects(request):
    context = {}
    return render(request, 'App/projects.html', context)

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'App/contact.html', {'form': form})


def feedback_success(request):
    context = {}
    return render(request, 'App/feedback_success.html', context)
