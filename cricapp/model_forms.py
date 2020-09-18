from django.forms import ModelForm
from .models import *


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
