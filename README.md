# 垃圾邮件识别系统


# 备忘
## url 反向生成(别名):
```
@app.route('/index', methods=['GET'], endpoint='n1')
v1 = url_for('n1')
```

## 路由转换(可自定义转换器):
 @app.route('/index/<int:nid>', methods=['GET'])  
 def index(nid):  
 转换器: <username>(默认字符串), int, float, path, uuid(用于生成唯一标识)

## app.route参数
 default=xx 函数默认参数值  
 redirect_to='/url' 重定向  
 subdomain

## 请求相关
 request.method, args, form, values, cookies, headers, path, url, host, files

## 相应相关
```
return ""
return json.dumps({}) # return jsonify({})
return render_template('index.html', n1=123)
return redirect('/index')
from flask import make_response
response = make_response(render_template('index.html'))
response.set_cookie('key', 'value')
response.delete_cookie('key')
response.headers['X-somthing'] = 'A-value'
return response
```

## 模板
```传参:  
{{ k1 }}, {{ k2[0] }}, {{ k3.name }}, {{ k3.get('name', 888) }}  
传函数:  
def fun(value):  
     return ("<h1> title: '%s' </h1>" %value)  
     return Markup("<h1> title: '%s' </h1>" % value)  
{{ k4(9)|safe }}  
@app.template_global() # 全局函数, 每个模板都可以用  
def fun():  
```

## 装饰器
```
app.before_request  
app.after_request, 被装饰函数需要有参数和返回参数, 用来传递, 注意多个时执行顺序相反  
@app.before_request  
def check_login():  
  if request.path=='/login':
      return None
  user = session.get('user_info')
  if not user:
      return redirect('/login')
app.errorhandler(404)

flash, 通过session实现, 取后即删, category可选
flash('msg', category='x1') = "message"
data = get_flashed_messages(category_filter=['x1'])

Middleware(app.wsgi_app) 中间件
```

## 蓝图
ad = Blueprint('ad', __name__, url_prefix='/admin', static_floder='', templete_floder='')  
分发路由  
目录划分  
定制 before_request  



