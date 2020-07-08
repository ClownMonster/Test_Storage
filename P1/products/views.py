from django.shortcuts import render
#from django.http import JsonResponse
#from django.http import HttpResponse
from .models import Product

# Create your views here.

def home_view(request, *args, **kwargs):
    my_data = {
        'name' : 'Mohan Kumar K',
        'company': 'Clown Monsters Tech Inc',
        'Fav_Color': 'Blue',
        'my_list' : [1,4,5,6,8],


    }
    return render(request,'home.html', my_data)






def product_detail_view(request, * args, **kwargs):
    d1 = Product.objects.get(id = 3)
    '''
    context = {
        'title': d1.title,
        'description': d1.description
    }
    '''

    context = {
        'object': d1
    }

    return render(request, 'Product_Detail.html',context)


from .forms import ProductForm, RawProductForm

def add_products(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form =  RawProductForm(request.POST)
    if my_form.is_valid():
        Product.objects.create(**my_form.cleaned_data)
    else:
        print(my_form.errors)

    context = {
        'form' : my_form
    }



    return render(request, 'add_products.html',context)

    

from django.shortcuts import get_object_or_404 # for object out of range handling
from django.http import Http404

#render the dynamic products look up
def dynamic_look_up(request,my_id):
    ob = get_object_or_404(Product, id = my_id)
    context = {
        'object': ob
    }


    '''
    hadling using http 404
     try:
        ob = Product.objects.get(id = my_id)
    except Product.DoesNotExist:
        raise Http404

    '''

    return render(request, 'lookup.html',context)



def all_products(request):
    ob = Product.objects.all()
    context = {
        'object': ob
    }

    return render(request, 'AllProducts.html', context)