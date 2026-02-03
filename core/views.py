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
    newss = News.objects.order_by("-id")[:3]
    clubs = Club.objects.order_by("-id")[:3]
    events = Event.objects.order_by("-id")[:3]
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
    az_products = Product.objects.filter(category__title="azərbaycan")
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    author = request.GET.get('author')
    publisher = request.GET.get('publisher')
    category = request.GET.get('category')
    products = Product.objects.all()
    if author == 'bakixanov':
        az_products = Product.objects.filter(author='Abbasqulu ağa Bakıxanov')
        print(products)
    if author == 'brown':
        az_products = Product.objects.filter(author='Dan Brown')
        print(products)
    if author == 'calil':
        az_products = Product.objects.filter(author='Cəlil Məmmədquluzadə')
        print(products)
        
    
    
        
  
    
    if publisher == 'qanun':
        az_products = Product.objects.filter(publisher='Qanun Nəşriyyatı')
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
        'az_products':az_products,
        'products' : products,
        'newss':newss,
    }
    return render(request, 'filtr-page.html', context)
    


def filtr_page_rus(request):
    rus_products = Product.objects.filter(category__title="rus")
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    author = request.GET.get('author')
    publisher = request.GET.get('publisher')
    category = request.GET.get('category')
    products = Product.objects.all()
    if author == 'carlz':
        rus_products = Product.objects.filter(author='Чарльза Диккенс')
        print(products)
    if author == 'emili':
        rus_products = Product.objects.filter(author='Эмили Баллестерос')
        print(products)
    if author == 'robert':
        rus_products = Product.objects.filter(author='Роберт Луис Стивенсон')
        print(products)
    if author == 'yevqeniy':
        rus_products = Product.objects.filter(author='Евгений Замятин')
        print(products)
        
    
    
        

    
    if publisher == 'eksmo':
        rus_products = Product.objects.filter(publisher='Эксмо')
        print(products)
    if publisher == 'azbuka':
        rus_products = Product.objects.filter(publisher='Азбука')
        print(products)
    if publisher == 'alpina':
        rus_products = Product.objects.filter(publisher='Альпина Паблишер')
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
        'rus_products':rus_products,
        'products' : products,
        'newss':newss,
    }
    return render(request, 'filtr-page-rus.html', context)

def filtr_page_turk(request):
    tr_products = Product.objects.filter(category__title="türk")
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    author = request.GET.get('author')
    publisher = request.GET.get('publisher')
    category = request.GET.get('category')
    products = Product.objects.all()
    if author == 'budak':
        tr_products = Product.objects.filter(author='Beyhan Budak')
        print(products)
    if author == 'rauf':
        tr_products = Product.objects.filter(author='Mehmet Rauf')
        print(products)
    if author == 'wolf':
        tr_products = Product.objects.filter(author='Christa Wolf')
        print(products)
    if author == 'ozgur':
        tr_products = Product.objects.filter(author='Özgür Taburoğlu')
        print(products)
        
    
    
        

    
    if publisher == 'koc':
        tr_products = Product.objects.filter(publisher='Koç Üniversitesi Yayınları')
        print(products)
    if publisher == 'is':
        tr_products = Product.objects.filter(publisher='İş Bankası Kültür Yayınları')
        print(products)
    if publisher == 'kronik':
        tr_products = Product.objects.filter(publisher='Kronik Kitap')
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
        'tr_products':tr_products,
        'products' : products,
        'newss':newss,
    }
    return render(request, 'filtr-page-turk.html', context)

def filtr_page_ing(request):
    ing_products = Product.objects.filter(category__title="ingilis")
    search = request.GET.get('search')
    sort = request.GET.get('sort')
    author = request.GET.get('author')
    publisher = request.GET.get('publisher')
    category = request.GET.get('category')
    products = Product.objects.all()
    if author == 'kawa':
        ing_products = Product.objects.filter(author='Yasunari Kawabata')
        print(products)
    if author == 'susan':
        ing_products = Product.objects.filter(author='Susan Sontag')
        print(products)
    if author == 'marcus':
        ing_products = Product.objects.filter(author='Marcus Aurelius')
        print(products)
    if author == 'bram':
        ing_products = Product.objects.filter(author='Bram Stoker')
        print(products)
        
    
    
        

    
    if publisher == 'arc':
        ing_products = Product.objects.filter(publisher='Arcturus Publishing')
        print(products)
    if publisher == 'ebury':
        ing_products = Product.objects.filter(publisher='Ebury Publishing')
        print(products)
    if publisher == 'penguin':
        ing_products = Product.objects.filter(publisher='Penguin Books Ltd')
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
        'ing_products':ing_products,
        'products' : products,
        'newss':newss,
    }
    return render(request, 'filtr-page-ing.html', context)

def news_page(request,id):
    newsss = News.objects.exclude(id=id).order_by("-id")[:5]

    newss = News.objects.get(id=id)
    context = {
        'newss': newss,
        'newsss': newsss,
    }
    return render(request, 'news.html', context)

def event_page(request,id):
    eventss = Event.objects.exclude(id=id).order_by("-id")[:5]

    events = Event.objects.get(id=id)
    context = {
        'events': events,
        'eventss': eventss,
    }
    return render(request, 'events.html', context)

def club_page(request,id):
    clubss = Club.objects.exclude(id=id).order_by("-id")[:5]

    clubs = Club.objects.get(id=id)
    context = {
        'clubs': clubs,
        'clubss': clubss,
    }
    return render(request, 'club.html', context)