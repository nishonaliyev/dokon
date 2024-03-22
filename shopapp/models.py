
from django.db import models


class Mahsulot(models.Model):
    nomi = models.CharField(max_length=100)
    narxi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nomi


class Buyurtma(models.Model):
    mahsulotlar = models.ManyToManyField(Mahsulot, through='BuyurtmaMahsulot')

    def buyurtma_narxi(self):
        umumiy_narx = sum(mahsulot.narxi for mahsulot in self.mahsulotlar.all())
        chegirma_summasi = sum(
            mahsulot.narxi * mahsulot.buyurtmamahsulot.chegirma_foizi / 100 for mahsulot in self.mahsulotlar.all() if
            mahsulot.buyurtmamahsulot)
        chegirma_qilingan_narx = umumiy_narx - chegirma_summasi
        return chegirma_qilingan_narx


class BuyurtmaMahsulot(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    chegirma_foizi = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    chegirma_muddati = models.DateField(null=True, blank=True)


class Chegirma(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    chegirma_foizi = models.DecimalField(max_digits=5, decimal_places=2)
    chegirma_muddati = models.DateField()

