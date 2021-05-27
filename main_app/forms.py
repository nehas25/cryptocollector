from django import forms
from .models import CryptoCurrency, HistoricalData

class CryptoCurrencyForm(forms.ModelForm):
    class Meta:
        model = CryptoCurrency
        fields = ('name', 'ticker_symbol', 'about', 'current_price_usd', 'market_cap_usd')

class HistoricalDataForm(forms.ModelForm):
    class Meta:
        model = HistoricalData
        fields = ('date', 'open', 'close')