from django.shortcuts import render
from django.http import HttpResponse


def showTest(request):
    #s="<h1><b><u>This is a test page</u></b></h1>"
    #return HttpResponse(s)
    que="Who developed C language?"
    a="Ken Theampson"
    b="Dennis Ritchie "
    c="Bjarne Stroustroup"
    d="James Gosling"
    dataindict={'QUE':que,'A':a,'B':b,'C':c,'D':d}

    res=render(request,'exam/test.html',context=dataindict)
    return res
def showResult(request):
    s="<h1><b>This is a result page</b></h1>"
    return HttpResponse(s)


# Create your views here.
