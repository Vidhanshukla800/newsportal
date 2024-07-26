from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator
import requests

# Create your views here.
def index(request):
    data =slider.objects.all().order_by('-id')[0:2]
    d=ncategory.objects.all().order_by('-id')
    nc = city.objects.all().order_by('-id')
    tn = trending.objects.all().order_by('-id')[0:3]
    myn = mynews.objects.all().order_by('-id')[0:20]
    th = topheadline.objects.all().order_by('-id')[0:1]
    vd = videonews.objects.all().order_by('-id')[0:21]
    mydict={"res":data,"data":d,"ncity":nc,"tdata":tn,"ndata":myn,"thd":th,"vdata":vd,}
    return render(request, 'user/index.html',context=mydict)
#########################################################
def aboutus(request):
    th = topheadline.objects.all().order_by('-id')[0:1]
    tn = trending.objects.all().order_by('-id')[0:3]
    mydict={"thd":th,"tdata":tn}
    return render(request, 'user/aboutus.html',context=mydict)
###########################################################
def contact(request):
    status=False
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mob')
        message = request.POST.get('msg')
        contactus(Name=name,Email=email,Mobile=mobile,Message=message).save()
        status=True
    tn = trending.objects.all().order_by('-id')[0:3]
    th = topheadline.objects.all().order_by('-id')[0:1]
    return render(request, 'user/contact.html',context={'msg':status,"tdata":tn,"thd":th})

##########################################################
def video(request):
    from django.db.models import Q
    th = topheadline.objects.all().order_by('-id')[0:1]
    vd = videonews.objects.all().order_by('-id')
    if request.method=="GET":
        s=request.GET.get("search")
        if s is not None:
         vd=videonews.objects.all().filter(Q(vhead__icontains=s)| Q(vcategory__icontains=s)| Q(vcity__icontains=s))

    tn = trending.objects.all().order_by('-id')[0:3]
    mydict = {"thd": th,"vdata":vd,"tdata":tn}
    return render(request, 'user/video.html',mydict)
#############################################################
def gallery(request):
    d=igallery.objects.all().order_by('-id')
    th = topheadline.objects.all().order_by('-id')[0:1]
    tn = trending.objects.all().order_by('-id')[0:3]
    mydict={"data":d,"thd":th,"tdata":tn}
    return render(request, 'user/gallery.html',context=mydict)
###########################################################
def news(request):
    myn=mynews.objects.all().order_by('-id')
    paginator = Paginator(myn,10)
    page_number=request.GET.get('page')
    newsDatafinal=paginator.get_page(page_number)
    totalpage=newsDatafinal.paginator.num_pages
    d = ncategory.objects.all().order_by('-id')
    tn = trending.objects.all().order_by('-id')[0:3]
    nc = city.objects.all().order_by('-id')[0:13]
    th = topheadline.objects.all().order_by('-id')[0:1]
    x = trending.objects.all().order_by('-id')[0:3]
    mydict={"data":newsDatafinal,"ncat":d,"ncity":nc,"thd":th,"ndata": x,"totalPagelist":[n+1 for n in range(totalpage)],"tdata":tn}
    return render(request, 'user/news.html',context=mydict)
##########################################################
def ndetails(request):
    nid = request.GET.get("n")
    x=mynews.objects.all().filter(id=nid)
    th = topheadline.objects.all().order_by('-id')[0:1]
    tn = trending.objects.all().order_by('-id')[0:3]
    myd={"ndata":x,"thd":th,"tdata":tn}
    return render(request, 'user/ndetails.html',myd)
##########################################################
def login(request):
    th = topheadline.objects.all().order_by('-id')[0:1]
    tn = trending.objects.all().order_by('-id')[0:3]
    mydict = {"thd": th,"tdata":tn}
    return render(request, 'user/login.html',mydict)
#########################################################
def viewnews(request):
    a=request.GET.get("ab")
    x=mynews.objects.all().order_by('-id').filter(ncategory=a)
    th = topheadline.objects.all().order_by('-id')[0:1]
    tn = trending.objects.all().order_by('-id')[0:3]
    mydict={"ndata":x,"thd":th,"tdata":tn}
    return render(request,'user/viewnews.html',context=mydict)
###################################################################
def trendnews(request):
    nid = request.GET.get("n")
    x = trending.objects.all().filter(id=nid)
    th = topheadline.objects.all().order_by('-id')[0:1]
    tn = trending.objects.all().order_by('-id')[0:3]
    myd = {"ndata": x, "thd": th,"tdata":tn}
    return render(request, 'user/trendnews.html', myd)
################################################################
def slidenews(request):
    nid = request.GET.get("n")
    x = slider.objects.all().filter(id=nid)
    th = topheadline.objects.all().order_by('-id')[0:1]
    tn = trending.objects.all().order_by('-id')[0:3]
    myd = {"ndata": x, "thd": th,"tdata":tn}
    return render(request, 'user/slidenews.html', myd)
################################################################
def citynews(request):
    a = request.GET.get("ab")
    x = mynews.objects.all().order_by('-id').filter(ncity=a)
    th = topheadline.objects.all().order_by('-id')[0:1]
    tn = trending.objects.all().order_by('-id')[0:3]
    mydict = {"ndata": x, "thd": th,"tdata":tn}
    return render(request, 'user/citynews.html', context=mydict)
#####################################################################
def videodetails(request):
    vid = request.GET.get("vd")
    x = videonews.objects.all().filter(id=vid)
    th = topheadline.objects.all().order_by('-id')[0:1]
    tn = trending.objects.all().order_by('-id')[0:3]
    myd = {"ndata":x,"thd":th,"tdata":tn}
    return render(request,'user/videodetails.html',myd)

def insta(request):
    return redirect("https://www.instagram.com/technochangers/")

def facebook(request):
    return redirect("https://www.facebook.com/vidhan.shukla.986")

def youtube(request):
    return redirect("https://www.youtube.com/channel/UCP6n_R0WWNTUlr8V7Ar3vKw")

def linkdin(request):
    return redirect("https://www.linkedin.com/in/vidhan-shukla-72519122b/")