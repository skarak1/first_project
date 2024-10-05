from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.
# def index(request):
#     return HttpResponse("Hello world!")
# def index(request):
#     dic = {"insert":"Hello World!!"}
#     return render(request,'index.html',context=dic)

def index(request):
    #dic = {"insert":"Hello World!!"}
    Webpages_list = AccessRecord.objects.order_by('date')
    date_dic = {'access_records':Webpages_list}
    return render(request,'index.html',context=date_dic)