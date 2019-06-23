from django import forms

class GoodsSearchForm(forms.Form):
    title = forms.CharField(
        initial='',
        label='商品名',
        required = False, # 必須ではない
    )
    price = forms.IntegerField(
        initial='',
        label='価格',
        required=False,  # 必須ではない
    )
