from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
import matplotlib.pyplot as plt
import urllib,base64
import io
import math
import numpy as np
#it is programme for simple ptoting the circle.user enter the radious of the r=16
#def relation(request):
def home(request):
    #R=str(request.GET.get('number'))
    r=16
    rad=math.sqrt(r)
    plt.axis([-rad,rad,-rad,rad])
    r1=[]
    r2=[]
    angle=0
    while(angle<=360):
        delta=angle
        delta=math.radians(delta)
        r1.append(rad*math.cos(delta))
        r2.append(rad*math.sin(delta))
        angle+=10
        #what is the designing an os
    plt.axes().spines['bottom'].set_position(('data' , 0))
    fig=plt.gcf()
    plt.axes().spines['left'].set_position(('data' ,0))
    fig=plt.gcf()
    plt.axhline(y=-rad)
    fig=plt.gcf()
    plt.axvline(x=-rad)
    fig=plt.gcf()
    #it is the function for printing the data on browser
    #it is function for printing two garph one for circle and another one for line.
    plt.plot(r1,r2,color='g')
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    return render(request,'home.html', {'data':uri})


