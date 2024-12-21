from django.shortcuts import render
from django.http import HttpResponse
from .forms import CareerInputForm
# Create your views here.

def index(request):
    #print(request.user)
    return HttpResponse("Hello, %s. Curious about career development? You're at the right place!" % request.user)

def advice(request):
    if request.method == 'POST':
        form = CareerInputForm(request.POST)
        if form.is_valid():
            linkedin_url = form.cleaned_data['linkedin_url']
            job_description = form.cleaned_data['job_description']
            career_goals = form.cleaned_data['career_goals']
            skills_experience = form.cleaned_data['skills_experience']
            print(linkedin_url)
            # Process the input with AI model here
            return render(request, 'advisor/advice.html', {'advice': 'Your tailored career advice here.'})
    else:
        form = CareerInputForm()
        text= f"Hello, {request.user}. Curious about career development? You're at the right place!" 
    return render(request, 'advisor/index.html', {'form': form, 'text': text})

#return render(request, 'advisor/advice.html', {'advice': 'Your tailored career advice here.'})