from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Brand
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied

# Rule 1: Only Admins
def is_admin(user):
    if user.is_authenticated and user.role == 'admin':
        return True
    raise PermissionDenied # Kicks them out if they try to access

# Rule 2: Managers OR Admins (since Admins should also be able to fix products)
def is_manager_or_admin(user):
    if user.is_authenticated and user.role in ['admin', 'manager']:
        return True
    raise PermissionDenied



################################################ all products
@login_required(login_url='login')


def Products(request):
    product_list = Product.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    
    # Get filter parameters from GET request
    cateid = request.GET.get('category_id')
    brand_id = request.GET.get('brand_id')
    
    selected_cate = int(cateid) if cateid else None
    selected_brand = int(brand_id) if brand_id else None

    # Chain filters dynamically
    if cateid:
        product_list = product_list.filter(category_id=cateid)
    if brand_id:
        product_list = product_list.filter(brand_id=brand_id)

    # Apply pagination to the filtered list
    paginator = Paginator(product_list, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'brands': brands,
        'page_obj': page_object,
        'selected_cate': selected_cate,
        'selected_brand': selected_brand,
    }

    return render(request, 'ProductTemplate/Products.html', context)

################################################## add products 

@login_required(login_url='login')
@user_passes_test(is_manager_or_admin)
def AddProduct(request):
    allcategories = Category.objects.all()
    allbrands = Brand.objects.all()

    if request.method == 'POST':
        p_name = request.POST.get('name')
        p_price = request.POST.get('price')
        p_image = request.FILES.get('image')

        cat_id = request.POST.get('category_id')
        new_cate = request.POST.get('new_category')

        brand_id = request.POST.get('brand_id')
        new_brand = request.POST.get('new_brand')

        # 🚀 Category Logic
        if new_cate:
            clean_cate = new_cate.strip().title()
            category_obj, create_cate = Category.objects.get_or_create(name=clean_cate)
        elif cat_id: # 🛡️ Safe check agar dropdown use hua ho
            category_obj = Category.objects.get(id=cat_id)
        else:
            return redirect('addproduct') # Agar user ne dono select nahi kiye to wapas bhej do

        # 🚀 Brand Logic (Copy Paste Error Fixed)
        if new_brand:
            clean_brand = new_brand.strip().title()
            brand_obj, created_brand = Brand.objects.get_or_create(name=clean_brand)
        elif brand_id: # 🛡️ Safe check
            brand_obj = Brand.objects.get(id=brand_id)
        else:
            return redirect('addproduct')

        Product.objects.create(
            p_name=p_name,
            p_price=p_price,
            p_image=p_image,
            category=category_obj,
            brand=brand_obj,
        )
        return redirect('products')

    context = {'categories': allcategories, 'brands': allbrands}
    return render(request, 'ProductTemplate/AddProduct.html', context)


@login_required(login_url='login')
@user_passes_test(is_manager_or_admin)
def UpdateProduct(request, id):
    product = get_object_or_404(Product, id=id) # 🛡️ Crash se bachanay k liye
    allcategories = Category.objects.all()
    allbrands = Brand.objects.all()

    if request.method == 'POST':
        p_name = request.POST.get('name')
        p_price = request.POST.get('price')
        p_image = request.FILES.get('image')

        cat_id = request.POST.get('category_id')
        new_cate = request.POST.get('new_category')

        brand_id = request.POST.get('brand_id')
        new_brand = request.POST.get('new_brand')

        # 🚀 Update Category Logic (Nayi category bhi update ho sakay gi ab)
        if new_cate:
            clean_cate = new_cate.strip().title()
            new_category, create_cate = Category.objects.get_or_create(name=clean_cate)
        else:
            new_category = Category.objects.get(id=cat_id)

        # 🚀 Update Brand Logic
        if new_brand:
            clean_brand = new_brand.strip().title()
            new_brand_obj, created_brand = Brand.objects.get_or_create(name=clean_brand)
        else:
            new_brand_obj = Brand.objects.get(id=brand_id)

        # Values update ki
        product.p_name = p_name
        product.p_price = p_price
        product.category = new_category
        product.brand = new_brand_obj

        if p_image:
            product.p_image = p_image

        product.save()
        return redirect('products')

    context = {
        'product': product, 
        'categories': allcategories,
        'brands': allbrands 
    }
    return render(request, 'ProductTemplate/UpdateProduct.html', context)

########################################### DELETE PRODUCT   ####################################### 

@user_passes_test(is_manager_or_admin)
def DeleteProduct(request, id):
    
    product = get_object_or_404(Product, id=id)
    product.delete()
    return JsonResponse({'status':'success'})

################################################################################## FILTER category
@login_required(login_url='login')
def Categorry(request):

    allcategories =Category.objects.all().order_by('-id')

    if request.method =='POST':
        newcategory = request.POST.get('category_name')

        if newcategory:
            clean_category = newcategory.strip().title()
            Category.objects.get_or_create(name = clean_category)
            return redirect('category')

    return render(request , 'ProductTemplate/Category.html' , context={'categories':allcategories})




##################################################################################  BRANDS
@login_required(login_url='login')
def Brandds(request):
    if request.method == 'POST':
        new_brand = request.POST.get('brand_name')
   
        if new_brand:
            cleand_brand = new_brand.strip().title()
            Brand.objects.get_or_create(name = cleand_brand)

        return redirect('brand')

         
    if request.GET.get('trash') == 'true':
        brands = Brand.objects.filter(is_delete=True).order_by('-id')
    else:
        brands = Brand.objects.filter(is_delete=False).order_by('-id')
    
        
    return render(request, 'ProductTemplate/Brand.html', {'brands': brands})




    

################################## category status  ###############################################

def DeleteStatus(request , id):
    category =get_object_or_404( Category ,id=id)
    category.status = 'Deactive'
    category.save()

    return redirect('category')

def RecoverStatus(request , id):
    category =get_object_or_404( Category ,id=id)
    category.status = 'Active'
    category.save()

    return redirect('category')

def BrandSoftDelete(request , id):
    brand =get_object_or_404(Brand, id=id)
    brand.is_delete = True
    brand.save()

    return redirect('brand')

def BrandSoftrecover(request , id):
    brand =get_object_or_404(Brand, id=id)
    brand.is_delete = False
    brand.save()

    return redirect('brand')