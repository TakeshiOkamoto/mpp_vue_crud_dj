import json

from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.db import connection, transaction

from .models import VueCrudData


# 表示
class IndexView(TemplateView):
    template_name = 'vue_crud_data/index.html'


# 初期化
class InitView(View):

    def get(self, request, *args, **kwargs):

        try:
            with transaction.atomic(): 
                with connection.cursor() as cursor:
                    cursor.execute('TRUNCATE TABLE vue_crud_data;')
                    cursor.execute('INSERT INTO vue_crud_data' 
                                    ' SELECT * FROM vue_crud_data_bk;')
        except Exception as e:
            pass
        return redirect('vue_crud_data:index')


# API
class APIView(View):

    def get(self, request, *args, **kwargs):
    
        # JSONデータの生成
        items = VueCrudData.objects.order_by('updated_at').reverse()
        data = []
        for item in items:
            data.append({
                'id'        : item.id,
                'name'      : item.name,
                'comment'   : item.comment,
                'created_at': str(item.created_at).replace('+00:00',''),
                'updated_at': str(item.updated_at).replace('+00:00',''),
            })
            
        # JSONは次のような形式となる
        #  [
        #    {"id": 1, "name": "プチモンテ"}
        #    {"id": 2, "name": "プチラボ"  }
        #    {"id": 3, "name": "@ゲーム"   }
        #  ]                                    
        return HttpResponse(json.dumps(data, ensure_ascii=False))
        

    def post(self, request, *args, **kwargs):
    
        try:            
            # JSONデータの読み込み
            param = json.loads(request.body)
            
            # データの登録
            vue_crud_data = VueCrudData()
            vue_crud_data.name = param['name']
            vue_crud_data.comment = param['comment']

            with transaction.atomic():
                vue_crud_data.save()

            data = {
               'msg'       : 'Ajaxによるデータの登録が成功しました。',
               'id'        : vue_crud_data.id,
               'name'      : vue_crud_data.name,
               'comment'   : vue_crud_data.comment,
               'updated_at': str(vue_crud_data.updated_at) \
                                .replace('+00:00',''),
            }
            return HttpResponse(json.dumps(data, ensure_ascii=False))
        except Exception as e:
            data = {
                'msg' : 'Ajaxによるデータの登録が失敗しました。',
                'id'  : 'error'
            }
            return HttpResponse(json.dumps(data, ensure_ascii=False))
            
    def put(self, request, *args, **kwargs):
    
        try:            
            # JSONデータの読み込み
            param = json.loads(request.body)
            
            # データの更新
            vue_crud_data = VueCrudData.objects \
                    .get(id=request.GET['id'])
            vue_crud_data.name = param['name']
            vue_crud_data.comment = param['comment']

            with transaction.atomic():
                vue_crud_data.save()

            data = {
               'msg' : 'Ajaxによるデータの更新が成功しました。',
            }
            return HttpResponse(json.dumps(data, ensure_ascii=False))
        except Exception as e:
            data = {
                'msg' : 'Ajaxによるデータの更新が失敗しました。',
            }
            return HttpResponse(json.dumps(data, ensure_ascii=False))
                
    def delete(self, request, *args, **kwargs):
     
        try:            
            # データの削除
            vue_crud_data = VueCrudData.objects \
                    .get(id=request.GET['id'])

            with transaction.atomic():
                vue_crud_data.delete()

            data = {'msg': 'Ajaxによるデータの削除が成功しました。'}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
        except Exception as e:
            data = {'msg': 'Ajaxによるデータの削除が失敗しました。'}
            return HttpResponse(json.dumps(data, ensure_ascii=False))

    
