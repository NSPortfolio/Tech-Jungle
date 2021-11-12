from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings
from app import forms
from app.models import Post
from django.core.mail import send_mail

def firstpage(request):
    return render(request,'home.html')

@login_required()
def home(request):
    return render(request, 'home.html')

@login_required()
def email(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'POST':
        tocontact = request.POST.get("to")
        subject = request.POST.get("subject")
        message = request.POST.get("message") + "\nContact Buyer " + request.user.email
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [tocontact],
        )
        return redirect('/buy/')
    return render(request, 'email.html')

@login_required()
def buy(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                      'searchbutton': searchbutton}
            return render(request, 'buy.html', context)
        else:
            ship = Post.objects.filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'buy.html', context)

@login_required()
def computer(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='1').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='1').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='1').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                      'searchbutton': searchbutton}
            return render(request, 'tabs/computer.html', context)
        else:
            ship = Post.objects.filter(category='1').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='1').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='1').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/computer.html', context)

@login_required()
def camera(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='2').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='2').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='2').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                      'searchbutton': searchbutton}
            return render(request, 'tabs/camera.html', context)
        else:
            ship = Post.objects.filter(category='2').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='2').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='2').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/camera.html', context)

@login_required()
def tablet(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='3').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='3').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='3').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/tablet.html', context)
        else:
            ship = Post.objects.filter(category='3').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='3').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='3').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/tablet.html', context)

@login_required()
def watch(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='4').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='4').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='4').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/watch.html', context)
        else:
            ship = Post.objects.filter(category='4').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='4').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='4').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/watch.html', context)

@login_required()
def phone(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='5').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='5').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='5').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/phone.html', context)
        else:
            ship = Post.objects.filter(category='5').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='5').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='5').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/phone.html', context)

@login_required()
def ereader(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='6').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='6').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='6').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/ereader.html', context)
        else:
            ship = Post.objects.filter(category='6').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='6').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='6').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/ereader.html', context)

@login_required()
def storagedevice(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='7').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='7').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='7').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/storagedevice.html', context)
        else:
            ship = Post.objects.filter(category='7').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='7').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='7').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/storagedevice.html', context)

@login_required()
def projector(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='8').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='8').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='8').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/projector.html', context)
        else:
            ship = Post.objects.filter(category='8').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='8').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='8').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/projector.html', context)

@login_required()
def speaker(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='9').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='9').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='9').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/speaker.html', context)
        else:
            ship = Post.objects.filter(category='9').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='9').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='9').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/speaker.html', context)

@login_required()
def headphoneearbud(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='10').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='10').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='10').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/headphoneearbud.html', context)
        else:
            ship = Post.objects.filter(category='10').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='10').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='10').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/headphoneearbud.html', context)

@login_required()
def microphone(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='11').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='11').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='11').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/microphone.html', context)
        else:
            ship = Post.objects.filter(category='11').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='11').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='11').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/microphone.html', context)

@login_required()
def printer(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='12').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='12').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='12').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/printer.html', context)
        else:
            ship = Post.objects.filter(category='12').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='12').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='12').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/printer.html', context)

@login_required()
def mice(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='13').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='13').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='13').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/mice.html', context)
        else:
            ship = Post.objects.filter(category='13').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='13').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='13').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/mice.html', context)

@login_required()
def keyboard(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='14').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='14').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='14').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/keyboard.html', context)
        else:
            ship = Post.objects.filter(category='14').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='14').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='14').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/keyboard.html', context)

@login_required()
def appliances(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    if request.method == 'GET':
        query = request.GET.get('searchforelectronics')
        searchbutton = request.GET.get('submit')
        if query is not None:
            shipsearch = Post.objects.filter(category='15').filter(name_of_product__icontains=query).filter(pickuporship="Shipping Only").order_by('-created_at')
            pickshipsearch = Post.objects.filter(category='15').filter(name_of_product__icontains=query).filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')
            pickupsearch = Post.objects.filter(category='15').filter(name_of_product__icontains=query).filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')
            context = {'shipsearch': shipsearch,
                       'pickshipsearch': pickshipsearch,
                       'pickupsearch': pickupsearch,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/appliances.html', context)
        else:
            ship = Post.objects.filter(category='15').filter(pickuporship="Shipping Only").order_by('-created_at')[:5]
            pickship = Post.objects.filter(category='15').filter(pickuporship="Both Pick Up and Shipping").order_by('-created_at')[:5]
            pickup = Post.objects.filter(category='15').filter(pickuporship="Pick Up Only").filter(city=current_seller.pickup_area).order_by('-created_at')[:5]
            context = {'ship': ship,
                       'pickship': pickship,
                       'pickup': pickup,
                       'searchbutton': searchbutton}
            return render(request, 'tabs/appliances.html', context)

@login_required()
def editpost(request, name_of_product):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    edit = Post.objects.filter(email=request.user.email).get(name_of_product=name_of_product)
    sell_form = forms.ItemsCreateForm(request.POST or None, instance=edit)
    if sell_form.is_valid():
        sell_form.save()
        return redirect('/sell/')
    return render(request, 'editpost.html', {
        "edit": edit,
        "sell_form": sell_form,
    })

@login_required()
def deletepost(request, name_of_product):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    delete = Post.objects.filter(email=request.user.email).get(name_of_product=name_of_product)
    delete.delete()
    return redirect('/sell/')

@login_required()
def sell(request):
    myposts = Post.objects.filter(email=request.user.email).order_by('-created_at')
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    sell_form = forms.ItemsCreateForm()
    if request.method == "POST":
        if request.POST.get('step') == '1':
            sell_form = forms.ItemsCreateForm(request.POST, request.FILES)
            if sell_form.is_valid():
                creating_post = sell_form.save(commit=False)
                creating_post.email = request.user.email
                creating_post.city = creating_post.city.lower()
                creating_post.city = creating_post.city.replace(" ", "")
                creating_post.save()
                return redirect('/sell/')
    return render(request, 'sell.html', {
        "sell_form": sell_form,
        "myposts": myposts,
    })


@login_required()
def profile(request):
    current_customer = request.user.seller
    user_form = forms.BasicUserForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)
    pickup_form = forms.Pickup()
    if request.method == 'POST':
        if request.POST.get('action') == 'update_profile':
            user_form = forms.BasicUserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Your profile has been updated.')
                return redirect('/profile/')
        elif request.POST.get('action') == 'update_pickup_area':
            pickup_form = forms.Pickup(request.POST, instance=current_customer)
            if pickup_form.is_valid():
                pickup_form = pickup_form.save(commit=False)
                pickup_form.pickup_area = pickup_form.pickup_area.lower()
                pickup_form.pickup_area = pickup_form.pickup_area.replace(" ", "")
                pickup_form.save()
                messages.success(request,'Your area has been updated.')
                return redirect('/profile/')
        elif request.POST.get('action') == 'update_password':
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request,user)
                messages.success(request, 'Your profile has been updated.')
                return redirect('/profile/')
    return render(request, 'profile.html', {
        "user_form": user_form,
        "password_form": password_form,
        "pickup_form": pickup_form,
    })


def sign_up(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.save(commit=False)
            user.username = email
            user.save()
            login(request, user)
            return redirect('/home/')
    return render(request, 'sign_up.html', {
        'form': form
    })

@login_required()
def removeitem(request, name_of_product):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    post = Post.objects.get(name_of_product=name_of_product)
    if post.saved.filter(id=request.user.id).exists():
        post.saved.remove(request.user)
    else:
        return redirect('/saveditems/')
    return redirect('/saveditems/')

@login_required()
def saveitem(request, name_of_product):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    post = Post.objects.get(name_of_product=name_of_product)
    if post.saved.filter(email=request.user.email).exists():
        return redirect('/saveditems/')
    else:
        post.saved.add(request.user)
    return redirect('/saveditems/')

@login_required()
def SavedItems(request):
    current_seller = request.user.seller
    if not current_seller.pickup_area:
        return redirect('/profile/')
    user = request.user
    saved_posts = user.saved.all()
    return render(request, 'saveditems.html', {
        "saved_posts": saved_posts,
    })
