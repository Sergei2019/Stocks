from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TickerForm
from .tingo import get_data, get_price


def index(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        form = TickerForm()
    return render(request, 'index.html', {'form': form})


def ticker(request, id):
    return render(request, 'ticker.html', {'ticker': id,
                                           'meta': get_data(id),
                                           'price': get_price(id)})

