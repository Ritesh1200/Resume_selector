from django.shortcuts import render
from django.views import View
from resume.models import Resume
import PyPDF2 
import docx

# Create your views here.

def doc_to_text(path):

    text = docx.Document("./resume/static/" +path)
    all_paras = text.paragraphs
    text_data = ""
    for para in all_paras:
        text_data = text_data + " "+para.text
    return text_data


def pdf_to_text(path):

    pdfFileObj = open("./resume/static/" +path, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pageObj = pdfReader.getPage(0)
    print(pageObj.extractText())
    print("this is pdf")
    return "this is pdf"

class Home(View):
    def get(self, request):
        return render(request, "resume/home.html") 

    def post(self, request):
        if len(request.FILES) != 0:
            resume = request.FILES['resume']
        resume_obj = Resume(username= request.POST.get("username"), resume= resume)
        resume_obj.save()
         
        key_works = set(("c", "java", "sql", "python", "django"))

        path = request.POST.get("username") + str(resume)
        value =str(resume).split('.')
        print(value[len(value)-1])

        if value[len(value)-1] == "pdf":
            data = pdf_to_text(path)
        if value[len(value)-1] == "docx":
            data = doc_to_text(path)

        data = data.split()
        matches = 0
        for word in data: 
            if word.lower() in key_works:
                matches = matches + 1
        
        response = ""
        if matches > 3:
            response = "user has a good resume"
        else:
            response = "user must practice more"
        return render(request, "resume/home.html", {"response":response})