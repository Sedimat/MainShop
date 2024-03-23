from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import UserRegistrationForm
from .models import UserProfile, Products, ProductKeys, UserBuying, Rules, FAQ


# Create your views here.
def index(request):
    context = {}
    if request.user.username:
        user = User.objects.get(username=request.user.username)
        context.update({"user": user})
    products = Products.objects.all()
    context.update({"products": products})

    return render(request, 'Shop/index.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('index')


def registration(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            profile = UserProfile(id_user=user, avatar='avatar/1234.jpg')
            profile.save()
            return redirect('index')
        else:
            # Якщо форма не валідна, отримайте доступ до помилок
            errors = user_form.errors
            return redirect('index')


def product(request, id=None):
    context = {}
    product = Products.objects.get(id=id)
    context.update({"product": product})


    return render(request, 'Shop/product.html', context=context)


def user(request):
    context = {}
    if request.user.username:
        user = User.objects.get(username=request.user.username)
        context.update({"user": user})

        user_inf = UserProfile.objects.get(id_user=user)
        context.update({"user_inf": user_inf})

        user_buys = UserBuying.objects.filter(id_user=user).order_by('-timestamp')
        context.update({"user_buys": user_buys})

    return render(request, 'Shop/user.html', context=context)


def buy(request, id=None):

    context = {}
    if request.user.username:
        user = User.objects.get(username=request.user.username)

        user_inf = UserProfile.objects.get(id_user=user)

        product = Products.objects.get(id=id)

        wallet = float(user_inf.wallet)
        price = float(product.price)
        result = wallet - price

        if result >= 0:
            user_inf.wallet = result
            user_inf.save()

            buy = UserBuying(id_user=user, product=product, keys="asdf-asds-dasd-ghjj", price=price)
            buy.save()

            return redirect('user')

        else:
            print("Менше", result)

    return redirect(f'/product/{id}')


def news(request):
    context = {}

    return render(request, 'Shop/news.html', context=context)


def shop(request):
    context = {}
    products = Products.objects.all()
    context.update({"products": products})

    return render(request, 'Shop/shop.html', context=context)


def mode(request):
    context = {}

    return render(request, 'Shop/mode.html', context=context)


def support(request):
    context = {}
    faq = FAQ.objects.all()
    context.update({"faq": faq})

    return render(request, 'Shop/support.html', context=context)


def rules(request):
    context = {}
    rules = Rules.objects.all()
    context.update({"rules": rules})

    return render(request, 'Shop/rules.html', context=context)


def src(request):
    context = {}
    if request.method == "POST":
        src = request.POST.get('src')
        rules = Rules.objects.filter(Q(title__icontains=src.lower()) | Q(description__icontains=src.lower())
                                     | Q(title__icontains=src.capitalize()) | Q(description__icontains=src.capitalize())
                                     | Q(title__icontains=src.upper()) | Q(description__icontains=src.upper()))

        context.update({"rules": rules})

    faq = FAQ.objects.all()
    context.update({"faq": faq})

    return render(request, 'Shop/support.html', context=context)