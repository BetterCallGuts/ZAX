from django.shortcuts import render, redirect

from .models import ManF, ManfComponentRel, Components,ManfComponentRelHowManyComp
from django.http import HttpRequest, HttpResponse
from django.contrib.messages  import success






def manf_product_submit(req:HttpRequest) ->HttpResponse:
  
  
  data     = dict(req.POST)
  data.pop("csrfmiddlewaretoken")
  prod     = data.pop("prod")[0]
  days     = int(data.pop("how_many_days")[0])
  ismanf   = data.pop("ismanf", None)
  isdhan   = data.pop("isdhan", None)
  istshteb = data.pop("istshteb", None)

  
  obj_pk = data.get("obj_pk", False)
  if not obj_pk:
    
    many = int(data.pop("how_many")[0])
    obj =  None
    
  else:
    many= None
    data.pop("obj_pk")
    days_to_dhan   = data.pop("howmany_days_dhan"  , False)
    days_to_tshteb = data.pop("howmany_days_tshteb", False)
    
    obj = ManfComponentRel.objects.get(pk=int(obj_pk[0]))
   
    if ismanf:
      obj.have_perm_to_manf   = True
    if isdhan:
      obj.have_perm_to_dhan   = True
    if istshteb:
      obj.have_perm_to_tshteb = True
    
    if req.user.has_perm("manufacturers.can_give_perm"):
      if  not ismanf:
        obj.have_perm_to_manf   = False
      if  not isdhan:
        obj.have_perm_to_dhan   = False
      if   not istshteb:
        obj.have_perm_to_tshteb = False
      
      

    if days_to_dhan:
      obj.howmany_days_dhan     = int(days_to_dhan[0])

    if days_to_tshteb:
      obj.howmany_days_tshteb   = int(days_to_tshteb[0])

  # handle product exists or not
  
  proditem = ManF.objects.filter(name=prod)
  if proditem.exists():
    proditem = proditem[0]
  else:
    proditem = ManF.objects.create(name=prod)
    proditem.save()
  
  # prep for component
  is_even     = True
  list_sorted = []
  temp_list_s = {}

  for i in data:
    if is_even:
      temp_list_s["name"]     = data[i][0]
      
      is_even = not is_even
      continue
    if not is_even:
      temp_list_s["how_many"] = int(data[i][0])
      list_sorted.append(temp_list_s)
      temp_list_s             = {}
      is_even = not is_even
  # check  conponent exists or create it
  del temp_list_s
  
  many_to_many_field_list = []
  # create or get component
  for i in list_sorted:
    
    comp   = Components.objects.filter(name=i['name'])
    if comp.exists():
      comp = comp[0]
    else:
      comp = Components.objects.create(
        name=i['name']
      )
      comp.save()
    rel_withman = ManfComponentRelHowManyComp.objects.filter(
      component = comp,
      how_many  = i['how_many'],
    ) 
    if rel_withman.exists():
      rel_withman = rel_withman[0]
    else:
      rel_withman = ManfComponentRelHowManyComp.objects.create(
        component = comp,
        how_many  = i['how_many'],
      )
      rel_withman.save()
    
    many_to_many_field_list.append(rel_withman)
  
  # make a rel
  if obj:
    print(proditem)
    print(type(proditem))
    obj.manf              = proditem
    obj.howmany_days_manf = days
    obj.component.clear()

    for i in many_to_many_field_list:
      obj.component.add(i)  
    obj.save()
  else:
    
    for i in range(many):
      manfobjectfinal = ManfComponentRel.objects.create(
        manf              = proditem,
        howmany_days_manf =  days
      )

      for i in many_to_many_field_list:
        manfobjectfinal.component.add(i)
        

      manfobjectfinal.save()

    del manfobjectfinal

  success(req, "تم اضافة المنتج بنجاح")
  
  return redirect("/manufacturers/manfcomponentrel/" )



def check_product(req:HttpRequest) ->HttpResponse:


  product = req.POST.get("prod")
  if product:
    x = ""
    a = 1
    manfuca = ManF.objects.filter(name=product)
    if manfuca.exists():
      manfuca = manfuca[0]
      
      rel  = ManfComponentRel.objects.filter(manf=manfuca)
      if rel.exists():
        rel = rel[0]  
        for i in rel.component.all():
          x += f""" 
          
          <div class="bg-light px-2 py-4 gap-3 component form-group d-flex justify-content-around">
            <input type="text"   required value="{i.component}"   name="name{a}" class="form-control mx-3"  placeholder="اسم القطعة"    list="compo">
            <input type="number" required value="{i.how_many}"   name="howmuch{a}" class="form-control mx-3"  placeholder="العدد المطلوب"  >
            <button type="button" class="btn btn-danger btn-sm remove-btns">Remove</button>

          </div>
        
          """
          a += 1
    x += f'''
      <div id='last' class="bg-light px-2 py-4 gap-3  form-group d-flex justify-content-around">
        <input type="text"   required value=""   name="name{a}" class="form-control mx-3"  placeholder="اسم القطعة"    list="compo">
        <input type="number" required value="0"   name="howmuch{a}" class="form-control mx-3"  placeholder="العدد المطلوب"  >
          <button type="button" class="btn btn-danger btn-sm remove-btns">Remove</button>

      </div>
      ''' '''
      <script>
      var x   = document.querySelectorAll('.remove-btns');
      
      
      
        var a = 0;
        for (a; a < x.length; a++) {
        
        x[a].addEventListener('click', (e) => {
            e.preventDefault();
            e.target.closest('.form-group').remove();
            });
      }
      
      delete x
      delete a
      </script>


      '''
    return HttpResponse(x)
  

