from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TickerForm

def index(request):
    if request.method == 'POST':
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = request.POST['ticker']
            return HttpResponseRedirect(ticker)
    else:
        form = TickerForm()
    return render(request, 'index.html',{'form':form})


def ticker(request, id):
    context = {}
    context['ticker'] = id
    return render(request, 'ticker.html', context)