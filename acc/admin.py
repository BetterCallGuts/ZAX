from django.contrib             import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin  import UserAdmin, GroupAdmin
from .models                    import (

  CustomUser,
  CustomGroup,
  absent
  )

from main.admin   import omar_admin_site

class AbsentInlineStack(admin.StackedInline):
  
  model = absent
  extra = 0
  verbose_name = "يوم غياب"
  verbose_name_plural = "غيابات الموظف"



class CustomUSerAdmin(UserAdmin):
  
  

  fieldsets = list(UserAdmin.fieldsets)
  fieldsets.insert(0, ("الأساسى", {
    "fields" : (
      "photo_f",
      "pers_pho",
      "salary",
      "gender",
      "phone_nu",
      "id_for",
      "date_ofj",
      )
  }))
  fieldsets.pop(2)
  
  readonly_fields = (
    "photo_f",
  )
  inlines = (
    AbsentInlineStack , 
  )
  
  search_fields = (
    "username",
    
  )
  list_filter =(
    "gender",
    
  )
  list_display = (
    "username",
    "salary"  ,
    "id_for",
    
    
  )


omar_admin_site.register(CustomUser, CustomUSerAdmin)
omar_admin_site.register(CustomGroup, GroupAdmin)







