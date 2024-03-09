from typing import Iterable
from django.db import models

from datetime import datetime, timedelta




class Factory(models.Model):
  
  name   = models.CharField(max_length=255, verbose_name="اسم المصنع",)
  addr   = models.TextField(verbose_name="عنوان المصنع", blank=True, null=True)


  
  class Meta:
    verbose_name = "مصنع"
    verbose_name_plural = "اماكن التصنيع"
  def __str__(self):
    return f"{self.name}"

class Components(models.Model):
  
  name     = models.CharField(verbose_name="اسم القطعة", max_length=255)
  how_many = models.IntegerField(default=0, verbose_name="عددها")

  def __str__(self):
    
    return self.name

  class Meta:
    
    verbose_name        = "القطعة"
    verbose_name_plural = "القطع"

class ManF(models.Model):
    
  name       = models.CharField(max_length=255, verbose_name="اسم المنتج")

  where      = models.ForeignKey(
    Factory, on_delete=models.SET_NULL,
    null=True, blank=True, verbose_name="المصنع")
  
  
  def __str__(self):
    
    return self.name
  
  class Meta:
    verbose_name        = "منتج"
    verbose_name_plural = "منتجات"
    




class ManfComponentRelHowManyComp(models.Model):
  
  component = models.ForeignKey(
    Components,
    on_delete=models.CASCADE
  )

  how_many = models.IntegerField(default=1)

  def __str__(self):
    return f""" القطعة:{self.component}\nالكمية:{self.how_many}"""

class ManfComponentRel(models.Model):
# 
  component   = models.ManyToManyField(
      ManfComponentRelHowManyComp,
      blank=True,
      verbose_name="القطع",
)
# 
  manf   = models.ForeignKey(
      ManF                       ,
      on_delete   =models.CASCADE,
      verbose_name="المنتج"      ,
)
#
  
  have_perm_to_manf    = models.BooleanField(default=False,verbose_name="إذن التصنيع")
  have_perm_to_dhan    = models.BooleanField(default=False,verbose_name="إذن الدهان")
  have_perm_to_tshteb  = models.BooleanField(default=False,verbose_name="إذن بالتشطيب")
# 
  day_started_tshted   = models.DateField(blank=True, null=True)
  day_started_dhan     = models.DateField(blank=True, null=True)

  day_started_manf     = models.DateField(blank=True, null=True)

# 
  howmany_days_manf    = models.IntegerField(default=0, verbose_name="ايام التصنيع") 
  howmany_days_dhan    = models.IntegerField(default=0, verbose_name="ايام التصنيع") 
  howmany_days_tshteb  = models.IntegerField(default=0, verbose_name="ايام التصنيع") 
# 
  time_added   = models.DateField(default=datetime.now, editable=False, verbose_name="وقت بدء التصنيع")

  def save(self, *args, **kwargs) :
    if self.pk:
      super(ManfComponentRel, self).save(*args, **kwargs)
      if self.have_perm_to_tshteb and not self.day_started_tshted:
        self.day_started_tshted = datetime.now().date()
      
      if self.have_perm_to_dhan and not self.day_started_dhan:
        self.day_started_dhan = datetime.now().date()
      
      
      if self.have_perm_to_manf and not self.day_started_manf:
        self.day_started_manf = datetime.now().date()
    
    
    super(ManfComponentRel, self).save(*args, **kwargs)

  def check_status(self):
    
    if self.have_perm_to_tshteb:
      
      start = self.day_started_tshted
      delta = timedelta(self.howmany_days_tshteb)
      end   = start + delta
      if end > datetime.now().date():
        return "يتم التشطيب"
      
      return "جاهز للبيع"
      # 
    if self.have_perm_to_dhan:


      start = self.day_started_dhan
      delta = timedelta(self.howmany_days_dhan)
      end   = start + delta
      if end > datetime.now().date():
        return "يتم الدهان"
      
      return "تم الدهان و انتظار التشطيب"
      # 
    if self.have_perm_to_manf:
      
      start = self.day_started_manf
      delta = timedelta(self.howmany_days_manf)
      end   = start + delta
      if end > datetime.now().date():
        return "يتم التصنيع"
      
      
      return "تم التصنيع وفى انتظار الإذن للدهان" 
      # 
    return "فى انتظار امر التصنيع"
  check_status.short_description = "حالة المنتج"

  def __str__(self) -> str:
    return f"{self.manf.name}"

  class Meta:
    
    verbose_name_plural = "اضف منتجات للتصنيع"
    verbose_name        = "قطعة للتصنيع"
    permissions         = [
      ("can_give_perm", "صلاحية تغير المرحلة"),
    ]
    
