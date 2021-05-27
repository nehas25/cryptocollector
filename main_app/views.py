from django.shortcuts import render, redirect
from .models import CryptoCurrency, Exchange
from .forms import CryptoCurrencyForm, HistoricalDataForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    all_coins = CryptoCurrency.objects.all()
    context = {
        'coins': all_coins
    }
    return render(request, 'coins/coins_index.html', context)

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

def add_coin(request):
    if request.method == 'GET':
        form = CryptoCurrencyForm()
        context = {
            'form': form
        }
        return render(request, 'coins/coins_new.html', context)
    else:
        form = CryptoCurrencyForm(request.POST)
        print('======== form initialized ==========')
        if form.is_valid():
            print('======== form valid ==========')
            coin = form.save()
            return redirect('coins_detail', coin.id)

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

def coins_delete(request, coin_id):
    CryptoCurrency.objects.get(id=coin_id).delete()
    return redirect('index')

def coins_add_historical_data(request, coin_id):
    form = HistoricalDataForm(request.POST)
    if form.is_valid():
        data = form.save(commit=False)
        data.cryptocurrency_id = coin_id
        data.save()
        return redirect('coins_detail', coin_id)

def add_exchange(request, coin_id, exchange_id):
    CryptoCurrency.objects.get(id=coin_id).exchanges.add(exchange_id)
    return redirect('coins_detail', coin_id)

def remove_exchange(request, coin_id, exchange_id):
    CryptoCurrency.objects.get(id=coin_id).exchanges.remove(exchange_id)
    return redirect('coins_detail', coin_id)