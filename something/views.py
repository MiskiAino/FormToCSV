from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Document
from .models import Person
import csv
from pwgen import pwgen
from .models import UploadFile
from .forms import UploadFileForm



def gen(request):


    if request.method == 'POST':
        document = Document()
        document.name = request.POST['name']
        document.urlDownload = "/files/"+request.POST['name'] + ".csv"
        document.save()
        my_file = open( "static/files/"+request.POST['name'] + ".csv", 'w')  #создание файла
        my_file.close()

    doc = Document.objects.latest('id')
    upload = UploadFile.objects.latest('id')
    form = UploadFileForm()



    return render(request, 'index.html',locals())



def translit(s):
    """translit string 's' from russian to english"""
    dic = {'а': 'a',
           'б': 'b',
           'в': 'v',
           'г': 'g',
           'д': 'd',
           'е': 'e',
           'ё': 'yo',
           'ж': 'zh',
           'з': 'z',
           'и': 'i',
           'й': 'i',
           'к': 'k',
           'л': 'l',
           'м': 'm',
           'н': 'n',
           'о': 'o',
           'п': 'p',
           'р': 'r',
           'с': 's',
           'т': 't',
           'у': 'u',
           'ф': 'f',
           'х': 'h',
           'ц': 'c',
           'ч': 'ch',
           'ш': 'sh',
           'щ': 'sch',
           'ъ': '_',
           'ы': 'y',
           'ь': '_',
           'э': 'e',
           'ю': 'yu',
           'я': 'ya',
           '\n': ''}
    for c in dic:
        s = s.replace(c, dic[c])
    return s


def add(request):


    if request.method == 'POST':
        docE = Document.objects.get(id=request.POST['key'])
        doc = docE.name
        person = Person()
        person.FIO = request.POST['data']
        person.file =  docE
        person.save()
        persons = Person.objects.filter(file=docE)



        try:
            with open("static/files/"+doc+".csv", 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                for psn in persons:

                    lines = psn.FIO.split("\n")


                    for line in lines:
                        password = pwgen(10, symbols=False)
                        word = line.split()
                        username = doc + translit(word[0].lower())
                        email = username + '@prk.local'
                        spamwriter.writerow([username]+[password]+[word[0]]+[word[1]]+[email])
        except:
            pass



    return HttpResponseRedirect("/",locals())




def upload(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file = UploadFile()
        file.upload = request.FILES['upload']
        file.download = file.upload.name +".csv"
        file.save()
    #
    doc = UploadFile.objects.latest('id').upload
    print(doc)
    # with open("static/files/"+doc, 'w', newline='') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    f = open('static/media/'+doc.name)







    with open("static/media/"+doc.name+".csv", 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for line in f:
            print(line)
            password = pwgen(10, symbols=False)
            word = line.split()
            username = doc.name + translit(word[0].lower())
            email = username + '@prk.local'
            spamwriter.writerow([username]+[password]+[word[0]]+[word[1]]+[email])









    return HttpResponseRedirect("/",locals())
