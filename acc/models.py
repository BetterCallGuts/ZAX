from typing import Any
from django.db import models
from datetime import datetime
from django.utils.html import mark_safe

# Create your models here.
from django.contrib.auth.models import User, Group




class CustomUser(User):


        # username = models.CharField(max_length=255, verbose_name="اسم الحساب")

    ch = (
        ("m", "ذكر"),
        ("f", "انثى"),
    )
    
    pers_pho= models.ImageField(upload_to="emp_photos",verbose_name="رفع صورة شخصية", blank=True)
    salary  = models.FloatField(verbose_name='دخله الشهري', null=True, blank=True)

    gender  = models.CharField(max_length=250, choices=ch, verbose_name='الجنس', default="m")
    phone_nu= models.CharField(max_length=15 , null=True, blank=True, verbose_name='رقم الهاتف')
    id_for  = models.CharField(max_length=250, blank=True, null=True, verbose_name='الرقم القومي')
    date_ofj= models.DateField(default=datetime.now, verbose_name="وقت انضمامة للعمل")
    
    def photo_f(self):
        return mark_safe(f"<img src='{self.pers_pho.url}' alt='person_photo' style='width:300px;height=300px;border-radius:7px;box-shadow:0 0 10px black;'  />")
  
    photo_f.short_description = "الصورة"
    
    def __str__(self):
        return f"{self.username}"
    

    class Meta:
        # proxy = True
        app_label = 'acc'
        verbose_name = 'الحسابات الشخصية '
        verbose_name_plural = 'الحسابات الشخصية للموقع'



class CustomGroup(Group):
    class Meta:
        proxy = True
        app_label = 'acc'
        verbose_name = 'المجموعات'
        verbose_name_plural = 'مجموعات'

        




class absent(models.Model):
  fr = models.ForeignKey(CustomUser,
    on_delete=models.CASCADE,
    verbose_name="الحساب",
    )
  hmd= models.FloatField(verbose_name="عدد ايام الغياب")
  startdate = models.DateField(default=datetime.now, verbose_name="يبدأ من يوم")
  
  
  class Meta:
    verbose_name = "غائب"
    verbose_name_plural = "غيابات"







# ------------------------------------
