from    django import forms
from .models import asset,platform


class FileForm(forms.Form):
    file = forms.FileField(label="导入资产")


class AssetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    class Meta:
        model = asset
        fields = '__all__'

        labels = {
            "network_ip": "外网IP",
        }
        widgets = {
            'ctime': forms.DateInput(
                attrs={'type': 'date', }
            ),
            'utime': forms.DateInput(
                attrs={'type': 'date', }
            ),
            'ps': forms.Textarea(
                attrs={'cols': 80, 'rows': 3}
            ),
            'platform': forms.Select(
                attrs={'class': 'select2',
                       'data-placeholder': ('----请选择平台----')}),
            'manager': forms.Select(
                attrs={'class': 'select2',
                       'data-placeholder': ('----请选择负责人----')}),
            'region': forms.Select(
                attrs={'class': 'select2',
                       'data-placeholder': ('----请选择区域----')}),
            'project': forms.Select(
                attrs={'class': 'select2',
                       'data-placeholder': ('----请选择项目----')}),

        }
        help_texts = {
            'hostname': '*  必填项目,名字唯一',
            'platform': '*  必填项目',
            'manager': '*  必填项目',
            "ctime": '*  必填项目',
            "utime": '*  必填项目',
            'project': '*  必填项目'
        }
        error_messages = {
            'model': {
                'max_length': ('太短了'),
            }
        }




