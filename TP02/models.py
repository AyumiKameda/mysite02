from django.db import models

# Create your models here.
class Goods(models.Model):
    """商品モデル"""
    class Meta:
        #テーブル名を定義
        db_table = 'goods'

    #テーブルのカラムに対応するフィールドを定義
    title = models.CharField(verbose_name='タイトル', max_length=255)
    price = models.IntegerField(verbose_name='価格', null=True, blank=True)

    def __str__(self):
        return self.title