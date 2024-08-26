from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    current_time=datetime.now().time()
    if 6 <= current_time.hour < 12:
        greet_message = "Good Morning"
    elif 12 <= current_time.hour <12:
        greet_message = "Good Afternoon"
    else:
        greet_message = "Good Evening"
    return render(request,'index.html',{'curr_time':current_time,'greet':greet_message})