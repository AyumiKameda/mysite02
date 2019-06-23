from django.contrib import admin #←adminサイトテンプレ読み込み
from .models import Goods #←model定義TBL読み込み

#adminサイトのメソッドでGoods登録
admin.site.register(Goods)