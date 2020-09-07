from django.shortcuts import render
from django.http import HttpResponse
from collections import Counter 
# Create your views here.
def home(request):
    return render(request, 'home.html');

def add(request):
    string = request.POST['string']
    #print("val1",string)

    fileName= request.FILES['filename'].read()
    word_list= str(fileName, encoding='UTF-8').split('\n')

    result = list(filter(lambda x: (Counter(string) == Counter(x)),word_list)) 
    print(result)
    return render(request, 'result.html', {'string':string , 'result':result});