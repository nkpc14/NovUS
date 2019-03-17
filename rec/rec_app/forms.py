from django.forms import ModelForm
from .models import Recruitment


class RecruitmentCreateForm(ModelForm):
    class Meta:
        model = Recruitment
        fields = '__all__'
