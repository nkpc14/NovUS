from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView
from .forms import RecruitmentCreateForm
# Create your views here.
from .models import Recruitment
from django.http import HttpResponse


class RecruitmentView(CreateView):
    model = Recruitment
    form_class = RecruitmentCreateForm
    template_name = "rec_app/rec_app.html"
    success_url = "/"

    def form_valid(self, form):
        # form.instance.user = self.request.user
        return super(RecruitmentView, self).form_valid(form)
