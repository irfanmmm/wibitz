import json
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from web.models import Creators,Subscribe,Futiuersection,Creatvedeo,Partners,Marketting,Solution,Resources
from web.form import ContactForm

def index(request):

    creators = Creators.objects.all()

    latest_creators = Creators.objects.all()[:4]



    futiuersection = Futiuersection.objects.all()

    creatvedeo = Creatvedeo.objects.all()

    partner = Partners.objects.all()

    marketting = Marketting.objects.all()

    solution = Solution.objects.all()

    resources = Resources.objects.all()

    form = ContactForm()

    

    
    return render(request,"index.html",context = {
        "creators": creators,
        "futiuersection": futiuersection,
        "creatvedeo": creatvedeo,
        "partner": partner,
        "marketting": marketting,
        "solution": solution,
        "resources": resources,
        "form": form,
        "latest_creators": latest_creators,
    } )


def subscribe(request):
    # POST = elladatasum ithilan
    email = request.POST.get("email")

    if not Subscribe.objects.filter(email=email).exists():


        Subscribe.objects.create(
        email = email
        )
        responsdata = {
            "status" : "success",
            "title":"Successfully Registerd",
            "message" : "Thank you for subscribing"
        }
    else :
        responsdata = {
            "status" : "error",
            "title":"You are already registerd",
            "message" : "You are alredy a member"
        }
    #  submit button click cheythal ed pagilekk redirect cheyyanam enn an
    return HttpResponse(json.dumps(responsdata),content_type="application/javascript")



def contact(request):

    # all datasum ithilund
    form = ContactForm(request.POST)

    if form.is_valid():
        form.save()

        responsdata = {
            "status" : "success",
            "title":"Successfully Registerd",
            "message" : "Thank you for subscribing"
        }
    else:
        responsdata = {
            "status" : "error",
            "title":"You are already registerd",
            "message" : "You are alredy a member"
        }

    return HttpResponse(json.dumps(responsdata),content_type="application/javascript")
#   pk (,pk) -> add cheyyanam same name avanam
def product(request,pk):
    #  Error filtr cheyyunnu -> programin Error kittilla
    product = get_object_or_404(Solution.objects.filter(pk=pk))

    customers = Creators.objects.filter(product=product)

    context = {
        "product":product,
        "customers":customers
    }
    return render(request,"product.html", context=context)






    