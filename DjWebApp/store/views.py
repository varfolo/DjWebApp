from django.shortcuts import render, redirect
from store.forms import ProductApplyForm
from django.template import RequestContext
from store.models import UserProduct, Profile
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from django.views.generic import View
from store.forms import UserForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):

    form = UserForm(request.POST or None)
    all_products = UserProduct.objects.all()

    return render(request,'store/index.html', {"form": form})

def log_in(request):
    #form = UserForm(request.POST or None)
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        authuser = authenticate(username=username, password=password)
        if authuser is not None:
            if authuser.is_active:
                login(request, authuser)
                user_id=authuser.id
                return HttpResponseRedirect(reverse ('account', args=(user_id,)))
            else:
                return render(request, 'store/Error.html', {'error_message': 'Ваш аккаунт заблокирован'})
        else:
           return render(request, 'store/error.html', {'error_message': 'Такой пользователь не существует'})
    return render(request, 'store/index.html')


    #template = loader.get_template('store/index.html')
 #       context = {
 #        'all_products': all_products, "form": form,
 #        }

       # Создание объекта user усли данные корректны

  #  html = ''
  #  for product in all_products:
  #      url = '/item/' + str(product.id) + '/'
  #      html += '<a href="' + url + '">' + product.productName + '</a><br>'
  #  return HttpResponse(html)
  #  return HttpResponse(template.render(context, request))

def add(request):
    if request.method =='POST':
        SGForm = ProductApplyForm(request.POST, request.FILES)
        if SGForm.is_valid():
            data = SGForm.cleaned_data
            Product = UserProduct()
            Product.userId = data['userId']
            Product.productName = data['productName']
            Product.description = data['description']
            Product.price = data['price']
            Product.Category = data['category']
            Product.image = request.FILES['image']#data['image']
            Product.save()
        return redirect ('/add')
    else:
        SGForm = ProductApplyForm()
    context ={'SGForm': SGForm}
    return render(request,'store/addproduct.html', context)#, RequestContext(request) )

def item(request, prod_id):
    try:
        product1 = UserProduct.objects.get(pk=prod_id)
    except UserProduct.DoesNotExist:
        raise Http404("Товар не существует")
    contextItem ={'product1': product1, 'prod_id':prod_id}
    return render(request,'store/item.html', contextItem)
   # return HttpResponse("<h2>Здесть можно увидеть детали интересующих товарров</h2>" + str(prod_id))

def registration(request):
    form = UserForm(request.POST or None, request.FILES)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        password2 = form.cleaned_data['password2']

        if 'password' in form.cleaned_data and 'password2' in form.cleaned_data:
            if form.cleaned_data['password'] != form.cleaned_data['password2']:
                #raise forms.ValidationError(u'You must type the same email each time')
              return render(request, 'store/error.html', {'error_message': 'Пароли не совпадают'})

        user.set_password(password)
        user.save()
        user = authenticate(request, username=username, password=password)

        userP = User.objects.get(pk=user.pk)
        userP.profile.userPic = request.FILES['userPic']
        userP.save()
        if user is not None:
            if user.is_active:
                login(request, user)
                #return render(request, 'store/index.html', {"form": form})               args=('2')
                return HttpResponseRedirect(reverse ('account', args=(user_id,)))
            else:
                return render(request, 'store/error.html', {'error_message': 'Ваш аккаунт заблокирован'})
        else:
           return render(request, 'store/error.html', {'error_message': 'Такой пользователь не существует'})
    else:
        return render(request, 'store/error.html', {'form': form})
   # return render(request,'store/index.html', {"form": form}) 
    return redirect ('/registration')

def account(request, user_id):
    return redirect('/')

def log_out(request):
    logout(request)
    # Перенаправление на страницу.
   # return HttpResponse("store/addproduct.html")
    #render(request, 'store/index.html')
    return redirect('/')

def error(request):
    return render(request, 'store/error.html')


