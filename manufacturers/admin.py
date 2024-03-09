from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from .models import Components, ManF, ManfComponentRel, Factory
from main.admin  import omar_admin_site




class ProductComponentFilter(admin.SimpleListFilter):
    title =  "منتج"
    parameter_name = "product"

    def lookups(self, request, model_admin):
      products = ManF.objects.all()

      return [[x.name, x.name] for x in products]

    def queryset(self, request, queryset):
      returned_list = []
      if self.value():
        
        
        l        = ManF.objects.get(name=self.value())
        products = ManfComponentRel.objects.filter(
          manf=l
        )
        
        for i in products:

            for m in queryset:
              
              for k in i.component.all():
                if m ==  k.component:
          
                  returned_list.append(m.id)
      
        return queryset.filter(id__in=returned_list)
      
      return queryset




class StatusFilter(admin.SimpleListFilter):
  title = "حالة التصنيع"
  parameter_name = "statis"

  def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
    
    x = [
      ["فى انتظار امر التصنيع", "فى انتظار امر التصنيع"],
      ["يتم التصنيع", "يتم التصنيع"],
      ["يتم الدهان", "يتم الدهان"],
      ["جاهز للبيع", "جاهز للبيع"],
      ["يتم التشطيب", "يتم التشطيب"],
      ["تم الدهان و انتظار التشطيب", "تم الدهان و انتظار التشطيب"],
      ["تم التصنيع وفى انتظار الإذن للدهان", "تم التصنيع وفى انتظار الإذن للدهان"]
    ]
    return x

  def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
    
    if self.value():
      r = []
      alls = ManfComponentRel.objects.all()

      for i in alls:
        if i.check_status() == self.value():
          r.append(i.pk)
          
      return queryset.filter(id__in=r)
    return queryset

class ComponentsAdminStyle(admin.ModelAdmin):
  
  list_display = ["name", "how_many"]

  search_fields = ("name", "how_many" )
  
  list_filter   = (
    ProductComponentFilter,
  )

class ManFAdminStyle(admin.ModelAdmin):
  
  list_display = (
    "name",
    "where"
    
  )
  search_fields = (
    "name",
  )
  
  
  

class ManfComponentRelModelAdmin(admin.ModelAdmin):
  

  list_display = (
    "manf",
    "check_status",
    "time_added"
    )
  
  list_filter = [
    StatusFilter,
      ]
  

  change_form_template = "mycustom/manf.html"
  
  def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
    x = super().get_queryset(request)
    return x
  
  def changeform_view(self, request: HttpRequest, object_id: str | None = ..., form_url: str = ..., extra_context: dict[str, bool] | None = ...) -> Any:
    extra_context = extra_context or {}
    extra_context['choices'] = ManF.objects.all()
    extra_context['components'] = Components.objects.all()
    return super().changeform_view(request, object_id, form_url, extra_context)


class FactoryProductFilter(admin.SimpleListFilter):
    title = ("تحتوي على منتج")
    parameter_name = "searchfabypr"

    def lookups(self, request, model_admin):
        x = ManF.objects.all()
        return [ [f"{a.name}", a.name]   for a in x if a.where != None]

    def queryset(self, request, queryset):
      if self.value():
        x = []
        alls = ManF.objects.get(name=self.value())
        
        for i in queryset:
          if i == alls.where:
            return
          
        
      return queryset


class FactoryAdminStyle(admin.ModelAdmin):
  
  list_display = ["name"]
  list_filter  = [FactoryProductFilter]

  search_fields = ["name", "addr"]



omar_admin_site.register(Components      ,ComponentsAdminStyle       )
omar_admin_site.register(ManF            ,ManFAdminStyle             )
omar_admin_site.register(ManfComponentRel, ManfComponentRelModelAdmin)
omar_admin_site.register(Factory, FactoryAdminStyle)
