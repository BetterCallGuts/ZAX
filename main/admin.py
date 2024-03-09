from typing import Any
from django.contrib.admin import AdminSite
from django.core.handlers.wsgi import WSGIRequest
from django.template.response  import TemplateResponse
from manufacturers.models      import ManfComponentRel
from django.contrib.messages   import add_message, INFO
from django.utils.html         import mark_safe

class MyAdmin(AdminSite):
  
  def make_messages(self, req):
    waitmanf = 0
    waitdhan = 0
    waittsht = 0
    allss = ManfComponentRel.objects.all( )
    for i in allss:
      if i.check_status() == "فى انتظار امر التصنيع":
          waitmanf += 1
      elif i.check_status() == "تم الدهان و انتظار التشطيب":
        waittsht   += 1
      
      elif i .check_status() == "تم التصنيع وفى انتظار الإذن للدهان":
        waitdhan   += 1
    # wait for manf
    if waitmanf != 0:
      add_message(req,INFO, mark_safe(f"<a href='/manufacturers/manfcomponentrel/?statis=فى+انتظار+امر+التصنيع'> يوجد لديك {waitmanf}  ينتظرون منك الإذن لبدء التصنيع</a>") )
    # tm eldhan wait tshteb
    if waitdhan != 0:
      add_message(req,INFO, mark_safe(f"<a href='/manufacturers/manfcomponentrel/?statis=تم+التصنيع+وفى+انتظار+الإذن+للدهان'> يوجد لديك {waitdhan}  ينتظرون منك الإذن لبدء الدهان</a>") )
    # 
    if waittsht != 0:
      add_message(req,INFO, mark_safe(f"<a href='/manufacturers/manfcomponentrel/?statis=تم+الدهان+و+انتظار+التشطيب'> يوجد لديك {waittsht}  ينتظرون منك الإذن لبدء التشطيب</a>") )



    return req

  def index(self, 
  request: WSGIRequest, 
  extra_context: dict[str, Any] | None = {}) -> TemplateResponse:
    request = self.make_messages(request)
    return super().index(request, extra_context)
  


omar_admin_site = MyAdmin()