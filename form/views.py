from django.shortcuts import render
from django.http import HttpResponse
from .models import Rating, Option
from django import forms
#from django.http import HttpResponse
# Create your views here.

class smartRatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['age', 'gender', 'edu', 'expertise', 'religion', 'race', 'marriage', 'grow_city', 'grow_town', 'fill_city', 'fill_town', 'whatIsWisdom', 'is_wisdom1', 'most_wisdom', 'most_wisdom_year', 'most_wisdom_old', 'most_wisdom_period', 'special', 'wisdom_perform', 'think', 'idea', 'postiveEffect', 'who_postiveEffect', 'what_postiveEffect', 'think_period', 'is_wisdom2', 'why_wisdom', 'realize', 'why_realize',] 
        #fields = ['age',]

def index(request):
    if request.method == 'POST':
        request.POST._mutable = True #設定為可寫入
        int_list = ['age','is_wisdom1','most_wisdom_year','most_wisdom_old','most_wisdom_period','wisdom_perform','idea','postiveEffect','most_wisdom_period','who_postiveEffect','what_postiveEffect','think_period','is_wisdom2','realize']
        for i in range(len(int_list)):
           if i < 14:
                request.POST[int_list[i]] = int(request.POST[int_list[i]])
           else:
               request.POST[int_list[i]] = 1
        # request.POST['age'] = int(request.POST['age'])
        # request.POST['is_wisdom1'] = int(request.POST['is_wisdom1'])
        # request.POST['most_wisdom_year'] = int(request.POST['most_wisdom_year'])
        # request.POST['most_wisdom_old'] = int(request.POST['most_wisdom_old'])
        # request.POST['most_wisdom_period'] = int(request.POST['most_wisdom_period'])
        # request.POST['wisdom_perform'] = int(request.POST['wisdom_perform'])
        # request.POST['idea'] = int(request.POST['idea'])
        # request.POST['postiveEffect'] = int(request.POST['postiveEffect'])
        # request.POST['most_wisdom_period'] = int(request.POST['most_wisdom_period'])
        # request.POST['who_postiveEffect'] = int(request.POST['who_postiveEffect'])
        # request.POST['what_postiveEffect'] = int(request.POST['what_postiveEffect'])
        # request.POST['think_period'] = 1
        # request.POST['is_wisdom2'] = 1
        # request.POST['realize'] = 1
        
        form = smartRatingForm(request.POST)
        print(request.POST)
        if form.is_valid():
            new_form = form.save()
            return HttpResponse("success")
        else:
            return HttpResponse("failed")
    return render(request, 'index.html')