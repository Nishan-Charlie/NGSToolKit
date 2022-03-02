from pyexpat.errors import messages
from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm

# Create your views here.
def home(request):
    return render(request, "home.html")

# CSV file upload
def csv_file(request):
    if request.method =="POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploadedfile = request.FILES['Document']
            fileName = uploadedfile.name
            fileSize = uploadedfile.size
            fs = FileSystemStorage()    #Creating an object
            fs.save(fileName, uploadedfile)
            return HttpResponseRedirect('/visualize/')
        else:
            form = UploadFileForm()
        
    return render(request, "upload.html", {'form': form})

#CSV file Visualize
def visualize(request):
    return 2
