from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.

def Home(request):
    return HttpResponse("Welcome to Home page")
def text(request):
    return render(request,"text.html")

def analyze(request):

    if request.method=="GET":
        
        text=request.GET["text"]
        lowercase=request.GET.get("lowercase","off")
        uppercase=request.GET.get("uppercase","off")
        remove_punc=request.GET.get("removepunc","off")
        title_case=request.GET.get("title","off")
        charcount=request.GET.get("charcount","off")
        remove_line=request.GET.get("removeline","off")
      
        convert_list=" {2,10}"
        replace="\n\n"
        text=re.sub(convert_list,replace,text)
        
        '''def countLetters_Digit_Only(msg):
            length = 0
            for i in msg:
                if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
                   length += 1
            return length'''

        def count_Letters_Digit_special(msg):
            special_char=[33,34,35,36,37,38,39,40,41,42,44,45,58,59,60,62,63,64,91,93,94,95,123,124,125,126]
            length = 0
            for i in msg:
                if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57) or ( ord(i) in special_char ):
                   length += 1
            return length
        def punc(msg):
            punc_list=["!","@","#","%","$","^","&","*","(",")","-","_","=","|"," ' ",' " ',";",":",",","?","<",">","/","\n" ]
            punc_text=""
            for i in msg:
                if i not in punc_list:
                    punc_text=punc_text+i
            return punc_text  
        def removeline(msg):
            remove_list=["\n"]
            remove_line_text=""
            for i in msg:
                if i not in remove_list:
                    remove_line_text=remove_line_text+i
                else:
                    remove_line_text=remove_line_text+" "
            return remove_line_text
        def convert_line(msg):
            convert_list=["  "]
            convert_line_text=""
            for i in msg:
                if i not in convert_list:
                   convert_line_text=convert_line_text+i
            else:
                convert_line_text=convert_line_text+ "\n"
            return convert_line_text   

        if(remove_punc=="on" and remove_line=="on"):
            context={"remove_punc":remove_punc,"remove_line":remove_line}
            return render(request,"analyzed.html", context)
        elif(remove_punc=="on"):
            antext=punc(text)
            if((lowercase=="on") and (uppercase=="on") and (title_case=="on")):
                context={"lowercase":lowercase,"remove_punc":remove_punc,"uppercase":uppercase,"title_case":title_case}
                return render(request,"analyzed.html", context)
            elif((lowercase=="on" and title_case=="on") or (uppercase=="on" and title_case=="on") or (uppercase=="on" and lowercase=="on")):
                context={"lowercase":lowercase,"remove_punc":remove_punc,"uppercase":uppercase,"title_case":title_case}
                return render(request,"analyzed.html", context)
            elif(lowercase=="on"):
                antext=antext.lower()
                if(charcount=="on"):
                    count=count_Letters_Digit_special(antext)
                    context={"text":text,"lowercase":lowercase,"remove_punc":remove_punc,"charcount":charcount,"count":count,"antext":antext}
                    return render(request,"analyzed.html", context)
                else:
                    context={"text":text,"lowercase":lowercase,"remove_punc":remove_punc,"antext":antext}
                    return render(request,"analyzed.html", context)
            elif(uppercase=="on"):
                antext=antext.upper()
                if(charcount=="on"):
                    count=count_Letters_Digit_special(antext)
                    context={"text":text,"uppercase":uppercase,"remove_punc":remove_punc,"charcount":charcount,"count":count,"antext":antext}
                    return render(request,"analyzed.html", context)
                else:
                    context={"text":text,"uppercase":uppercase,"remove_punc":remove_punc,"antext":antext}
                    return render(request,"analyzed.html", context)
            elif(title_case=="on"):
                antext=antext.title()
                if(charcount=="on"):
                    count=count_Letters_Digit_special(antext)
                    context={"text":text,"title_case":title_case,"remove_punc":remove_punc,"charcount":charcount,"count":count,"antext":antext}
                    return render(request,"analyzed.html", context)
                else:
                    context={"text":text,"title_case":title_case,"remove_punc":remove_punc,"antext":antext}
                    return render(request,"analyzed.html", context)
            elif(charcount=="on"):
                count=count_Letters_Digit_special(antext)
                context={"text":text,"remove_punc":remove_punc,"charcount":charcount,"count":count,"antext":antext}
                return render(request,"analyzed.html", context)
            else:
                context={"text":text,"remove_punc":remove_punc,"antext":antext}
                return render(request,"analyzed.html", context)
        elif((lowercase=="on") and (uppercase=="on") and (title_case=="on")):
                context={"lowercase":lowercase,"uppercase":uppercase,"title_case":title_case}
                return render(request,"analyzed.html", context)
        elif((lowercase=="on" and title_case=="on") or (uppercase=="on" and title_case=="on") or (uppercase=="on" and lowercase=="on")):
                context={"lowercase":lowercase,"uppercase":uppercase,"title_case":title_case}
                return render(request,"analyzed.html", context)
        elif(lowercase=="on"):
            antext=text.lower()
            if(remove_line=="on" and charcount=="on"):
                text=convert_line(text)
                antext=removeline(antext)
                count=count_Letters_Digit_special(antext)
                context={"lowercase":lowercase,"remove_line":remove_line,"charcount":charcount,"count":count,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
            elif(remove_line=="off" and charcount=="on"):
                count=count_Letters_Digit_special(antext)
                context={"lowercase":lowercase,"remove_line":remove_line,"charcount":charcount,"count":count,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
            elif(remove_line=="on" and charcount=="off"):
                antext=removeline(antext)
                context={"lowercase":lowercase,"remove_line":remove_line,"charcount":charcount,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
            else:
                context={"lowercase":lowercase,"remove_line":remove_line,"charcount":charcount,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
        elif(uppercase=="on"):
            antext=text.upper()
            if(remove_line=="on" and charcount=="on"):
                antext=removeline(antext)
                count=count_Letters_Digit_special(antext)
                context={"uppercase":uppercase,"remove_line":remove_line,"charcount":charcount,"count":count,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
            elif(remove_line=="off" and charcount=="on"):
                count=count_Letters_Digit_special(antext)
                context={"uppercase":uppercase,"remove_line":remove_line,"charcount":charcount,"count":count,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
            elif(remove_line=="on" and charcount=="off"):
                antext=removeline(antext)
                context={"uppercase":uppercase,"remove_line":remove_line,"charcount":charcount,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
            else:
                context={"uppercase":uppercase,"remove_line":remove_line,"charcount":charcount,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
        elif(title_case=="on"):
            antext=text.title()
            if(remove_line=="on" and charcount=="on"):
                antext=removeline(antext)
                count=count_Letters_Digit_special(antext)
                context={"title_case":title_case,"remove_line":remove_line,"charcount":charcount,"count":count,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
            elif(remove_line=="off" and charcount=="on"):
                count=count_Letters_Digit_special(antext)
                context={"title_case":title_case,"remove_line":remove_line,"charcount":charcount,"count":count,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
            elif(remove_line=="on" and charcount=="off"):
                antext=removeline(antext)
                context={"title_case":title_case,"remove_line":remove_line,"charcount":charcount,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
            else:
                context={"title_case":title_case,"remove_line":remove_line,"charcount":charcount,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
        elif(remove_line=="on" and charcount=="on"):
            antext=removeline(text)
            count=count_Letters_Digit_special(antext)
            context={"remove_line":remove_line,"charcount":charcount,"count":count,"text":text,"antext":antext}
            return render(request,"analyzed.html", context)
        elif(remove_line=="on"and charcount=="off"):
                antext=removeline(text)
                context={"remove_line":remove_line,"charcount":charcount,"text":text,"antext":antext}
                return render(request,"analyzed.html", context)
        elif(remove_line=="off"and charcount=="on"):
                count=count_Letters_Digit_special(text)
                context={"remove_line":remove_line,"charcount":charcount,"count":count,"text":text}
                return render(request,"analyzed.html", context)
        else:
            return render(request,"analyzed.html", context={"Oneaction":"Select At lease one action"})
    else:
         return HttpResponse("ERROR")
    
      