# I have created this file - Shubham
from django.http import HttpResponse
from django.shortcuts import render


nav = '''<html>
<head><title> Exercise 1 </title></head>
<body>
<table border="5" cellpadding="12" cellspacing="5" frames="border" height="80" width="65">
<marquee behavior="scroll" direction="right" scrollamount="10">
<caption style="white-space:nowrap;overflow:hidden"> <h1>Personal Navigator</h1> </caption>
</marquee>
<tr>
<th> Sl. No. </th>
<th> Website Name </th>
</tr>
<td>1</td>
<td><a href="https://www.google.co.in" target = _blank> Google_NewTab </a><br></td>
</tr>
<tr>
<td>2</td>
<td><a href="https://www.google.co.in"> Google </a><br></td>
</tr>
</table>
<br>
<div style="display:flex;"><a href="/removepunc" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;
border-radius:10px;color:white;">Remove Punctuation</a>
<a href="/capitalfirst" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;
border-radius:10px;color:white;">Capitalize First</a>
<a href="/newlineremove" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;
border-radius:10px;color:white;">Remove New Line</a>
<a href="/spaceremove" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;
border-radius:10px;color:white;">Remove Space</a>
<a href="/charcount" style="text-decoration:none;padding:13px 25px;margin-right:30px;background:#E74C3C;
border-radius:10px;color:white;">Character Counter</a>
</div>
</body>
</html>'''

# def index(request):
#     return HttpResponse('<h1>Hello World!</h1> <a href="https://www.google.co.in"> Google </a>')

def index(request):
    dict = {'name':'Shubham','place':'Mars'}
    return render(request,'index.html',dict)                        #dict is used to pass variables to teamplate
     #return HttpResponse(nav)


def readFile(request):
    f=open('D:/Shubham/PyCharm/Django/textutils/testFile.txt','r')
    fileContent=f.read()
    f.close()
    return HttpResponse(fileContent,content_type="text/plain")

def about(request):
    return HttpResponse("About Section")

def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    email=request.POST.get('email','default')
    query = request.POST.get('query', 'default')
    print(email)
    print(query)
    return render(request, 'contactus.html')

def textanalyze(request):
    return render(request,'textAnalyze.html')

def removepunc(request):
    #Get the text
    textRet=request.POST.get('text', 'default')

    #Check checkbox values
    removepunc=request.POST.get('removepunc','off')
    allcaps = request.POST.get('allcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charcounter=request.POST.get('charcounter', 'off')

    print(newlineremover)
    print(textRet)

    #Analyze the text
    #analyzed=textRet
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in textRet:
            if char  not in punctuations:
                analyzed=analyzed+char
        removepunc="off"
        params={'purpose':'Punctuation Removed','analyzed_text':analyzed}
        textRet=analyzed
        #return render(request,'rempunc.html',params)
    if allcaps=="on":
        analyzed=""
        for char in textRet:
            analyzed=analyzed+char.upper()

        params = {'purpose': 'All UPPERCASE', 'analyzed_text': analyzed}
        textRet = analyzed
        #return render(request, 'rempunc.html', params)
    if newlineremover=="on":
        analyzed=""
        for char in textRet:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'New Lines Removed', 'analyzed_text': analyzed}
        textRet = analyzed
        #return render(request, 'rempunc.html', params)
    if extraspaceremover=="on":
        analyzed=""
        for ind,char in enumerate(textRet):
            if not (textRet[ind-1]==" " and textRet[ind]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        textRet = analyzed
        #return render(request, 'rempunc.html', params)
    if charcounter=="on":
        analyzed=""
        #for ind,char in enumerate(textRet):
            #analyzed = ind
        analyzed=f"Total number of characters in the final string are: {len(textRet)} \r\nAnalyzed text: {textRet}."
        params = {'purpose': 'Characters Counted', 'analyzed_text': analyzed}
        #return render(request, 'rempunc.html', params)
    if(removepunc!="on" and allcaps!="on" and newlineremover!="on" and extraspaceremover!="on" and charcounter!="on"):
        return HttpResponse("Error!")

    return render(request, 'rempunc.html', params)

def capitalfirst(request):
    return HttpResponse('''<h1>Capitalize First</h1><br><br><br><a href="/" style="text-decoration:none;padding:13px 25px;margin-right:30px;
    background:#E74C3C;border-radius:10px;color:white">Home</a>''')

def newlineremove(request):
    return HttpResponse('''<h1>New Line Remover</h1><br><br><br><a href="/" style="text-decoration:none;padding:13px 25px;margin-right:30px;
    background:#E74C3C;border-radius:10px;color:white">Home</a>''')

def spaceremove(request):
    return HttpResponse('''<h1>Space Remover</h1><br><br><br><a href="/" style="text-decoration:none;padding:13px 25px;margin-right:30px;
    background:#E74C3C;border-radius:10px;color:white">Home</a>''')

def charcount(request):
    return HttpResponse('''<h1>Character Counter</h1><br><br><br><a href="/" style="text-decoration:none;padding:13px 25px;margin-right:30px;
    background:#E74C3C;border-radius:10px;color:white">Home</a>''')