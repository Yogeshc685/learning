class Product(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=10)
    slug=models.SlugField()
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.title
