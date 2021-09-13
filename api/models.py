from django.db import models



class Dataset(models.Model):
    country = models.CharField(max_length=100, verbose_name='Country')
    category = models.CharField(max_length=100, verbose_name='Category')

    def __str__(self):
        return self.category
    

class Link(models.Model):
    dataset_link = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='link', blank=True)
    link = models.URLField(verbose_name='Link')

    def __str__(self):
        return self.link

class Source(models.Model):
    dataset_source = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='source', blank=True)
    source = models.CharField(max_length=100, verbose_name='Source')

    def __str__(self):
        return self.source

class Brand(models.Model):
    dataset_brand = models.ForeignKey(Dataset, on_delete=models.CASCADE, related_name='brand', blank=True)
    brand = models.CharField(max_length=100, verbose_name='Brand')

    def __str__(self):
        return self.brand
