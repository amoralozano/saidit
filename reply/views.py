from django.shortcuts import render
from .models import Reply
from django.views.generic import View
# Create your views here.




class ReplyDetailView(View):
    def get(self, request, reply_id):
        template_name = "reply_detail.html"
        reply = Reply.objects.filter(id=reply_id).first()
        context = {"reply": reply}
        return render(request, template_name, context)
