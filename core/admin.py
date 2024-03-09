from typing import Any
from django.contrib import admin
from .models import (Warehouse, 
Products,
WarehouseProductRel,
sales,
zabon,
saler,
fwater,
Shop,


)
from django.contrib.admin.models import LogEntry
from main.admin import omar_admin_site
from manufacturers.models import ManfComponentRel
# from django.db.models import Sum, Avg
# Register your models here.

# inlines
# -----------------------------------------
class warehouseProduectRelInine(admin.TabularInline):
  model = WarehouseProductRel
  extra = 0
  verbose_name_plural = "المنتجات داخل المخزن"
  verbose_name        = "منتج"

class ProdTypeRelInline(admin.TabularInline):
  model = Products
  extra = 0
  verbose_name_plural = "المنتجات داخل المخزن"
  verbose_name        = "منتج"


class SalesProduectRelInine(admin.TabularInline):
  model = sales
  extra = 0
  verbose_name_plural = "المبيعات الخاصة بالعنصر"
  verbose_name        = "مبيعات"

# simplelistfilter
# ------------------------

class ProductsFilter(admin.SimpleListFilter):
  
  title = "المنتج"
  parameter_name = "product"
  
  def lookups(self, req, modeladmin) -> list[tuple[Any, str]]:
    
    products_objects = Products.objects.all()
    
    returned_list = [
      (f"{i.pk}", f"{i}") for i in products_objects
    ]

    return returned_list
  
  def queryset(self, request, queryset):
   
    if self.value():
      
      returned_list = []
      item = Products.objects.get(pk=int(self.value()))
      

      for shop in queryset:
          
          if item.shop_in == shop:
            
            returned_list.append(shop.id)
            
      

      return queryset.filter(id__in=returned_list)
    else: 
      return queryset


# modeladmin
# --------------------------------------
class WareHouseProduct(admin.ModelAdmin):
  inlines = (warehouseProduectRelInine,)
  list_display = (
    "name",
    "address",
    "max_amount"
  )
  list_filter = (
    "name", 
    "address",

    
  )
  search_fields =(
    "name",
    "address",
    "max_amount"
  )
  


class ProductAdmin(admin.ModelAdmin):

  
  
  def formfield_for_foreignkey(self, db_field, request, **kwargs):
    
    
    if db_field.name == "mnaf":

        g = []
        x = ManfComponentRel.objects.all()
        for i in x:
          if i.check_status() == "جاهز للبيع":
            g.append(i.pk)


        
        kwargs["queryset"] = ManfComponentRel.objects.filter(id__in=g)

    return super().formfield_for_foreignkey(db_field, request, **kwargs)

  list_display = (
    "mnaf",
    "price",
    "shopin"
  )
  
  inlines = (
    warehouseProduectRelInine,
  )
  
  
class   SalesAdmin(admin.ModelAdmin):
  
  list_display = (
    "what_got_saled",
    "how_many",
    "win",
    'who_bought',
    "time_added"
  )
  list_filter = (
    "what_got_saled",
   
    "who_bought",
    
  )
  

class zabonAdminStyle(admin.ModelAdmin):
  
  list_display = (
    "name", 
    "phone",
    "how_much",
    "isdeb",
    "how_muchd",
    
  )
  list_filter = (
    "isdeb",
  )
  search_fields  = (
    "name",
    "phone",
    "addr",
    "how_muchd"
  )
  list_tatals = []
  SalesProduectRelInine.verbose_name_plural ="المنتج داخل المخازن"

  inlines = (
    SalesProduectRelInine,
    
    )

class salerAdminStyle(admin.ModelAdmin):
  
  list_display = (
    "name", 
    "phone",
    "isdeb",
    "how_much"
    
  )
  
  search_fields  = (
    "name",
    "phone",
    "addr",
    "how_much"
  )
  list_filter = (
    "isdeb",
    
  )
  

class fwaterAdmin(admin.ModelAdmin):
  
  list_display = (
    "how_many_fwater",
    "time_added_fwater"
  )
  search_fields = (
    "description_fwater",
    "how_many_fwater",
    
  )
  


class ShopAdminStyle(admin.ModelAdmin):
  
  list_display = (
    "name",
    "how_many_in_me",
  )
  # inlines      = ( ProdTypeRelInline,)
  list_filter  = (ProductsFilter,)






omar_admin_site.register(Warehouse   , WareHouseProduct)
omar_admin_site.register(Products    , ProductAdmin )

omar_admin_site.register(zabon       , zabonAdminStyle)
omar_admin_site.register(sales       , SalesAdmin)
omar_admin_site.register(saler       , salerAdminStyle)
omar_admin_site.register(fwater      , fwaterAdmin)
omar_admin_site.register(Shop        , ShopAdminStyle)


# admin.site.register(LogEntry)``

