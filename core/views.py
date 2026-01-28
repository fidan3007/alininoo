from django.shortcuts import render
from .models import *
from core.forms import*
def home(request):
    sliders = Slider.objects.all()
    products1 = Product.objects.order_by("-id")[:5]
    products2 = Product.objects.order_by("-id")[5:10]
    az_products1 = Product.objects.filter(category__title="azərbaycan")[:5]
    az_products2 = Product.objects.filter(category__title="azərbaycan")[5:10]
    rus_products1 = Product.objects.filter(category__title="rus")[:5]
    rus_products2 = Product.objects.filter(category__title="rus")[5:10]
    tr_products1 = Product.objects.filter(category__title="türk")[:5]
    tr_products2 = Product.objects.filter(category__title="türk")[5:10]
    ing_products1 = Product.objects.filter(category__title="ingilis")[:5]
    ing_products2 = Product.objects.filter(category__title="ingilis")[5:10]
    newss = News.objects.order_by("-id")
    clubs = Club.objects.order_by("-id")
    events = Event.objects.order_by("-id")
    context = {
        'sliders': sliders,
        'products1': products1,
        'products2': products2,
        'az_products1': az_products1,
        'az_products2': az_products2,
        'rus_products1': rus_products1,
        'rus_products2': rus_products2,
        'tr_products1': tr_products1,
        'tr_products2': tr_products2,
        'ing_products1': ing_products1,
        'ing_products2': ing_products2,
        'newss': newss,
        'clubs' : clubs,
        'events': events,
    }
    return render(request, 'index.html',context)
   
def detailed_page(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = Product.objects.get(id=id)
            comment.user = request.user
            comment.save()
    form = CommentForm()
    products = Product.objects.get(id=id)
    similar_products = Product.objects.filter()[:5]
    similar_products2 = Product.objects.filter()[5:10]
    context = {
        'form':form,
        'product': products,
        'similar_products': similar_products,
        'similar_products2': similar_products2,
    }
    return render(request, 'detailed-page.html', context)

def filtr_page(request):
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    author = request.GET.get('author')
    publisher = request.GET.get('publisher')
    category = request.GET.get('category')
    products = Product.objects.all()
    if author == 'bakixanov':
        products = Product.objects.filter(author='Abbasqulu ağa Bakıxanov')
        print(products)
    if author == 'brown':
        products = Product.objects.filter(author='Dan Brown')
        print(products)
    if author == 'calil':
        products = Product.objects.filter(author='Cəlil Məmmədquluzadə')
        print(products)
        
    if author == 'susan':
        products = Product.objects.filter(author='Susan Sontag')
        print(products)
    if author == 'rauf':
        products = Product.objects.filter(author='Mehmet Rauf')
        print(products)
    if author == 'leo':
        products = Product.objects.filter(author='Leo Tolstoy')
        print(products)
        
    if author == 'emili':
        products = Product.objects.filter(author='Эмили Баллестерос')
        print(products)
    
    if publisher == 'qanun':
        products = Product.objects.filter(publisher='Qanun Nəşriyyatı')
        print(products)
    if publisher == 'is':
        products = Product.objects.filter(publisher='İş Bankası Kültür Yayınları')
        print(products)

    if category == 'rus':
        products = Product.objects.filter(category='rus')
        print(products)
    
    print(sort)
    if sort == 'new':
        products = Product.objects.order_by('-id')
    if sort == 'lower-price':
        products = Product.objects.order_by('price')
    if sort == 'higher-price':
        products = Product.objects.order_by('-price')
    if sort == 'discount':
        products = Product.objects.order_by('discount_price')
    if search:
        products = Product.objects.filter(title__icontains=search)
    newss = News.objects.order_by("-id")[:3]

    context = {
        'products' : products,
        'newss':newss,
    }
    return render(request, 'filtr-page.html', context)
    
def news_page(request,id):
    newsss = News.objects.order_by("-id")[:5]

    newss = News.objects.get(id=id)
    context = {
        'newss': newss,
        'newsss': newsss,
    }
    return render(request, 'news.html', context)