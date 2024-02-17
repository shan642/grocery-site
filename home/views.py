from django.shortcuts import render,redirect
from .models import user,product,cart

# Create your views here.
def home(request):
    return render(request,"home.html")
def signup(request,method=['GET','POST']):
    if request.method=='POST':
        email=request.POST.get("email")
        psw=request.POST.get("passw1")
        psw2=request.POST.get("passw2")
        user.objects.create(email=email,password=psw)
        return render(request,"login.html")

    return render(request,"signup.html")

def login(request,method=['GET','POST']):
    if request.method=='POST':
        email=request.POST.get("email")
        psw=request.POST.get("passw1")
        ob=user.objects.filter(email=email,password=psw)
        if(ob):
            return redirect("/product/")
        else:
            return render (request,"signup.html")
    return render(request,"login.html")

def products(request):
    ob=product.objects.all()
    return render(request,"product.html",{"ob":ob})

def carts(request,id):
    sum=0
    x=id
    item=product.objects.filter(id=x)
    print(item)
    items,created=cart.objects.get_or_create(item=item[0])
    if not created:
        items.quantity=items.quantity+1
        items.save()

    cartitems=cart.objects.all()
    for i in cartitems:
        sum=sum+i.quantity*i.item.price
    
    return render(request,"cart.html",{'cartitems':cartitems,'sum':sum})