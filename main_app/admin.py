from django.contrib import admin
from .models import CryptoCurrency, HistoricalData, Exchange

# Register your models here.
admin.site.register(CryptoCurrency)
admin.site.register(HistoricalData)
admin.site.register(Exchange)