import pandas as pd
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  redirect, render
from .models import collections , collections2
from functools import wraps

# decorators
def login_required(f):
    @wraps(f)
    def wrap(request,*args,**kwargs):
        if 'admin' in request.session:
            return f(request,*args,**kwargs)
        else:
            return redirect("/admin")
    return wrap

def login_requiredd(g):
    @wraps(g)
    def wrapp(request,*args,**kwargs):
        if 'subadmin' in request.session:
            return g(request,*args,**kwargs)
        else:
            return redirect("/admin")
    return wrapp

def login_requireddd(h):
    @wraps(h)
    def wrappp(request,*args,**kwargs):
        if 'subadmin' in request.session:
            return h(request,*args,**kwargs)
        
        elif 'admin' in request.session:
            return h(request,*args,**kwargs)

        else:
            return redirect("/admin")
    return wrappp

def homepage(request):
    return render(request, 'newhomepagefornstech.html')

def admission(request):
    return render(request, "admission.html")


def certificatefind(request):
    if request.method == "POST":
            number = request.POST.get('certificate_num').upper()
            if collections.find({"CertificateNumber": number }) :
                x = list(collections.find({"CertificateNumber": number }))
                if not x:
                    return HttpResponseRedirect("/verification")
                args = x[0]
                return render(request, 'document1.html', args)
            return HttpResponseRedirect("/verification")
    return render(request, 'certificate_login.html')

def contact_us(request):
    if 'submit' in request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name,email, subject, message)
        return HttpResponseRedirect("/contactus")
    return render(request, 'contact.html')


def adminlogin(request):
    global id , password
    id = request.POST.get('id')
    password = request.POST.get('pass')
    if collections2.find_one({"password":password,"username":id}):
        if id == "nstech":
            request.session["admin"] = True
            return HttpResponseRedirect('/admin/kashif')
        elif id == "subadmin":
            request.session['subadmin'] = True
            return HttpResponseRedirect('/subadmin')
    else:
        return render(request, 'adminlogin.html')


@login_required
def adminpage(request):
    if 'adding' in request.POST:
        name = request.POST.get('name').capitalize()
        fathername = request.POST.get('fathername').capitalize()
        type = request.POST.get('type').capitalize()
        certificate = request.POST.get('certificate').upper()
        course = request.POST.get('course').capitalize()
        months = request.POST.get('months')
        issued = request.POST.get('issued')
        grade = request.POST.get('grade').capitalize()
        fromm = request.POST.get('from')
        too = request.POST.get('too')
        collections.insert_one({"Name": name, "CertificateNumber": certificate,
        "Course": course, "Grade": grade, "From": fromm, "To": too,
        "FatherName": fathername, "CertificateType":type, "Months": months, "IssuedDate": issued})

    if 'deleting' in request.POST:
        certificate = request.POST.get('certificate2')
        collections.delete_many({'CertificateNumber': certificate })
    
    if 'thefile' in request.POST:
        try:
            file = request.FILES['thefile']
            df = pd.read_excel(file)
            data = pd.DataFrame(df)
            li = []
            for i in range(len(df)):
                frdate = str(data.iat[i,6].month_name()[slice(3)]).ljust(4,"-") + str(data.iat[i,6].strftime('%Y'))
                todate = str(data.iat[i,7].month_name()[slice(3)]).ljust(4,"-") + str(data.iat[i,7].strftime('%Y'))
                issuedate = str(data.iat[i,8]).split(" ")
                li.append({"CertificateNumber": data.iat[i,0],"Name": data.iat[i,1],"FatherName": data.iat[i,2],
                "Course":data.iat[i,3],"Months":str(data.iat[i,4]),"CertificateType":data.iat[i,5],"From":frdate,
                "To":todate,"IssuedDate":issuedate[0],"Grade":data.iat[i,9]})
            collections.insert_many(li)
        except ValueError:
            return HttpResponse("<h1>Please Upload only xlsx File Not Any Other File Format</h1>")
        except AttributeError:
            return HttpResponse("<h1>Please Upload File which have Dates in Date Format in xlxs File</h1>")

    if 'deleteall' in request.POST:
        collections.delete_many({})
    

    if 'searches' in request.POST:
        srchno = str(request.POST.get('search'))
        result = list(collections.find({"CertificateNumber": {"$regex":srchno}}))
        arr = {"context": result}
        return render(request, "searches.html",arr)
    
    if 'logout' in request.POST:
        del request.session["admin"]
        return HttpResponseRedirect("/")

    x = list(collections.find({}))
    args = {"context":x }
    return render(request, 'adminpage.html', args)

@login_requireddd
def adminedit(request):
    if 'submit' in request.POST:
        certificate1 = request.POST.get('certificate1')
        certificate = request.POST.get('certificate')
        name = request.POST.get('name')
        fathername = request.POST.get('fathername')
        type = request.POST.get('type')
        course = request.POST.get('course')
        months = request.POST.get('months')
        issued = request.POST.get('issued')
        grade = request.POST.get('grade')
        fromm = request.POST.get('from')
        too = request.POST.get('too')
        if certificate:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"CertificateNumber":certificate}})
        if name:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"Name":name}})
        if fathername:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"FatherName":fathername}})
        if type:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"Type":type}})
        if course:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"Course":course}})
        if months:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"Months":months}})
        if issued:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"IssuedDate":issued}})
        if grade:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"Grade":grade}})
        if fromm:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"From":fromm}})
        if too:
            collections.update_one({"CertificateNumber":certificate1},{"$set":{"To":too}})
        return HttpResponseRedirect("/admin/kashif")
    return render(request,'editstudent.html')

def ourservices(request):
    return render(request,'services.html')

def certificatecourses(request):
    return render(request,'certificatecourses.html')

def diplomacourses(request):
    return render(request,'diplomacourses.html')

def languagecourses(request):
    return render(request,'languagecourses.html')

def subadminpermissions(request):
    add = request.POST.get('add')
    edit = request.POST.get('edit')
    search = request.POST.get('search')
    delete = request.POST.get('delete')
    download = request.POST.get('download')
    deldatabase = request.POST.get('deldatabase')
    xlsxfile = request.POST.get('xlsxfile')
    global xodus
    xodus = {"add":add,"edit":edit,"search":search,"delete":delete,"download":download,
    "deldatabase":deldatabase,"xlsxfile":xlsxfile}
    return HttpResponseRedirect('admin/kashif')

@login_requiredd
def subadmin(request):
    try:
        if 'logout' in request.POST:
            del request.session["subadmin"]
            return HttpResponseRedirect("/")

        global xodus
        x = list(collections.find({}))
        xodus['context'] = x
        return render(request,"subadmin.html",xodus)
    except NameError:
        return HttpResponse("Permissions of subadmin are not defined by the admin")

@login_required
def changepassword(request):
    if request.POST.get('pass1') == request.POST.get('pass2'):
        select = request.POST.get('select')
        passw = request.POST.get("pass1")
        if select == "1":
            collections2.update_one({"username":"nstech"},{"$set":{"password":passw}})
            return HttpResponseRedirect("/admin/kashif")
        elif select == "2":
            collections2.update_one({"username":"subadmin"},{"$set":{"password":passw}})
            return HttpResponseRedirect("/admin/kashif")
    else:
        return render(request,'changepassword.html',{"message":1})
    return render(request,'changepassword.html')