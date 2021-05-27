from django.db import models

# Create your models here.

class Exchange(models.Model):
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class CryptoCurrency(models.Model):
    name = models.CharField(max_length=100)
    ticker_symbol = models.CharField(max_length=100)
    about = models.TextField(max_length=5000)
    current_price_usd = models.DecimalField(max_digits=20, decimal_places=10)
    market_cap_usd = models.CharField(max_length=50)
    exchanges = models.ManyToManyField(Exchange, blank=True)

    def __str__(self):
        return f'{self.name} ({self.ticker_symbol})'
    

class HistoricalData(models.Model):
    date = models.DateField()
    open = models.DecimalField(max_digits=20, decimal_places=10)
    close = models.DecimalField(max_digits=20, decimal_places=10)
    cryptocurrency = models.ForeignKey(CryptoCurrency, on_delete=models.CASCADE)