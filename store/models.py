from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=200,unique=True)
    def __str__(self):
        return self.name 


class Occassion(models.Model):
    name=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self) :
        return self.name
    
class Shape(models.Model):
    name=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Cake(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product_images", default="default.jpg", null=True, blank=True)
    occassion_object=models.ManyToManyField(Occassion)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Weight(models.Model):
    name=models.CharField(max_length=150,unique=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True) 
    def __str__(self):
        return self.name
    
class Flavour(models.Model):
    name=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name



class CakeVarient(models.Model):
    name=models.CharField(max_length=200,null=True)
    images=models.ImageField(upload_to="product_images", default="default.jpg", null=True, blank=True)
    weight_object=models.ManyToManyField(Weight)
    shape_object=models.ForeignKey(Shape,on_delete=models.CASCADE, related_name="shape")
    cake_object=models.ManyToManyField(Cake)
    flavour_object=models.ForeignKey(Flavour,on_delete=models.CASCADE,related_name="flavour")
    qty=models.PositiveIntegerField( null=True)
    price=models.PositiveIntegerField()
    description=models.CharField(max_length=400,null=True)
    occassion_object=models.ManyToManyField(Occassion,)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    tag_objects=models.ManyToManyField(Tag,null=True)
    def __str__(self):
        return self.name

class Basket(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE, related_name="cart")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    @property
    def cart_items(self):
        return self.cartitem.filter(is_order_placed=False)
    
    @property
    def cart_item_count(self):
        return self.cart_items.count()
    
    @property
    def basket_total(self):
        basket_items=self.cart_items
        if basket_items:
            total=sum([bi.item_total for bi in basket_items])
            return total
        return 0

class BasketItem(models.Model):
    cakev_object=models.ForeignKey(CakeVarient, on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
    basket_object=models.ForeignKey(Basket,on_delete=models.CASCADE, related_name="cartitem")
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)
    weight_object=models.ForeignKey(Weight,on_delete=models.CASCADE,null=True)
    occassion_object=models.ForeignKey(Occassion,on_delete=models.CASCADE,null=True)
    is_order_placed=models.BooleanField(default=False)
    
    @property
    def item_total(self):
        return self.qty*self.cakev_object.price

class Order(models.Model):
    user_object=models.ForeignKey(User,on_delete=models.CASCADE,related_name="purchase")
    delivery_address=models.CharField(max_length=200)
    email=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=12)
    is_paid=models.BooleanField(default=False)
    total=models.PositiveIntegerField()
    order_id=models.CharField(max_length=200, null=True)
    options=(
        ("cod","cod"),
        ("online","online")
    )
    payment=models.CharField(max_length=200, choices=options, default="cod")
    option=(
        ("order-placed","order-placed"),
        ("intransit","intransit"),
        ("dispatched","dispatched"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=200,choices=option,default="order-placed")


    @property
    def get_order_items(self):
        return self.purchaseitems.all()

    @property
    def get_order_total(self):
        purchase_items=self.get_order_items
        order_total=0
        if purchase_items:
            order_total=sum([pi.basket_item_object.item_total for pi in purchase_items])
        return order_total
    
class OrderItems(models.Model):
    order_object=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="purchaseitems")
    basket_item_object=models.ForeignKey(BasketItem,on_delete=models.CASCADE)

def create_basket(sender,instance,created,**kwargs):
    if created:
        Basket.objects.create(owner=instance)
post_save.connect(create_basket,sender=User)
    





    
