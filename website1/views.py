from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from website1.decorators import unauthenticated_user
from website1.models import Project
from website1.models import UserModel
from website1.models import Feedback

user_dept1=""
user_year1=""
org=""
role=""

def home(request):
    if request.user.is_authenticated:
        if not UserModel.objects.filter(user_email=request.user.email).exists():
            return redirect("editdata")
    
    return render(request, "website1/index.html")

@login_required(login_url='/')
def itdept(request):
    datait=Project.objects.filter(dept='it')
    datait_rb=Project.objects.filter(dept='it').filter(proj_category='RESEARCH BASED')
    datait_pd=Project.objects.filter(dept='it').filter(proj_category='PRODUCT DEVELOPMENT')
    datait_et=Project.objects.filter(dept='it').filter(proj_category='EMERGING TECHNOLOGY')
    datait_env=Project.objects.filter(dept='it').filter(proj_category='SUSTAINABILITY')

    context={
    'datait':datait,
    'datait_rb':datait_rb,
    'datait_pd':datait_pd,
    'datait_et':datait_et,
    'datait_env':datait_env
    }

    if request.method=="POST":
        rating = int(request.POST.get("rating"))
        cmts = request.POST.get("comments")
        feedb_for_name = request.POST.get("for_proj") 
        Feedback.objects.create(rating=rating, user_feedback=cmts , project_dept=Project.objects.get(proj_title=feedb_for_name).dept , project_f=Project.objects.get(proj_title=feedb_for_name), user_f=UserModel.objects.get(user_email=request.user.email),user_role=UserModel.objects.get(user_email=request.user.email).user_designation,org_name=UserModel.objects.get(user_email=request.user.email).organisation)
    return render(request, "website1/it.html",context)

@login_required(login_url='/')
def compsdept(request):
    datacomps=Project.objects.filter(dept='comps')
    datacomps_rb=Project.objects.filter(dept='comps').filter(proj_category='RESEARCH BASED')
    datacomps_pd=Project.objects.filter(dept='comps').filter(proj_category='PRODUCT DEVELOPMENT')
    datacomps_et=Project.objects.filter(dept='comps').filter(proj_category='EMERGING TECHNOLOGY')
    datacomps_env=Project.objects.filter(dept='comps').filter(proj_category='SUSTAINABILITY')

    context={
    'datacomps':datacomps,
    'datacomps_rb':datacomps_rb,
    'datacomps_pd':datacomps_pd,
    'datacomps_et':datacomps_et,
    'datacomps_env':datacomps_env
    }

    if request.method=="POST":
        rating = int(request.POST.get("rating"))
        cmts = request.POST.get("comments")
        feedb_for_name = request.POST.get("for_proj") 
        print(Project.objects.get(proj_title=feedb_for_name).dept,'thiss issssssssssss')
        Feedback.objects.create(rating=rating, user_feedback=cmts , project_dept=Project.objects.get(proj_title=feedb_for_name).dept , project_f=Project.objects.get(proj_title=feedb_for_name), user_f=UserModel.objects.get(user_email=request.user.email))

    return render(request, "website1/comps.html",context)

@login_required(login_url='/')
def mechdept(request):
    datamech=Project.objects.filter(dept='mech')
    datamech_rb=Project.objects.filter(dept='mech').filter(proj_category='RESEARCH BASED')
    datamech_pd=Project.objects.filter(dept='mech').filter(proj_category='PRODUCT DEVELOPMENT')
    datamech_env=Project.objects.filter(dept='mech').filter(proj_category='SUSTAINABILITY')
    datamech_cw=Project.objects.filter(dept='mech').filter(proj_category='COMMUNITY WELFARE')

    context={
    'datamech':datamech,
    'datamech_rb':datamech_rb,
    'datamech_pd':datamech_pd,
    'datamech_env':datamech_env,
    'datamech_cw':datamech_cw
    }

    if request.method=="POST":
        rating = int(request.POST.get("rating"))
        cmts = request.POST.get("comments")
        feedb_for_name = request.POST.get("for_proj") 
        Feedback.objects.create(rating=rating, user_feedback=cmts , project_dept=Project.objects.get(proj_title=feedb_for_name).dept , project_f=Project.objects.get(proj_title=feedb_for_name), user_f=UserModel.objects.get(user_email=request.user.email))

    return render(request, "website1/mech.html",context)

@login_required(login_url='/')
def extcdept(request):
    dataextc=Project.objects.filter(dept='extc')
    dataextc_rb=Project.objects.filter(dept='extc').filter(proj_category='RESEARCH BASED')
    dataextc_pd=Project.objects.filter(dept='extc').filter(proj_category='PRODUCT DEVELOPMENT')
    dataextc_et=Project.objects.filter(dept='extc').filter(proj_category='EMERGING TECHNOLOGY')

    context={
    'dataextc':dataextc,
    'dataextc_rb':dataextc_rb,
    'dataextc_pd':dataextc_pd,
    'dataextc_et':dataextc_et
    }

    if request.method=="POST":
        rating = int(request.POST.get("rating"))
        cmts = request.POST.get("comments")
        feedb_for_name = request.POST.get("for_proj") 
        # print(rating,cmts,feedb_for_name,request.user, "thisss issssssssssss ")
        print(Project.objects.get(proj_title=feedb_for_name).dept,'thiss issssssssssss')
        Feedback.objects.create(rating=rating, user_feedback=cmts , project_dept=Project.objects.get(proj_title=feedb_for_name).dept , project_f=Project.objects.get(proj_title=feedb_for_name), user_f=UserModel.objects.get(user_email=request.user.email))
        
    return render(request, "website1/extc.html",context)

def privacypolicy(request):
    return render(request, "website1/privacypolicy.html")    

def edit_data(request):

    global org
    global role
    global user_dept1
    global user_year1

    if UserModel.objects.filter(user_email=request.user.email).exists():
        return redirect("/")
    elif request.method=="POST":
         
        org   = request.POST.get("org")
        role  = request.POST.get("role")

        if org == "other":
            org   = request.POST.get("other_org")
            user_dept1= "-"
            user_year1 = "-"
        elif org == "DBIT" and role == "STUDENT":
            user_dept1 = request.POST.get("stream")
            user_year1 = request.POST.get("year")
        elif org == "DBIT" and role == "FACULTY":
            user_dept1 = request.POST.get("stream")
            user_year1 = "-"
        else:
            user_dept1="-"
            user_year1="-"

        if request.user.is_authenticated and not UserModel.objects.filter(user_email=request.user.email).exists():
            UserModel.objects.create(organisation=org, user_designation=role, user_name=request.user.username, user_email=request.user.email,user_dept=user_dept1,user_year=user_year1)


        print(org,role,user_dept1,user_year1,"thisss issssssssssss ")

        return redirect("/")

    context={
        'email':request.user.email,
        'name' :request.user.first_name + " " + request.user.last_name
    }

    return render(request, "website1/form.html",context) 

@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('login')


