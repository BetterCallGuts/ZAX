from django.db import models
from datetime import datetime
from manufacturers.models import ManfComponentRel, Components


class Products(models.Model):
  
  mnaf = models.ForeignKey(ManfComponentRel, on_delete=models.CASCADE,verbose_name="المنتج", null=True, blank=True)
  
  price= models.FloatField(verbose_name="السعر")
  
  shopin= models.ForeignKey("Shop",on_delete=models.SET_NULL, null=True, blank=True, verbose_name="يعرض في محل")


  class Meta:
    
    verbose_name =   "منتج"
    verbose_name_plural = "منتجات"
  def __str__(self):
    return f"{self.mnaf.manf.name}"


class WarehouseProductRel(models.Model):
  warehouse   = models.ForeignKey('core.Warehouse', on_delete=models.CASCADE, verbose_name="المخزن")
  products    = models.ForeignKey('core.Products', on_delete=models.CASCADE, verbose_name="المنتج")
  how_many    = models.IntegerField( verbose_name="الكمية")
  


class saler(models.Model):
  
  name     = models.CharField(max_length=255, verbose_name="اسم البائع")
  phone    = models.CharField(max_length=255, verbose_name="رقم الهاتف",blank=True, null=True)
  addr     = models.TextField(verbose_name="العنوان"                   ,blank=True, null=True)
  isdeb    = models.BooleanField(default=False, verbose_name="دائن؟")
  how_much = models.FloatField(default=0, verbose_name="المقدار")
  prod     = models.ManyToManyField(Components, verbose_name="القطع", )
  
  
  
  def __str__(self):
    return f"{self.name}"
  class Meta:
    
    verbose_name_plural = "الموردون"
    verbose_name = "المورد"
  

 
  def the_rel(self):
    mr = WarehouseProductRel.objects.filter(products=self)
    return mr
  
  @classmethod
  def class_name(cls):
    return "products"

  def __str__(self):
    return f"{self.name}"



class Warehouse(models.Model):
  
  name       = models.CharField(max_length=255, blank=True, default="ware house", null=True, verbose_name="اسم المخزن")
  address    = models.TextField(blank=True, null=True, verbose_name="عنوانه")
  max_amount = models.IntegerField(blank=True, null=True, verbose_name="أقصي كم")
  
  class Meta:
    
    verbose_name_plural = "المخزن"
    verbose_name = "المخزن"
  
  def __str__(self):
    
    return f"{self.name}"
  
  
  def amount_init(self):
    result = 0
    for i in WarehouseProductRel.objects.filter(warehouse=self):
      result += i.how_many
    
    return result
  
 
  def our_obj(self):
    pp = WarehouseProductRel.objects.all()
    li = []
    for i in pp:
      
        if i.warehouse == self:
          
          li.append(i)
        
    return li

# 



class zabon(models.Model):
  
  name     = models.CharField(max_length=255, verbose_name="اسم الزبون")
  phone    = models.CharField(max_length=255, verbose_name="رقم الهاتف",blank=True, null=True)
  addr     = models.TextField(verbose_name="العنوان"                   ,blank=True, null=True)
  isdeb    = models.BooleanField(default=False, verbose_name="مدين؟")
  how_muchd= models.FloatField(default=0, verbose_name="المقدار")
  

  def __str__(self):
    return f"{self.name}"
  class Meta:
    
    verbose_name_plural = "الزبائن"
    verbose_name = "الزبون"
  
  
  def how_much(self):
    mysales = sales.objects.filter(who_bought=self)
    result = 0
    for i in mysales:
      # try:
        product = Products.objects.filter(name=i.what_got_saled)
        # print(product)
        for s in product:
          # try:
            result += (s.salary * i.how_many)
          # except:
          #   pass
      # except:
      #   pass
    return result

  how_much.short_description = "اجمالي المشتريات"



class sales(models.Model):

  
  what_got_saled = models.ForeignKey(Products, verbose_name='المنتج', null=True, blank=True, on_delete=models.CASCADE)
  how_many       = models.FloatField(default=1, verbose_name='الكمية')
  who_bought     = models.ForeignKey(zabon, verbose_name='الزبون', null=True, blank=True, on_delete=models.CASCADE)
  time_added     = models.DateTimeField(default=datetime.now, editable=False, verbose_name="وقت الاضافة")
  
  
  def win(self):
    
    return self.what_got_saled.price * self.how_many
  win.short_description = "المبلغ"

  class Meta:

    verbose_name_plural = "المبيعات"
    verbose_name        = "بيعة"

  def __str__(self):
    
    return f"{self.what_got_saled}"







class fwater(models.Model):
  
  
  how_many_fwater   = models.FloatField(verbose_name="مقدار الفاتورة") 
  description_fwater= models.TextField(blank=True,null=True,verbose_name="السبب")
  time_added_fwater = models.DateTimeField(default=datetime.now,verbose_name="وقت اضافة الفاتورة", editable=False)

  
  def __str__(self):
    return f"{self.how_many_fwater}|{self.time_added_fwater}"
  
  class Meta:
    verbose_name= "فاتورة"
    verbose_name_plural = "فواتير"
    
    
    
  
  


class Shop(models.Model):
  name = models.CharField(max_length=255, verbose_name="اسم المحل")
  addr = models.TextField(null=True, blank=True, verbose_name="عنوان المحل")
  
  def how_many_in_me(self):
    items = Products.objects.filter(shop_in=self)
    
    return len(items)
  how_many_in_me.short_description = "عدد المنتجات"
  
  def __str__(self):
    return f"{self.name}"
  
  class Meta:
    
    verbose_name = "المحل"
    verbose_name_plural = "المحلات"
    
    

