import json
from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render


from .models import *
from django.http import HttpResponse
from math import sin, cos, sqrt, atan2, radians


# Create your views here.

def logout(request):
    auth.logout(request)
    return render (request,'index.html')



def loginpage(request):
    return render(request,"index.html")


def login_btn(request):
    un=request.POST['u']
    pwd=request.POST['p']
    try:
        ob=login_table.objects.get(username=un,password=pwd)
        if ob.type == "admin":
            ob1=auth.authenticate(username="admin",password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
            return HttpResponse("<script>alert('welcome');window.location='/adminhome'</script>")
        elif ob.type=="tp":
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse("<script>alert('welcome');window.location='/trafficpolicehome'</script>")
        else:
            return HttpResponse("<script>alert('Invalid username or password');window.location='/'</script>")


    except:
        return HttpResponse("<script>alert('Invalid username or password');window.location='/'</script>")









@login_required(login_url='/')

def add_ambulance(request):
    return render(request,"admin/ADD AMBULANCE.html")

@login_required(login_url='/')

def add_hospital(request):
    return render(request,"admin/ADDHOSPITAL.html")
@login_required(login_url='/')

def add_trafficpolice(request):
    return render(request,"admin/ADDTRAFFICPOLICE.html")
@login_required(login_url='/')

def adminhome(request):
    return render(request,"admin/index.html")
@login_required(login_url='/')

def editambulance(request):
    return render(request,"admin/EDIT AMBULANCE.html")
@login_required(login_url='/')


def add_amb(request):
    name= request.POST['textfield']
    vehicle_no= request.POST['textfield2']
    photo= request.FILES['file']
    fss = FileSystemStorage()
    photo_file = fss.save(photo.name, photo)
    phone= request.POST['textfield3']
    proof= request.FILES['file2']
    fsv = FileSystemStorage()
    phot_file1 = fsv.save(proof.name, proof)
    usname= request.POST['textfield4']
    password= request.POST['textfield5']

    ob = login_table()
    ob.username = usname
    ob.password = password
    ob.type = 'ambulance'
    ob.save()

    obj = ambulance_table()
    obj.name = name
    obj.vehicle_no= vehicle_no
    obj.phone = phone
    obj.photo = photo_file
    obj.proof = phot_file1
    obj.LOGIN = ob
    obj.save()
    return HttpResponse("<script>alert('Added');window.location='/manageambulance#about'</script>")

@login_required(login_url='/')

def edithospital(request):
    return render(request,"admin/EDITHOSPITAL.html")

@login_required(login_url='/')

def add_hspt(request):
    name = request.POST['textfield']
    dt = request.POST['textfield2']
    pn = request.POST['textfield3']
    email = request.POST['textfield4']
    ltd = request.POST['textfield5']
    lgtd = request.POST['textfield6']
    image= request.FILES['file']
    fss = FileSystemStorage()
    photo = fss.save(image.name, image)

    obj=hospital_table()
    obj.name=name
    obj.details=dt
    obj.phone=pn
    obj.email=email
    obj.latitude=ltd
    obj.longitude=lgtd
    obj.image=photo
    obj.save()
    return HttpResponse("<script>alert('Added');window.location='/managehospital#about'</script>")



@login_required(login_url='/')
def edittrafficpolice(request, trafic_id):
    request.session['trafic_id'] = trafic_id
    traffic_obj = trafficpoolice_table.objects.get(id=trafic_id)
    return render(request,"admin/EDITTRAFFICPOLICE.html", {'traffic_obj': traffic_obj})


@login_required(login_url='/')

def edit_tp_action(request):
    if "file" in request.FILES:
        name=request.POST['textfield']
        place=request.POST['textfield2']
        address=request.POST['textfield3']
        pin=request.POST['textfield4']
        email=request.POST['textfield5']
        phone=request.POST['textfield6']
        photo = request.FILES['file']
        fss = FileSystemStorage()
        photo_file = fss.save(photo.name, photo)
        ob = trafficpoolice_table.objects.get(id=request.session['trafic_id'])
        ob.name = name
        ob.place=place
        ob.address=address
        ob.pin=pin
        ob.phone=phone
        ob.email=email
        ob.photo = photo_file
        ob.save()
        return HttpResponse("<script>alert('edited');window.location='/managetrafficpolice#about'</script>")
    else:
        name = request.POST['textfield']
        place = request.POST['textfield2']
        address = request.POST['textfield3']
        pin = request.POST['textfield4']
        email = request.POST['textfield5']
        phone = request.POST['textfield6']
        ob = trafficpoolice_table.objects.get(id=request.session['trafic_id'])
        ob.name = name
        ob.place=place
        ob.address=address
        ob.pin=pin
        ob.phone=phone
        ob.email=email
        ob.save()
        return HttpResponse("<script>alert('edited');window.location='/managetrafficpolice#about'</script>")



@login_required(login_url='/')

def add_tpbtn(request):
    nm=request.POST['textfield']
    plc=request.POST['textfield2']
    pst=request.POST['textfield3']
    pin=request.POST['textfield4']
    email=request.POST['textfield5']
    ph=request.POST['textfield6']
    des=request.POST['textfield10']
    station=request.POST['station']
    lat=request.POST['lat']
    lon=request.POST['lon']

    photo=request.FILES['file']
    fs=FileSystemStorage()
    fn=fs.save(photo.name,photo)

    un= request.POST['textfield7']
    psw= request.POST['textfield8']

    ob=login_table()
    ob.username=un
    ob.password=psw
    ob.type='tp'
    ob.save()

    obj=trafficpoolice_table()
    obj.name=nm
    obj.station=station
    obj.place=plc
    obj.address=pst
    obj.pin=pin
    obj.email=email
    obj.phone=ph
    obj.photo=fn
    obj.designation=des
    obj.latitude=lat
    obj.longitude=lon
    obj.LOGIN=ob
    obj.save()
    return HttpResponse("<script>alert('Added');window.location='/managetrafficpolice#about'</script>")

@login_required(login_url='/')

def manageambulance(request):
    ob = ambulance_table.objects.all()
    return render(request,"admin/MANAGEAMBULANCE.html", {'val': ob})


@login_required(login_url='/')

def delambulance(request,id):
    res=ambulance_table.objects.get(id=id)
    res.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/manageambulance#about'</script>")
@login_required(login_url='/')

def deltrafficpolice(request,id):
    res=trafficpoolice_table.objects.get(id=id)
    res.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/managetrafficpolice#about'</script>")
@login_required(login_url='/')

def delhospital(request,id):
    res=hospital_table.objects.get(id=id)
    res.delete()
    return HttpResponse("<script>alert('Deleted');window.location='/managehospital#about'</script>")
@login_required(login_url='/')

def managehospital(request):
    ob = hospital_table.objects.all()
    return render(request, "admin/MANAGEHOSPITAL.html", {'val': ob})
@login_required(login_url='/')

def managetrafficpolice(request):
    ob=trafficpoolice_table.objects.all()
    return render(request,"admin/MANAGETRAFFICPOLICE.html",{'val':ob})
@login_required(login_url='/')

def verifydriver(request):
    res=driver_table.objects.all()
    return render(request,"admin/VERIFYDRIVER.html",{"data":res})
@login_required(login_url='/')

def managetpsrch(request):
    driver = request.POST['textfield']
    res=trafficpoolice_table.objects.filter(name__istartswith=driver)
    return render(request,"admin/MANAGETRAFFICPOLICE.html",{"val":res, 'driver_name':driver })
@login_required(login_url='/')

def verify_driver_search(request):
    driver_name = request.POST['textfield']
    res=driver_table.objects.filter(name__startswith=driver_name)
    return render(request,"admin/VERIFYDRIVER.html",{"data":res, 'driver_name': driver_name})
@login_required(login_url='/')

def accident_search(request):
    acc = request.POST['textfield']
    res=accidentreport_table.objects.filter(date=acc)
    return render(request,"admin/VIEW ACCIDENT REPORT.html",{"data":res, 'driver_name': acc})
@login_required(login_url='/')

def AMBULANCE_search(request):
    driver_name = request.POST['textfield']
    res=ambulance_table.objects.filter(name__istartswith=driver_name)
    return render(request,"admin/MANAGEAMBULANCE.html",{"val":res, 'driver_name': driver_name})
@login_required(login_url='/')

def hspt_srch(request):
    driver_name = request.POST['textfield']
    res=hospital_table.objects.filter(name__istartswith=driver_name)
    return render(request,"admin/MANAGEHOSPITAL.html",{"val":res, 'driver_name': driver_name})
@login_required(login_url='/')

def emergency_srch(request):
    driver_name = request.POST['textfield']
    res=emargency_table.objects.filter(ACCIDENTREPORT__date=driver_name)
    return render(request,"traffic_police/VIEW EMERGENCY REPORT.html",{"val":res})


def viewcomplaint(request):
    ob=complaint_table.objects.filter(TRAFFICPOLICE__LOGIN__id=request.session['lid'])
    return render(request,"traffic_police/viewcomplaint.html",{"val":ob})


def sendreply(request,id):
    request.session['sr']=id
    return render(request,"traffic_police/SENDREPLY.html")

def add_replay(request):
    rp = request.POST['textfield']
    obj=complaint_table.objects.get(id=request.session['sr'])
    obj.reply = rp
    obj.save()
    return HttpResponse("<script>alert('success');window.location='/viewcomplaint#about'</script>")



@login_required(login_url='/')

def acceptdriver(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='driver'
    ob.save()
    return HttpResponse("<script>alert('Accepted');window.location='/verifydriver#about'</script>")
@login_required(login_url='/')

def rejectdriver(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='reject'
    ob.save()
    return HttpResponse("<script>alert('Rejected');window.location='/verifydriver#about'</script>")


@login_required(login_url='/')

def viewaccidentreport(request):
    res=accidentreport_table.objects.all()
    return render(request,"admin/VIEW ACCIDENT REPORT.html",{"data":res})
@login_required(login_url='/')

def trafficpolicehome(request):
    return render(request,"traffic_police/index.html")
@login_required(login_url='/')

def trafficpolice(request):
    return render(request,"traffic_police/TRAFFICPOLICE.html")
@login_required(login_url='/')

def viewaccidentreport1(request):
    obt=trafficpoolice_table.objects.get(LOGIN__id=request.session['lid'])
    lat1=  radians(float(obt.latitude))
    lon1=  radians(float(obt.longitude))
    ob=accidentreport_table.objects.all().order_by("-id")
    res=[]
    for i in ob:
        lat2 = float(i.latitude)
        lon2 = float(i.longitude)

        # Convert latitude and longitude to radians if they are in degrees

        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        a = min(1.0, a)  # Ensure 'a' is not greater than 1 to avoid math domain error
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Approximate radius of the Earth in kilometers
        R = 6373.0
        distance = R * c
        print(distance,"==================================")
        if distance < 1000:
            res.append(i)

    return render(request, "traffic_police/VIEW ACCIDENT REPORT.html",{'val':res})


@login_required(login_url='/')

def viewaccidentreport1_search(request):
    date=request.POST['textfield']
    ob=accidentreport_table.objects.filter(date=date)
    return render(request, "traffic_police/VIEW ACCIDENT REPORT.html",{'val':ob})




def assginacc(request,id):
    oo=accidentreport_table.objects.get(id=id)
    oo.status='actioned'
    oo.save()
    request.session['accid']=id
    ob=hospital_table.objects.all()
    ob1=ambulance_table.objects.all()
    return render(request, "traffic_police/ADD emg accident.html", {'val': ob,"val1":ob1})


def assginacccode(request):
    hos = request.POST['select1']
    amb = request.POST['select2']
    obj=emargency_table()
    obj.AMBULANCE=ambulance_table.objects.get(id=amb)
    obj.HOSPITAL=hospital_table.objects.get(id=hos)
    obj.ACCIDENTREPORT=accidentreport_table.objects.get(id=request.session['accid'])
    obj.time=datetime.now()
    obj.date=datetime.today()
    obj.status='pending'
    obj.save()
    return HttpResponse("<script>alert('success');window.location='/viewaccidentreport1#about'</script>")


@login_required(login_url='/')


def viewemergencyreport(request):
    ob=emargency_table.objects.all().order_by("-id")
    print(ob,"gggggggg")
    return render(request, "traffic_police/VIEW EMERGENCY REPORT.html",{'val':ob})



@login_required(login_url='/')
def edithospita(request,id):
    request.session['HSPT_id'] = id
    ob = hospital_table.objects.get(id=id)
    return render(request,"admin/EDITHOSPITAL.html", {'val': ob})
@login_required(login_url='/')

def edithspt(request):
    if "file" in request.FILES:
        name=request.POST['textfield']
        details=request.POST['textfield2']
        phone=request.POST['textfield3']
        email=request.POST['textfield4']
        latitude=request.POST['textfield5']
        longitude=request.POST['textfield6']
        photo = request.FILES['file']
        fss = FileSystemStorage()
        photo_file = fss.save(photo.name, photo)
        ob = hospital_table.objects.get(id=request.session['HSPT_id'])
        ob.name = name
        ob.details=details
        ob.phone=phone
        ob.email=email
        ob.latitude=latitude
        ob.longitude=longitude
        ob.image = photo_file
        ob.save()
        return HttpResponse("<script>alert('edited');window.location='/managehospital#about'</script>")
    else:
        name = request.POST['textfield']
        details = request.POST['textfield2']
        phone = request.POST['textfield3']
        email= request.POST['textfield4']
        latitude= request.POST['textfield5']
        longitude = request.POST['textfield6']
        ob = hospital_table.objects.get(id=request.session['HSPT_id'])
        ob.name = name
        ob.details=details
        ob.photo=phone
        ob.email=email
        ob.latitude=latitude
        ob.longitude=longitude
        ob.save()
        return HttpResponse("<script>alert('edited');window.location='/managehospital#about'</script>")



@login_required(login_url='/')

def editambuln(request, id):
    request.session['amid'] = id
    ob = ambulance_table.objects.get(id=id)
    return render(request,"admin/EDIT AMBULANCE.html", {'val': ob})

@login_required(login_url='/')

def editambula(request):
    try:
        try:
            name = request.POST['textfield']
            vehicle_no = request.POST['textfield2']
            photo = request.FILES['file']
            fss = FileSystemStorage()
            photo_file = fss.save(photo.name, photo)
            proof = request.FILES['file2']
            fsv = FileSystemStorage()
            fs = fsv.save(proof.name, proof)
            phone = request.POST['textfield3']
            obj = ambulance_table.objects.get(id=request.session['amid'])
            obj.name = name
            obj.vehicle_no = vehicle_no
            obj.phone = phone
            obj.photo = photo_file
            obj.proof = fs
            obj.save()
            return HttpResponse("<script>alert('Edited');window.location='/manageambulance#about'</script>")
        except:
            if 'file' in request.FILES:
                name= request.POST['textfield']
                vehicle_no= request.POST['textfield2']
                photo= request.FILES['file']
                fss = FileSystemStorage()
                photo_file = fss.save(photo.name, photo)
                phone= request.POST['textfield3']
                obj = ambulance_table.objects.get(id=request.session['amid'])
                obj.name = name
                obj.vehicle_no= vehicle_no
                obj.phone = phone
                obj.photo = photo_file
                obj.save()
                return HttpResponse("<script>alert('Edited');window.location='/manageambulance#about'</script>")
            elif 'file2' in request.FILES :
                name = request.POST['textfield']
                vehicle_no = request.POST['textfield2']
                phone = request.POST['textfield3']
                proof = request.FILES['file2']
                fsv = FileSystemStorage()
                fs = fsv.save(proof.name, proof)
                obj = ambulance_table.objects.get(id=request.session['amid'])
                obj.name = name
                obj.vehicle_no = vehicle_no
                obj.phone = phone
                obj.proof = fs
                obj.save()
                return HttpResponse("<script>alert('Edited');window.location='/manageambulance#about'</script>")
            else:
                name = request.POST['textfield']
                vehicle_no = request.POST['textfield2']
                phone = request.POST['textfield3']
                proof = request.FILES['file2']
                fsv = FileSystemStorage()
                phot_file1 = fsv.save(proof.name, proof)
                obj = ambulance_table.objects.get(id=request.session['amid'])
                obj.name = name
                obj.vehicle_no = vehicle_no
                obj.phone = phone
                obj.proof = phot_file1
                obj.save()
                return HttpResponse("<script>alert('Edited');window.location='/manageambulance#about'</script>")
    except:
            name = request.POST['textfield']
            vehicle_no = request.POST['textfield2']
            phone = request.POST['textfield3']
            obj = ambulance_table.objects.get(id=request.session['amid'])
            obj.name = name
            obj.vehicle_no = vehicle_no
            obj.phone = phone
            obj.save()
            return HttpResponse("<script>alert('Edited');window.location='/manageambulance#about'</script>")


#########################################################################################################


def registration(request):
        print(request.POST,"hhhhhhhhh")
        Fname=request.POST['fname']
        image=request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(image.name, image)
        place= request.POST['place']
        post_office = request.POST['post']
        phone = request.POST['phone']
        email_id = request.POST['email']
        uname = request.POST['username']
        passwd = request.POST['password']
        lob = login_table()
        lob.username = uname
        lob.password = passwd
        lob.type = 'driver'
        lob.save()
        userob = driver_table()
        userob.name = Fname
        userob.address = place
        userob.regno = post_office
        userob.phone = phone
        userob.email = email_id
        userob.photo = fsave
        userob.LOGIN=lob
        userob.save()
        data = {"task": "valid"}
        r = json.dumps(data)
        print(r)
        return HttpResponse(r)





def login_code(request):
    username = request.POST['uname']
    password = request.POST['pass']
    try:
        login_obj = login_table.objects.get(username=username, password=password)
        if login_obj is None:
            data = {"task": "invalid"}
            return JsonResponse(data)

        else:

            data = {"task": "valid", "id": login_obj.id,"type":login_obj.type}
            return JsonResponse(data)

    except Exception as e:
        print(e)
        data = {"task": "invalid"}
        return JsonResponse(data)


def senntcomplaint(request):
    print(request.POST,"ooooooooo")
    cm=request.POST['complaint']
    id=request.POST['lid']
    tid=request.POST['tid']

    obj = complaint_table()
    obj.DRIVER=driver_table.objects.get(LOGIN__id=id)
    obj.TRAFFICPOLICE = trafficpoolice_table.objects.get(id=tid)
    obj.complaint=cm
    obj.date=datetime.today()
    obj.reply='pending'
    obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)





def setemergencynumber(request):
    nu=request.POST['number']
    id=request.POST['lid']


    obj = emergency_number()
    obj.DRIVER=driver_table.objects.get(LOGIN__id=id)

    obj.number=nu

    obj.save()
    data = {'task': 'success'}
    r = json.dumps(data)
    return HttpResponse(r)











def view_trfalert(request):
    driver_id = request.POST['lid']
    ob = emargency_table.objects.filter(ACCIDENTREPORT__DRIVER__LOGIN=driver_id)
    data = []
    for i in ob:
        d = {'date':i.ACCIDENTREPORT.date, 'time': i.ACCIDENTREPORT.time, 'type': i.ACCIDENTREPORT.type, 'latitude': i.ACCIDENTREPORT.latitude, 'longitude': i.ACCIDENTREPORT.longitude  }
        data.append(d)

    r = json.dumps(data)
    return HttpResponse(r)










def view_nearhspt(request):
    from math import sin, cos, sqrt, atan2, radians
    print(request.POST,"kkkkkkkkkkk")
    lat1 = float(request.POST.get('latitude', 0.0))
    lon1 = float(request.POST.get('longitude', 0.0))
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    ob = hospital_table.objects.all()
    r = []

    for i in ob:
        lat2 = i.latitude
        lon2 = i.longitude

        # Convert latitude and longitude to radians if they are in degrees

        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        a = min(1.0, a)  # Ensure 'a' is not greater than 1 to avoid math domain error
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Approximate radius of the Earth in kilometers
        R = 6373.0
        distance = R * c
        print(distance,"==================================")
        if distance < 1000:
            row = {'name': i.name, 'details': i.details, 'phone': i.phone, 'email': i.email, 'latitude': i.latitude,
                   'longitude': i.longitude, 'photo': i.image.url}
            r.append(row)
    print(r,"hhhhhhhhhhhhhhh")
    print(len(r),"hhhhhhhhhhhhhhh")
    return JsonResponse(r, safe=False)



















def view_traffic(request):
    ob = trafficpoolice_table.objects.all()
    data = []
    for i in ob:
        d = {'name':i.name, 'place':i.place, 'address':i.address, 'pin':i.pin,'phone':i.phone, 'email':i.email,'designation':i.designation, 'station':i.station,'photo':i.photo.url,'id':i.id }
        data.append(d)

    r = json.dumps(data)
    print(r)
    return HttpResponse(r)


def searchtraffic(request):
    name=request.POST['name']
    ob = trafficpoolice_table.objects.filter(station__istartswith=name)
    data = []
    for i in ob:
        d = {'name':i.name, 'place':i.place,'pin':i.pin,'phone':i.phone, 'email':i.email,'designation':i.designation, 'station':i.station,'photo':i.photo.url,'id':i.id }
        data.append(d)

    r = json.dumps(data)
    return HttpResponse(r)



def viewreply(request):
    uid=request.POST['lid']
    print(uid,"kkkkkkkkkkkkk")
    ob = complaint_table.objects.filter(DRIVER__LOGIN__id=uid)
    data = []
    for i in ob:
        d = {'complaint':i.complaint, 'date':str(i.date),'reply':i.reply,'trafficpolice':i.TRAFFICPOLICE.name}
        data.append(d)
        print(d,"jjjjjjjjjjjj")

    r = json.dumps(data)
    return HttpResponse(r)


def viewstation(request):
    ob = trafficpoolice_table.objects.all()
    data = []
    for i in ob:
        d = {'id':i.id, 'station':i.station}
        data.append(d)
        print(d,"jjjjjjjjjjjj")

    r = json.dumps(data)
    return HttpResponse(r)


# def view_nearacci(request):
#     ob = accidentreport_table.objects.all()
#     data = []
#     for i in ob:
#         d = {'DRIVER':i.DRIVER, 'latitude':i.latitude, 'longitude':i.longitude, 'date':i.date,'time':i.time, 'status':i.status, 'type':i.type}
#         data.append(d)
#         data = {'task': 'success'}
#         r = json.dumps(data)
#         return HttpResponse(r)










def view_nearacci(request):
    from math import sin, cos, sqrt, atan2, radians
    print(request.POST,"kkkkkkkkkkk")
    lat1 = float(request.POST.get('latitude', 0.0))
    lon1 = float(request.POST.get('longitude', 0.0))
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    ob = accidentreport_table.objects.all()
    r = []
    # print(request ,session['cid'],"mmmmmmmmm")

    for i in ob:
        lat2 = i.latitude
        lon2 = i.longitude

        # Convert latitude and longitude to radians if they are in degrees

        lat2 = radians(lat2)
        lon2 = radians(lon2)

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        a = min(1.0, a)  # Ensure 'a' is not greater than 1 to avoid math domain error
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Approximate radius of the Earth in kilometers
        R = 6373.0
        distance = R * c
        print(distance,"==================================")
        if distance < 1000:
            row = {'name': i.DRIVER.name, 'details': str(i.date), 'status': i.status,'email': str(i.time),'latitude': i.latitude,
                   'longitude': i.longitude, 'photo': i.DRIVER.photo.url}
            r.append(row)
    print(r,"hhhhhhhhhhhhhhh")
    print(len(r),"hhhhhhhhhhhhhhh")
    return JsonResponse(r, safe=False)






def view_emergencycase(request):
     driver_id = request.POST['lid']
     ob = emargency_table.objects.filter(ACCIDENTREPORT__DRIVER__LOGIN=driver_id)
     data = []
     for i in ob:
         d = {'date': i.ACCIDENTREPORT.date, 'time': i.ACCIDENTREPORT.time, 'type': i.ACCIDENTREPORT.type,'latitude': i.ACCIDENTREPORT.latitude, 'longitude': i.ACCIDENTREPORT.longitude}
         data.append(d)
         data = {'task': 'success'}
     r = json.dumps(data)
     return HttpResponse(r)



def updatelocation(request):
    print (request.POST)
    lati = float(request.POST['lat'])
    lid = float(request.POST['lid'])
    longi = request.POST['lon']
    ob=location_table.objects.filter(LOGIN__id=lid)
    if len(ob) != 0:
            obb=location_table.objects.get(LOGIN__id=lid)
            # obb.USER=user_table.objects.get(LOGIN__id=lid)
            obb.latitude=lati
            obb.longitude=longi

            obb.save()

    else:
            obb=location_table()
            obb.LOGIN = login_table.objects.get(id=lid)
            obb.latitude = lati
            obb.longitude = longi
            obb.save()

    obb=accidentreport_table.objects.filter(date__startswith=datetime.today().strftime("%Y-%m-%d")).exclude(DRIVER__LOGIN_id=lid)

    print(obb)

    for i in obb:
        lat2 = float(i.latitude)
        lon2 = float(i.longitude)
        # Approximate radius of earth in km
        R = 6373.0

        # lat1 = radians(lat1)
        # lon1 = radians(lon1)
        # lat2 = radians(lat2)
        # lon2 = radians(lon2)

        dlon = float(lon2) - float(longi)
        dlat = float(lat2) - float(lati)

        a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
        print(a)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        print(distance)


        if distance<1000:
            data = {"task": "alert"}
            r = json.dumps(data)
            print(r)
            return HttpResponse(r)

    data = {"task": "valid"}
    r = json.dumps(data)
    print(r)
    return HttpResponse(r)
#
#


def emergency(request):
    print(request.POST,"KKKKKKKKKKKKKKKK")
    lati = request.POST['lati']
    lid = request.POST['lid']
    longi = request.POST['longi']

    ob=accidentreport_table()
    ob.latitude=lati
    ob.longitude=longi
    ob.status="emergency"
    ob.date=datetime.today()
    ob.time=datetime.now()
    ob.type="emergency"
    ob.DRIVER=driver_table.objects.get(LOGIN__id=lid)
    ob.save()

    ob=emergency_number.objects.filter(DRIVER__LOGIN__id=lid)
    txt=[]
    for i in ob:
        txt.append(str(i.number))

    txt="#".join(txt)

    data = {"task": "valid","phno":txt}
    r = json.dumps(data)
    print(r)

    return HttpResponse(r)





# ===================================================================================

def and_logincode(request):
    print(request.POST,'lllll')
    un = request.POST['username']
    pwd = request.POST['password']
    print(un, pwd)

    try:
        ob = login_table.objects.get(username=un, password=pwd)

        if ob is None:
            data = {"task": "invalid"}

        elif ob.type == 'ambulance':
            print("in user_type_1 function")
            data = {
                "task": "valid",
                "lid": ob.id,
                "type": ob.type,

            }

        elif ob.type == 'driver':
            print("in user_type_1 function")
            data = {
                "task": "valid",
                "lid": ob.id,
                "type": ob.type,

            }

        else:
            data = {"task": "invalid"}

        return JsonResponse(data)

    except Exception as e:
        print("Error: {e}")  # To log the exception if needed
        data = {"task": "invalid"}
        return JsonResponse(data)



def view_hospital(request):
    lid=request.GET['id']
    lob=location_table.objects.get(LOGIN__id=lid)
    doctors = hospital_table.objects.all()
    longi=float(lob.longitude)
    lati=float(lob.latitude)
    if not doctors.exists():
        return JsonResponse({"status": "ok", "data": []})

    doctor_data = []
    for doctor in doctors:
        lat2 = float(doctor.latitude)
        lon2 = float(doctor.longitude)
        # Approximate radius of earth in km
        R = 6373.0

        # lat1 = radians(lat1)
        # lon1 = radians(lon1)
        # lat2 = radians(lat2)
        # lon2 = radians(lon2)

        dlon = float(lon2) - float(longi)
        dlat = float(lat2) - float(lati)

        a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
        print(a)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        print(distance)
        doctor_data.append({
            'id': doctor.id,
            # 'idd': doctor.Login.id,
            'name': doctor.name,
            'phone': doctor.phone,
            'email': doctor.email,
            'image': request.build_absolute_uri(doctor.image.url),
            'latitude': str(doctor.latitude),
            'longitude': str(doctor.longitude),
            'distance': float(distance),

        })
    print(doctor_data)
    doctor_data.sort(key=lambda x: x['distance'])
    return JsonResponse({"status": "ok", "data": doctor_data})


def view_accident_report(request):
    doctors = accidentreport_table.objects.all().order_by("-id")
    if not doctors.exists():
        return JsonResponse({"status": "ok", "data": []})

    doctor_data = []
    for doctor in doctors:
        doctor_data.append({
            'id': doctor.id,
            'DRIVER': doctor.DRIVER.name,
            'date': str(doctor.date),
            'time': str(doctor.time),
            'status': doctor.status,
            'type': doctor.type,
            'latitude': str(doctor.latitude),
            'longitude': str(doctor.longitude),

        })
    print(doctor_data)
    return JsonResponse({"status": "ok", "data": doctor_data})

import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the sound file
sound = pygame.mixer.Sound(r"C:\Users\LENOVO\Downloads\projectX(3)\projectX\zzz.wav")  # Replace with your actual file

# Play the sound

def get_notifications(request):
    ob=accidentreport_table.objects.filter(type='pending')
    status = False
    for i in ob:
        i.type="viwed"
        i.save()
    if len(ob) > 0:
        status = True

        sound.play()

        # Keep the program running so the sound plays fully
        pygame.time.delay(int(sound.get_length() * 1000))

    return JsonResponse({"task": status, "c": 0, "nc": 0, "txt": 0})
    #         from django.http import JsonResponse
    #         from playsound import playsound
    #
    #         def send_notification(request):
    #             # Path to your sound file
    #             sound_file_path = r"C:\Users\hp\PycharmProjects\scoreboard\whistle.mp3"  # Ensure this path is correct
    #
    #             # Play the custom sound
    #             playsound(sound_file_path)
    #
    #             # Example object 'i' to update status and save (assuming 'i' is already defined)
    #             i.Status = 'noti'
    #             i.save()
    #
    #     # Return JSON response
    # return JsonResponse({"task": status, "c": count, "nc": nc, "txt": txt})


def view_emergency_accident(request):
    doctors = emargency_table.objects.all()
    if not doctors.exists():
        return JsonResponse({"status": "ok", "data": []})

    doctor_data = []
    for doctor in doctors:
        doctor_data.append({
            'id': doctor.id,
            'ACCIDENTREPORT': doctor.ACCIDENTREPORT.date,
            'date': str(doctor.date),
            'time': str(doctor.time),
            'status': doctor.status,
            'type': doctor.type,
            'latitude': str(doctor.latitude),
            'longitude': str(doctor.longitude),

        })
    print(doctor_data)
    return JsonResponse({"status": "ok", "data": doctor_data})

def and_profile(request):
    lid = request.POST.get('lid')
    try:
        student = driver_table.objects.get(LOGIN_id=lid)
        return JsonResponse({
            'status': 'ok',
            'name': student.name,
            'address': student.address,
            'email': student.email,
            'regno': student.regno,
            'phonenumber': str(student.phone),
            'image': request.build_absolute_uri(student.photo.url),

        })
    except driver_table.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'User not found'})

def driver_update_profile(request):
    lid = request.POST.get('lid')
    name = request.POST.get('name')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    regno = request.POST.get('regno')

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        fp = fs.save(photo.name, photo)
        student = driver_table.objects.get(LOGIN_id=lid)
        student.name = name
        student.address = address
        student.phone = phone
        student.email = email
        student.regno = regno
        student.photo = fp
        student.save()
        return JsonResponse({'status': 'ok', 'message': 'Profile updated successfully'})
    else:
        student = driver_table.objects.get(LOGIN_id=lid)
        student.name = name
        student.address = address
        student.phone = phone
        student.email = email
        student.regno = regno
        student.save()
        return JsonResponse({'status': 'ok', 'message': 'Profile updated successfully'})

def driver_view_hospital(request):
    try:
        lid = request.GET['id']
    except:
        lid=2
    lob = location_table.objects.get(LOGIN__id=lid)
    doctors = hospital_table.objects.all()
    longi = float(lob.longitude)
    lati = float(lob.latitude)
    if not doctors.exists():
        return JsonResponse({"status": "ok", "data": []})

    doctor_data = []
    for doctor in doctors:
        lat2 = float(doctor.latitude)
        lon2 = float(doctor.longitude)
        # Approximate radius of earth in km
        R = 6373.0

        # lat1 = radians(lat1)
        # lon1 = radians(lon1)
        # lat2 = radians(lat2)
        # lon2 = radians(lon2)

        dlon = float(lon2) - float(longi)
        dlat = float(lat2) - float(lati)

        a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
        print(a)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        print(distance)
        doctor_data.append({
            'id': doctor.id,
            # 'idd': doctor.Login.id,
            'name': doctor.name,
            'phone': doctor.phone,
            'email': doctor.email,
            'image': request.build_absolute_uri(doctor.image.url),
            'latitude': str(doctor.latitude),
            'longitude': str(doctor.longitude),
            'distance': float(distance),

            })
        print(doctor_data)
    doctor_data.sort(key=lambda x: x['distance'])
    return JsonResponse({"status": "ok", "data": doctor_data})


# def driver_view_hospital(request):
#     doctors = hospital_table.objects.all()
#
#     if not doctors.exists():ctor.phone,
#     #         'email': doctor.email,
#     #         'image': request.build_absolute_uri(doctor.image.url),
#     #         'latitude': str(doctor.latitude),
#     #         'longitude': str(doctor.longitude),
#
#         return JsonResponse({"status": "ok", "data": []})
#
#     # doctor_data = []
#     # for doctor in doctors:
#     #     doctor_data.append({
#     #         'id': doctor.id,
#     #         'name': doctor.name,
#     #         'phone': do   #
#     #     })
#     # print(doctor_data)
#     # return JsonResponse({"status": "ok", "data": doctor_data})
#
#
#     doctor_data = []
#     for doctor in doctors:
#         lat2 = float(doctor.latitude)
#         lon2 = float(doctor.longitude)
#         # Approximate radius of earth in km
#         R = 6373.0
#
#         # lat1 = radians(lat1)
#         # lon1 = radians(lon1)
#         # lat2 = radians(lat2)
#         # lon2 = radians(lon2)
#
#         dlon = float(lon2) - float(longi)
#         dlat = float(lat2) - float(lati)
#
#         a = abs(sin(dlat / 2) * 2 + cos(lati) * cos(lat2) * sin(dlon / 2) * 2)
#         print(a)
#         c = 2 * atan2(sqrt(a), sqrt(1 - a))
#
#         distance = R * c
#         print(distance)
#         doctor_data.append({
#             'id': doctor.id,
#             # 'idd': doctor.Login.id,
#             'name': doctor.name,
#             'phone': doctor.phone,
#             'email': doctor.email,
#             'image': request.build_absolute_uri(doctor.image.url),
#             'latitude': str(doctor.latitude),
#             'longitude': str(doctor.longitude),
#             'distance': float(distance),
#
#         })
#     print(doctor_data)
#     doctor_data.sort(key=lambda x: x['distance'])
#     return JsonResponse({"status": "ok", "data": doctor_data})

def driver_view_report_accident(request):
    lid=request.POST['lid']
    accident = accidentreport_table.objects.filter(DRIVER__LOGIN_id=lid)
    doctor_data = []
    for ob in accident:
        doctor_data.append({
            'id': ob.id,
            'date': str(ob.date),
            'phone': str(ob.time),
            'email': ob.status,
            'latitude': str(ob.latitude),
            'longitude': str(ob.longitude),

        })
    print(doctor_data)
    return JsonResponse({"status": "ok", "data": doctor_data})


def driver_view_police(request):
    doctors = trafficpoolice_table.objects.all()

    if not doctors.exists():
        return JsonResponse({"status": "ok", "data": []})

    doctor_data = []
    for doctor in doctors:
        doctor_data.append({
            'id': doctor.id,
            'name': doctor.name,
            'place': doctor.place,
            'address': doctor.address,
            'image': request.build_absolute_uri(doctor.photo.url),
            'phone': str(doctor.phone),
            'designation': doctor.designation,
            'station': doctor.station,

        })
    print(doctor_data)
    return JsonResponse({"status": "ok", "data": doctor_data})


def drivercomplaint(request):
    did=request.POST['did']
    lid=request.POST['lid']
    Complaints=request.POST['Complaint']
    lob=complaint_table()
    lob.TRAFFICPOLICE_id=did
    lob.DRIVER=driver_table.objects.get(LOGIN__id=lid)
    lob.complaint=Complaints
    lob.reply='pending'
    from datetime import datetime
    lob.date=datetime.today().now()
    lob.save()
    return JsonResponse({"status": "ok"})


def viewcomplaintreply(request):
    lid = request.POST.get('lid')  # Get User ID from request
    ob = complaint_table.objects.filter(DRIVER__LOGIN__id=lid)

    mdata = []
    for i in ob:
        data = {
            'id': i.id,
            'complaint': i.complaint,
            'reply': i.reply,
            'date': str(i.date)
        }
        mdata.append(data)

    return JsonResponse({"status": "ok", "data": mdata})  # Corrected response


def viewemergency_accidentcase(request):
    lid = request.POST['lid']
    ob = emargency_table.objects.filter(AMBULANCE__LOGIN__id=lid).order_by("-id")

    mdata = []
    for i in ob:
        data = {
            'id': i.id,
            'ACCIDENT_latitude':str(i.ACCIDENTREPORT.latitude),
            'ACCIDENT_longitude':str(i.ACCIDENTREPORT.longitude),
            'ACCIDENT_date': str(i.ACCIDENTREPORT.date),
            'ACCIDENT_time': str(i.ACCIDENTREPORT.time),
            'status': i.status,
            'date': str(i.date)
        }
        mdata.append(data)

    return JsonResponse({"status": "ok", "data": mdata})  # Corrected response


def update_emergency(request):
    lid = request.POST['id']
    ob = emargency_table.objects.get(id=lid)
    ob.status="Processed"
    ob.save()
    oba=ob.ACCIDENTREPORT
    oba.status='Completed'
    oba.save()
    return JsonResponse({"status": "ok"})  # Corrected response




def delete_complaint(request):
    comp_id = request.POST.get('comp_id')

    try:
        complaint = complaint_table.objects.get(id=comp_id)
        complaint.delete()
        return JsonResponse({'status': 'ok', 'message': 'Complaint deleted successfully.'})
    except complaint_table.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Complaint not found.'})

def user_registrationcode(request):
    print(request.POST,'ppppppppppppppppppppppppppp')
    name = request.POST['name']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST['email']
    regno = request.POST['regno']
    username = request.POST['username']
    password = request.POST['password']
    photo = request.FILES['photo']


    fs=FileSystemStorage()
    fp=fs.save(photo.name,photo)

    lob1 = login_table()
    lob1.username = username
    lob1.password = password
    lob1.type = 'driver'
    lob1.save()

    lob = driver_table()
    lob.name = name
    lob.address = address
    lob.phone = phone
    lob.regno = regno
    lob.email = email
    lob.photo = fp
    lob.LOGIN = lob1
    lob.save()
    print("uuuuuuuuu", lob)
    return JsonResponse({'status': 'ok'})





def drivermanagerelation(request):
    lid=request.POST['lid']
    relation=request.POST['relation']
    number=request.POST['number']
    lob=emergency_number()
    lob.DRIVER=driver_table.objects.get(LOGIN__id=lid)
    lob.relation=relation
    lob.number=number
    lob.save()
    return JsonResponse({"status": "ok"})

def viewdrivermanagerelation(request):
    lid = request.POST.get('lid')  # Get User ID from request
    ob = emergency_number.objects.filter(DRIVER__LOGIN__id=lid)

    mdata = []
    for i in ob:
        data = {
            'id': i.id,
            'number': i.number,
            'relation': i.relation,
        }
        mdata.append(data)

    return JsonResponse({"status": "ok", "data": mdata})  # Corrected response
from math import radians, sin, cos, sqrt, atan2
from .sample import sendmessage
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Compute differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Apply Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    try:
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
    except:
        c = 2 * sqrt(a)

    # Compute distance
    distance = R * c
    return distance



def insert_emergency(request):
    print (request.POST)
    lat=request.POST['lat']
    lon=request.POST['lon']
    lid=request.POST['lid']

    obd=accidentreport_table.objects.filter(DRIVER__LOGIN__id=lid,date=datetime.today(),time__hour=datetime.now().hour)
    if len(obd)==0:
        obd= driver_table.objects.get(LOGIN__id=lid)
        ob=accidentreport_table()
        ob.DRIVER = driver_table.objects.get(LOGIN__id=lid)
        ob.latitude = lat
        ob.longitude = lon
        ob.date=datetime.today()
        ob.time=datetime.today()
        ob.status='pending'
        ob.type="pending"
        ob.save()
        msg="i am "+obd.name+" Emergency, locate me @ Help me http://maps.google.com?q="+lat+","+lon
        eob=emergency_number.objects.filter(DRIVER__LOGIN__id=lid)
        for i in eob:
            try:
             sendmessage(str(i.number),msg)
            except:
                pass
        obb=ambulance_table.objects.all()
        dis=-1
        cu=None
        for i in obb:
            try:

                res=location_table.objects.get(LOGIN__id=i.LOGIN.id)
                d=haversine(float(lat),float(lon),float(res.latitude),float(res.longitude))
                if dis==-1:
                    dis=d
                    cu=i
                if d<dis:
                    dis=d
                    cu=i

            except:
                pass

        obb=hospital_table.objects.all()
        dis=-1
        ch=None

        for i in obb:
            try:

                d=haversine(float(lat),float(lon),float(i.latitude),float(i.longitude))
                if dis==-1:
                    dis=d
                    ch=i
                if d<dis:
                    dis=d
                    ch=i
            except Exception as e:
                print(e)
                pass
        obn=emargency_table()
        obn.ACCIDENTREPORT=ob
        obn.HOSPITAL= ch
        obn.AMBULANCE= cu
        obn.status = 'pending'
        obn.time = datetime.today()
        obn.date =datetime.today()
        obn.save()

    return  JsonResponse({"status": "ok"})

