from django.http import HttpResponse
from django.shortcuts import render
from Meddonor import connect
# Create your views here.

#login
def login1(request):
    s1=request.POST["t1"]
    s2=request.POST["t2"]
    con=connect()
    cursor=con.cursor()
    s="select * from login where userid='"+s1+"' and password='"+s2+"'"
    cursor.execute(s)
    if cursor.rowcount==0:
        msg="Invalid Id and Password"
        return render(request,"home.html",{'msg':msg})
    else:
        if s1=="admin":
            return render(request,"adprocess.html")
        else:
            x=s1[0]
            if x=="S" or x=="s":
                import socket
                hostname=socket.gethostname()
                ip=socket.gethostbyname(hostname)
                s="delete from session where ip='"+ ip +"'"
                cursor.execute(s)
                con.commit()
                s="insert into session values('"+  s1 + "','"+ ip   + "')"
                cursor.execute(s)
                con.commit()
                return render(request,"adstaffprocess.html")
            else:
                return HttpResponse("Another User Logging In")


def home(request):
    return render(request, "home.html")

#registrations
def guestreg(request):
    return render(request,"guestreg.html")
#ngo
def ngoreg1(request):
    return render(request,"ngoreg.html")
def ngoreg2(request):


    return render(request,"ngoreg1.html")


#orphanage
def orpreg1(request):
    return render(request,"orphanagereg.html")
