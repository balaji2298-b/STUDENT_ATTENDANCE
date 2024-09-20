from django.shortcuts import render,redirect
from .models import Formpage


def index(request):
    data = Formpage.objects.raw("select id, count(pre) as pre from attendancesystem_formpage where pre='pre'")
    hit = Formpage.objects.raw("select id, count(abe) as abe from attendancesystem_formpage where abe='abe'") 
    return render(request,"index.html",{'data': data, 'hit':hit})


def formpage(request):
    if request.method == "POST":
        serial_no = request.POST.get("serial_no")
        studentsname = request.POST.get("studentsname")
        contactnumber = request.POST.get("contactnumber")
        course = request.POST.get("course")
        intime = request.POST.get("intime")
        outtime = request.POST.get("outtime")
        pre = request.POST.get("pre")
        abe = request.POST.get("abe")
        inform = request.POST.get("inform")
        formpage = Formpage(serial_no=serial_no, studentsname=studentsname, contactnumber=contactnumber, course=course, intime=intime, outtime=outtime, pre=pre, abe=abe, inform=inform)
        formpage.save()
        return redirect("index")
    else:
        return render(request,"formpage.html")

def read_java(request):
    formpagea = Formpage.objects.filter(course='CORE JAVA')
    context = {'formpagea':formpagea}
    return render(request, "javastudents.html", context)

def read_python(request):
    formpageb = Formpage.objects.filter(course='CORE PYTHON')
    context = {'formpageb':formpageb}
    return render(request, "pythonstudents.html", context) 

def read_tally(request):
    formpagec = Formpage.objects.filter(course='TALLY')
    context = {'formpagec':formpagec}
    return render(request, "tallystudents.html", context)

def read_typewriting(request):
    formpaged = Formpage.objects.filter(course='TYPEWRITING')
    context = {'formpaged':formpaged}
    return render(request, "typewritingstudents.html", context)

def read_noleave(request):
    formpagee = Formpage.objects.filter(pre='pre')
    context = {'formpagee':formpagee}
    return render(request, "noleavestudents.html", context)

def read_oneweekleave(request):
    formpagef = Formpage.objects.filter(abe='abe')
    context = {'formpagef':formpagef}
    return render(request, "oneweekleavestudents.html", context)


def allcoursestudents(request):
    formpagea = Formpage.objects.filter(course='CORE JAVA')
    formpageb = Formpage.objects.filter(course='CORE PYTHON')
    formpagec = Formpage.objects.filter(course='TALLY')
    formpaged = Formpage.objects.filter(course='TYPEWRITING')
    context = {'formpagea':formpagea,'formpageb':formpageb,'formpagec':formpagec,'formpaged':formpaged}
    return render(request,"allcourse.html",context)


def biometricuploadfile(request):
    return render(request, "biometricuploadfile.html")

