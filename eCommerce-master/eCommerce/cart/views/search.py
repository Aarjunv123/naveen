from django.views import  View
from django.shortcuts import render , redirect
from cart.models.product import Product
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class Search(View):

    def get(self , request):

        len_cart = 0
        try:
            cart = request.session.get("cart")
            if cart:
                len_cart = len(cart)
        except:
            pass
        my_product = {}
        query = None
        query = request.GET.get('q')
        all_prod = Product.objects.all()
        if query:
            # prod = Product.objects.filter(Q(name__icontains=query))

            prod = search(all_prod,query)

            paginator = Paginator(prod, 3)
            page = request.GET.get('page')

            try:
                prods = paginator.page(page)
            except PageNotAnInteger:
                prods = paginator.page(1)
            except EmptyPage:
                prods = paginator.page(paginator.num_pages)

            if page is None:
                start_index = 0
                end_index = 7
            else:
                (start_index, end_index) = proper_pagination(prods, index=1)

            page_range = list(paginator.page_range)[start_index:end_index]


            my_product = {"searchprods": prods,
                          "q": query,
                          'page_range': page_range,
                          'len': len_cart,
                          }

        return render(request, 'search.html', my_product)


def search(product, q):
    search_prod = []
    for i in product:
        if q.lower() in i.category.Name.lower() or q.lower() in i.description.lower() or q.lower() in i.name.lower() or q.lower() in i.subcategory.lower() or q.lower() in i.subcat_type.lower():

            search_prod.append(i)

    return search_prod

def proper_pagination(prods, index):
    start_index = 0
    end_index = 7
    if prods.number > index:
        start_index = prods.number - index
        end_index = start_index + end_index
    return (start_index,end_index)



