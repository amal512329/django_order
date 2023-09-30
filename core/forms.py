from django.forms  import ModelForm
from .models import LicenseOrder



class LicenseForm(ModelForm):
    class Meta:
        model = LicenseOrder
        fields = "__all__"