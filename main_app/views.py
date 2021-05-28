from django.shortcuts import render, redirect
from .models import CryptoCurrency, Exchange
from .forms import CryptoCurrencyForm, HistoricalDataForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def index(request):
    all_coins = CryptoCurrency.objects.filter(user=request.user)
    context = {
        'coins': all_coins
    }
    return render(request, 'coins/coins_index.html', context)

@login_required
def coins_detail(request, coin_id):
    coin = CryptoCurrency.objects.get(id=coin_id)
    form = HistoricalDataForm()
    remaining_exchanges = Exchange.objects.exclude(cryptocurrency=coin_id)
    context = {
        'coin': coin,
        'form': form,
        'remaining_exchanges': remaining_exchanges
    }
    return render(request, 'coins/coins_detail.html', context)

@login_required
def add_coin(request):
    if request.method == 'GET':
        form = CryptoCurrencyForm()
        context = {
            'form': form
        }
        return render(request, 'coins/coins_new.html', context)
    else:
        form = CryptoCurrencyForm(request.POST)
        if form.is_valid():
            coin = form.save(commit=False)
            coin.user = request.user
            coin.save()
            return redirect('coins_detail', coin.id)

@login_required
def coins_edit(request, coin_id):
    coin = CryptoCurrency.objects.get(id=coin_id)
    if request.method == 'GET':
        form = CryptoCurrencyForm(instance=coin)
        context = {
            'form': form
        }
        return render(request, 'coins/coins_edit.html', context)
    else:
        form = CryptoCurrencyForm(request.POST, instance=coin)
        if form.is_valid():
            form.save()
            return redirect('coins_detail', coin.id)

@login_required
def coins_delete(request, coin_id):
    CryptoCurrency.objects.get(id=coin_id).delete()
    return redirect('index')

@login_required
def coins_add_historical_data(request, coin_id):
    form = HistoricalDataForm(request.POST)
    if form.is_valid():
        data = form.save(commit=False)
        data.cryptocurrency_id = coin_id
        data.save()
        return redirect('coins_detail', coin_id)

@login_required
def add_exchange(request, coin_id, exchange_id):
    CryptoCurrency.objects.get(id=coin_id).exchanges.add(exchange_id)
    return redirect('coins_detail', coin_id)

@login_required
def remove_exchange(request, coin_id, exchange_id):
    CryptoCurrency.objects.get(id=coin_id).exchanges.remove(exchange_id)
    return redirect('coins_detail', coin_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('==============')
            print(user.__dict__)
            print('==============')
            # Auto login the user upon sucessful signup
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid username and/or password'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)