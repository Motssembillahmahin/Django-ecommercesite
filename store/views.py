from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product


# view to handle product upload
def home(request):
    return render(request, 'store/home.html')  # Render the home page


def upload_product(request):
    # Check if the user is a seller
    # if request.user.role != 'seller':
    #     return redirect('home')  # Or any page you want to redirect non-sellers to

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Include files for image upload
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # Set the seller as the logged-in user
            product.save()
            return redirect('product_list')  # Redirect to the product listing page
    else:
        form = ProductForm()

    return render(request, 'store/upload_product.html', {'form': form})

# View to list products for the logged-in seller
@login_required
def product_list(request):
    # # Filter products by the logged-in seller
    # if request.user.role != 'seller':
    #     return redirect('home')  # Or any page you want to redirect non-sellers to

    products = Product.objects.filter(seller=request.user)
    return render(request, 'store/product_list.html', {'products': products})
