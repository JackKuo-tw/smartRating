from django.shortcuts import render
from django.http import HttpResponse
from .models import Rating, Option
from django import forms
#from django.http import HttpResponse
# Create your views here.

class smartRatingForm(forms.ModelForm):
    """ 配合資料庫自訂表單欄位 """
    class Meta:
        model = Rating
        fields = ['age', 'gender', 'edu', 'expertise', 'religion',
        'race', 'marriage', 'grow_city', 'grow_town', 'fill_time',
        'fill_city', 'fill_town', 'whatIsWisdom', 'is_wisdom1', 'most_wisdom', 
        'most_wisdom_year', 'most_wisdom_old', 'most_wisdom_period', 'special', 
        'wisdom_perform', 'think', 'idea', 'postiveEffect', 'who_postiveEffect', 
        'what_postiveEffect', 'think_period', 'is_wisdom2', 'why_wisdom', 
        'realize', 'why_realize','IP_addr'] 

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    if request.method == 'POST':
        request.POST._mutable = True # 設定為可寫入

        # ** 將字串轉為 int 以符合資料庫型態
        int_list = ['age','is_wisdom1', 'most_wisdom_year', 'most_wisdom_old', 'most_wisdom_period', 
        'wisdom_perform', 'idea', 'postiveEffect', 'most_wisdom_period', 'who_postiveEffect', 
        'what_postiveEffect', 'think_period', 'is_wisdom2', 'realize']
        for i in range(len(int_list)):
            request.POST[int_list[i]] = int(request.POST[int_list[i]])
        # ** 轉換結束
        
        request.POST["IP_addr"] = get_client_ip(request)
        form = smartRatingForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            # 每次五個或十個用 JS DOM Method 產生的 input，存到另一張 table 並且做關聯，因為欄位可能為空
            input_list = ["think_element", "behavior_element", "wisdom_difficulty", "wisdom_conquer", "recall_element", "postiveEffect_element"]
            for text in input_list:
                for i in range(10):
                    try:
                        s = request.POST[text + "_" + str(i)]
                        if not (not s or s.isspace()):
                            Option.objects.create(name=text, content=s, which=new_form)
                    except:
                        pass
            return HttpResponse("success")
        else:
            return HttpResponse("failed")
    return render(request, 'index.html')

def show(request):
    R = Rating.objects.all()
    return render(request, 'show.html', locals())