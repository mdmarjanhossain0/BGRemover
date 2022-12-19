from django.shortcuts import render, redirect


from .form import ImageForm
from .models import Image

# from workermodule.djconnetinginterface import cutout


# Create your views here.
def index(request):

    # if request.method == "POST":
    #     form=ImageForm(data=request.POST, files=request.FILES)

    #     if form.is_valid():
    #         form.save()
    #         obj=form.instance
    #         path=obj.image.url

    #         cutout(path)
    #         return render(request,"index.html",{"obj":obj})
    # else:
    #     form=ImageForm()
    #     img=Image.objects.all()
    return render(request, "index.html", {})
