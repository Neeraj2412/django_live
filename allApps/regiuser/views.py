from allApps.regiuser.models import userProfiles
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import CreateUserForm,CreateSellerForm, profileForm, sellerProfileForm
from .productForm import herbProductForm
from django.contrib.auth import authenticate, login , logout
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    allproducts = herbProduct.objects.all()
    context = {'allpro':allproducts}
    return render(request, 'index.html', context)

def signuppg(request):
    form = CreateUserForm()
    form2 = profileForm()
    formseller = CreateSellerForm(request.POST)
    from2Seller = sellerProfileForm(request.POST)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = profileForm(request.POST)
        formseller = CreateSellerForm(request.POST)
        from2Seller = sellerProfileForm(request.POST)
        if form.is_valid() and form2.is_valid():
            #this part is important here we are doing multiple tasks
            user =  form.save() #saving userform in the user variable
            profile = profileForm().save(commit=False) #here we are saving the profileForm in profile but commit=False means
                                                     #the form is not saved in database but in profile variable
            profile.user = user                      #here we are refering to the OnToOneField with User
                                                      #here we are saving the form
            profile.phone = request.POST.get("phone", '')
            profile.address = request.POST.get("address", '')
            profile.save()
            # form2.save()     
            return redirect('home')

        elif formseller.is_valid() and from2Seller.is_valid():
            userSeller = formseller.save()
            profileSeller = sellerProfileForm(request.POST).save(commit=False)
            profileSeller.userSeller = userSeller
            profileSeller.phoneSeller = request.POST.get("phoneSeller", '')
            profileSeller.addressSeller = request.POST.get("addressSeller", '')
            profileSeller.save()

    context = {'form':form, 'form2':form2, 'formseller':formseller, 'form2seller':from2Seller}
    return render(request, 'signup.html', context)


def loginpg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        usernameSeller = request.POST.get('usernameSeller')
        passwordSeller = request.POST.get('passwordSeller')
        userSeller = authenticate(request, username=usernameSeller, password=passwordSeller)

        if user is not None:
            userId = user.id 
            if userProfiles.objects.filter(user_id= userId).exists():
                login(request, user)
                return redirect('home')

            elif sellerProfile.objects.filter(userSeller_id = userId).exists():
                messages.info(request, "Please LogIn Through Seller's Portal")
                # return redirect('login')

        elif userSeller is not None:
            userSellerId = userSeller.id 
            if userProfiles.objects.filter(user_id= userSellerId).exists():
                messages.info(request, "Please LogIn Through Users's Portal")

            elif sellerProfile.objects.filter(userSeller_id = userSellerId).exists():
                login(request, userSeller)
                return redirect('sellerPortal')

        else:
            messages.info(request, 'Username Or Passcode Is Incorrect')

    return render(request, 'login.html' )

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def sellerPage(request):
    productPageForm = herbProductForm()
    if request.method == 'POST':
        productPageForm = herbProductForm(request.POST)
        if productPageForm.is_valid():
            productProfile = herbProductForm().save(commit=False)
            sellername = request.user.sellerProfile
            productProfile.sellername = sellername
            productProfile.productName = request.POST.get("productName", '')
            productProfile.productImage = request.FILES.get("productImage", '')
            productProfile.productPrice = request.POST.get("productPrice", '')
            productProfile.productDesc = request.POST.get("productDesc", '')
            productProfile.save()


    seePro = request.user.sellerProfile
    allProduct = herbProduct.objects.filter(sellername = seePro).all()

    context = {'form':productPageForm, 'pro':allProduct}
    return render(request, 'sellerPortal.html', context)
# userprof = sellerProfile.objects.all()    
# print(userprof.phoneSeller)
# print(User.objects.all())



    