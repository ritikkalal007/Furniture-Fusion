from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {'title': 'index'}
    return render(request, 'index.html', context=context)

def about(request):
    context = {'title': 'about'}
    return render(request, 'about.html', context=context)

def services(request):
    context = {'title': 'services'}
    return render(request, 'services.html', context=context)

# def shop(request):
#     context = {'title': 'shop'}
#     return render(request, 'shop.html', context=context)

def contact(request):
    context = {'title': 'contact'}
    return render(request, 'contact.html', context=context)

def thankyou(request):
    context = {'title': 'thankyou'}
    return render(request, 'thankyou.html', context=context)

def cart(request):
    context = {'title': 'cart'}
    return render(request, 'cart.html', context=context)

def checkout(request):
    context = {'title': 'checkout'}
    return render(request, 'checkout.html', context=context)



from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already registered.')
            else:
                user = User(
                    name=name,
                    email=email,
                    mobile=mobile,
                    address=address,
                    city=city,
                    pincode=pincode,
                    password=make_password(password)
                )
                user.save()
                messages.success(request, 'Registration successful.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'registration.html')

from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import User

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # Set session or any other login logic
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                messages.success(request, 'Login successful.')
                return redirect('index')  # Redirect to a home or dashboard page
            else:
                messages.error(request, 'Invalid password.')
        except User.DoesNotExist:
            messages.error(request, 'User with this email does not exist.')
            
    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['user_id']
        del request.session['user_name']
        messages.success(request, 'Logout successful.')
    except KeyError:
        messages.error(request, 'You are not logged in.')
    return redirect('index')  # Redirect to the home page or login page


from django.shortcuts import render, redirect
from .models import *

def shop(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        image_file = request.FILES.get('image_file')
        price = request.POST.get('price')
        
        if product_name and image_file and price :
            new_product = Product(
                product_name=product_name,
                image_file=image_file,
                price=price,
            )
            new_product.save()
            
            return redirect('show_product')  # Redirect to show_product view after saving

    context = {
        'title': 'Add Product'
    }
    return render(request, 'shop.html', context)


def show_product(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'title': 'Product List'
    }
    return render(request, 'show_product.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # Import login_required decorator


@login_required  # Apply login_required decorator to restrict access to authenticated users only
def cart(request):
    cart_item = Cart.objects.filter(user=user)
    # total_price = sum(item.total_price() for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart.html', context)

@login_required  # Apply login_required decorator to restrict access to authenticated users only
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=pk)
    cart_item = Cart.objects.get(user=user)

    if not Cart.objects.filter(user=user, product=product).exists():
        Cart.objects.create(product=product,
                             user=user
                             )

    return redirect('cart')

@login_required  # Apply login_required decorator to restrict access to authenticated users only
def remove_from_cart(request, item_id):
    try:
        cart_item = Cart.objects.get(user=user, pk=pk)
        cart_item.delete()

    except Cart.DoesNotExist:
        pass

    return redirect('cart')
