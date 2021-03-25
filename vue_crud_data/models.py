from django.db import models
from django.core.validators import MaxLengthValidator

# CRUD
class VueCrudData(models.Model):

    class Meta:
        db_table = 'vue_crud_data'
        verbose_name = 'CRUD'

    # 名前
    name = models.CharField(verbose_name='名前', \
        max_length=100, default='', \
        validators=[MaxLengthValidator(100)])

    # コメント
    comment = models.TextField(verbose_name='コメント', 
        max_length=1000, default='', \
        validators=[MaxLengthValidator(1000)])

    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<id=' + str(self.id) + ', name=' + self.name + '>'

# CRUD(BK)
class VueCrudDataBk(models.Model):

    class Meta:
        db_table = 'vue_crud_data_bk'
        verbose_name = 'CRUD(BK)'

    # 名前
    name = models.CharField(verbose_name='名前', \
        max_length=100, default='', \
        validators=[MaxLengthValidator(100)])

    # コメント
    comment = models.TextField(verbose_name='コメント', 
        max_length=1000, default='', \
        validators=[MaxLengthValidator(1000)])

    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<id=' + str(self.id) + ', name=' + self.name + '>'
