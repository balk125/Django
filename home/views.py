from multiprocessing import context
from django.shortcuts import redirect, render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    v1=request.GET.get('textare','default')
    v2=request.GET.get('name','default')
    v3=request.GET.get('email','default')
    check_punctuation =request.GET.get('check_punctuation','off')
    check_captalize=request.GET.get('check_captalize','off')
    check_newline=request.GET.get('check_newline','off')
    check_extraspace=request.GET.get('check_extraspace','off')
    # print(v1)
    # print(v2)
    # print(v3)
    
    context={
        'var_name':v2,
        'var_email':v3,
        'message':""

    }
    # if v4!='on':
    #     return redirect('/')
    if check_punctuation=="on":

        punct='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analized=""
        for char in v1:
            if char not in punct:
                analized=analized+char
        context['message']='Your decided task : To remove Punctuation'

        context['analized_text']=analized
            
        
        return render(request,'about.html',context)

    elif check_captalize=="on":
        analized=""
        for char in v1:
            analized=analized + char.upper()
        context['message']='Your decided task : To convert into  Uppercase'
        context['analized_text']=analized
        return render(request,'about.html',context)

    elif check_newline=="on":
        analized=""
        for char in v1:
            if char!="\n":
                analized=analized + char
        context['message']='Your decided task : To Remove New Line'
        context['analized_text']=analized
        return render(request,'about.html',context)
    elif check_extraspace=="on":
        analized=""
        for index, char in enumerate(v1):
            try:
                if v1[index]==" " and v1[index+1]==" ":
                    continue
                else:
                    analized=analized + char
            except Exception as e:
                continue

        context['message']='Your decided task : To Remove Extra Space'
        context['analized_text']=analized

    return render(request,'about.html',context)





        







    
def contact(request):
    return render(request,'contact.html')





# def index(request):
#     return HttpResponse('''<h1> this is kanhaiya</h1>
#     <iframe width="560" height="315" src="https://www.youtube.com/embed/ES-bdt0KUZg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>''')
