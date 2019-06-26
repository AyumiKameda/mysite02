from django.shortcuts import render
from django.views import View



import logging
from django.views import generic
from .models import Goods
from .forms import GoodsSearchForm
from django.db.models import Q


class IndexView(generic.ListView):

    #paginate_by = 5
    template_name = 'TP02/index.html'
    # この行で変数名を指定
    context_object_name = 'goods_list'
    model = Goods
    #def post()でセッションに検索フォームの値を渡す。
    def POST(self, request, *args, **kwargs):

        form_value = [
            self.request.POST.get('title', None),
            self.request.POST.get('price', None),
        ]
        request.session['form_value'] = form_value


    #def get_queryset()でセッションから取得した検索フォームの値に応じてクエリ発行を行う。
    def get_queryset(self):

        # sessionに値がある場合、その値でクエリ発行する。
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            price = form_value[1]

            # 検索条件
            condition_title = Q()
            condition_price = Q()

            if len(title) != 0 and title[0]:
                condition_title = Q(title__contains=title)
            if len(price) != 0 and price[0]:
                condition_price = Q(price__contains=price)

            return Goods.objects.select_related().filter(condition_title & condition_price)
        else:
            # 何も返さない
            return Goods.objects.none()

    #def get_context_data()でセッションから検索フォームの値を取得して、検索フォームの初期値としてセットする。
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
        title = ''
        price = ''
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            price = form_value[1]

        default_data = {'title': title,  # タイトル
                        'price': price,  # 内容
                        }

        test_form = GoodsSearchForm(initial=default_data) # 検索フォーム
        context['test_form'] = test_form

        return context