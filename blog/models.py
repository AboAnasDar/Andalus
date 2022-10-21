from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    count = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.category.title} - {self.name}"

class History(models.Model):
    processes = (
        ('add', 'اضافة'),
        ('remove', 'سحب')
    )

    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    number = models.PositiveIntegerField()
    process = models.CharField(max_length=32, choices=processes)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.process
