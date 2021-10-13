from django.shortcuts import render
from .models import Reply
from django.views.generic import View
# Create your views here.




class ReplyDetailView(View):
    def get(self, request, reply_id):
        template_name = "post_detail.html"
        reply = Reply.objects.get(id=reply_id)
        replies = reply.get_descendants(include_self=False)
        context = {
                    "reply": reply,
                    "replies": replies
                    }
        return render(request, template_name, context)



class CreateReplyView(View):
    ...
