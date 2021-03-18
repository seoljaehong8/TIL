### django 초반 설정

- git bash

  > ``` bash
  > django-admin startproject mypjt01
  > python manage.py startapp myapp01
  > ```
  >
  > `mypjt01` 프로젝트가 생성되고 `myapp01` 앱 폴더가 생성된다
  >
  > 프로젝트 폴더 이름은 변경 가능하되 어플리케이션 폴더 이름은 수정 불가능!!!

- `mypjt01/mypjt01/settings.py` 설정

  > ```python
  > INSTALLED_APPS = [
  >     'myapp01',	#추가
  >     '''
  >     
  >     '''
  > ]
  > 
  > LANGUAGE_CODE = 'ko-kr'
  > TIME_ZONE = 'Asia/Seoul'
  > ```
  >
  > `myapp01` 경로 추가
  >
  > 위치와 시간동기화

- `mypjt01/mypjt01/urls.py` 설정

  > ```python
  > from django.contrib import admin
  > from django.urls import path,include
  > 
  > urlpatterns = [
  >     path('admin/', admin.site.urls),
  >     path('myapp01/',include('myapp01.urls'))
  > ]
  > ```
  >
  > `myapp01` 로 서버요청이 오면 `myapp01.urls`로 가라

- `mypjt01/myapp01/ursl.py` 파일 생성

  > ```python
  > from django.urls import path
  > from . import views
  > 
  > urlpatterns = [
  >     path('index/',views.index)
  > ]
  > ```

- `mypjt01/myapp01/views.py` 수정

  > ```python
  > def index(request):
  >     return render(request,'index.html')
  > ```

- `mypjt01/myapp01/templates/index.html`폴더 생성후 index.html 파일 생성

- 템플릿 확장

  > `mypjt01/mypjt01/templates/base.html` 설정 폴더안에 `templates`폴더 생성후 `base.html` 파일 생성
  >
  > ```html
  > <body>
  >   <h1>공통 부분</h1>
  >   {% block content%}
  >   {% endblock %}
  > </body>
  > ```

- `mypjt01/mypjt01/settings.py` 경로설정

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR / 'mypjt01' / 'templates'],
     '''
     
     '''
      }
  ]
  ```

- `mypjt01/myapp01/templates/index.html` 파일 수정

  ```html
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>인덱스</h1>
  {% endblock content %}
  ```

- 현재 디렉토리 구조

  > ![image-20210308194004241](django 초반 설정.assets/image-20210308194004241.png)



- Variable Routing
  - 주소의 일부를 변수에 담아서 사용하는 방법
  - `hello/java` , `hello/python` ... 
  - urls.py 에서 `path('hello/<str:name>/', views.hello)`
  - views.py 에서 변수를 매개변수로 만들어서 받아줘야 한다.
    * `def hello(request, name):`
    * 매개변수의 이름은 urls 에서 정의한 변수명과 같아야 한다.
  - str 은 기본값이므로 생략 `<name>`
  - 숫자는 int 로 표현 `<int:age>`



- Html Form tag
  - 사용자로 부터 입력받은 데이터를 전송하기 위한 태그
  - 설정해야할 속성은 2가지
    * action : 입력 데이터가 전송되는(도착하는, 전달되는) 경로
    * method : http method 를 입력. (GET, POST), 기본값은 (GET)
      * GET : 정보를 조회할 때, 읽어 올 때 
      * POST: 정보의 데이터가 변경점이 있을때. (수정, 삭제, 생성)
  - 전달을 할 때는 반드시 `submit` 동작이 필요.
    * `<input type=submit>`
    * `<button>`

  

- DTL

  * 장고 템플릿에서 사용하는 내장 시스템 언어.
  * 태그와 필터로 구성.
  * `{% 태그 %}`  / `{% value|필터 %}`

  * 값을 표현 할 때 `{{ value }}`

  * 주석 : 한줄`{# #}`, 여러줄 `{% comment %} 사이에 모든 것을 주석 처리 {% endcomment %}`

  * Tags

    * `if / elif / else`
      * in, not, is 사용 가능
    * `for / for empty`
      * forloop : counter, counter0, first, last
    * `lorem [갯수] [단위(w, p, b)] [random]`

    * `now "시간 포멧 형식"`
      * `now "시간포맷형식" as 별명`  를 사용해서 별명을 붙일 수 있다.

  * Filters - `:` 콜론뒤에 공백 없이 적어야 함.

    * `add:숫자`
    * `date:"시간 포멧 형식"`
    * 문자 관련
      * `capfirst` / `lower` / `title` / `upper`
      * `truncatewords:갯수`
      * `truncatechars:갯수` : `...` 도 갯수로 포함된다.
    * `length` 
    * `random`

  

### 템플릿 확장 하는 방법

1. 확장하는 템플릿이 위치할 폴더를 생성한다(택1)

   1. 프로젝트 폴더
   2. 설정 폴더

   - `DIRS`의 경로를 설정해 줘야 한다

   1-1 ` setting.py`에 폴더 경로를 잘 설정한다.

2. 공통적으로 사용되는 템플릿을 정의한다.(base.html)

   - `block` 을 설정해서 상이한 내용이 오는 공간을 확보한다.

3.  사용한다.

   - 템플릿 상단에 `{% extends 'base.html' %}` 을 추가한다.
     - 무조건 최상단에 위치할 수 있게 한다.
   - `block` 사이에 내용을 집어 넣는다.



### URL 분리

1. 설정 폴더의 `urls.py` 에서 분리 준비를 한다.
   - 상단 주석을 참고!! 설정을 한다.
2. application 폴더에 `urls.py` 파일을 생성
   - 기본 구조를 잡아줘야 한다.
   - `path` 함수를 사용하기 위한 import
   - `urlpatterns` 라는 리스트
3. 이제는 application 폴더의 `urls.py`에 경로를 등록하여 사용하면 된다.



## URL namespace

1. `path` 함수 세번째 위치에 `name='별명'` 추가한다.

2. 경로가 필요한 부분 (링크, form action 부분) 에 `url` 템플릿 태그를 이용해서 사용하면 끝

   * `{% url '별명' %}`

   * 단점 : 어플리케이션이 많아지는 경우 동일한 별명이 있을 수 있다.
     * 이러한 경우 어떤 url 인지 구분이 명확하지 않게 됨.
   * 해결 방법 : `app_name` 지정.

3. `app_name` 지정

   * `app_name = 어플리케이션 이름` 
     * app_name 을 설정한 순간 부터는 `{% url '별명' %}` 형식은 사용 불가능.
   * 사용 방법
     * `{% url '설정한app_name:별명'%}` 사용해서 구분을 해준다.



# model

- models.py 에 작성

```python
class Article(models.Model):
    # 길이에 제한이 있는 경우에 사용 필수인자 max_length
    title = models.CharField(max_length=10)
    # 글자수가 많을때, 길이에 제한을 받지 않을때.
	content = models.TextField()
    # 작성일
    created_at = models.DateTimeField(auto_now_add=True)
	# 수정일
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
```

- Migrations
  - django가 model에 생긴 변화를 반영하는 방법
  - 명령어
    - makemigrations
    - migrate
    - sqlmigrate
    - showmigrations
  - **makemigrations**
    - model을 변경한 것에 기반한 새로운 마이그레이션(like 설계도)을 만들때 사용
  - **migrate**
    - 마이그레이션을 DB에 반영하기 위해 사용
    - 설계도를 실제 DB에 반영하는 과정
    - 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸
  - sqlmigrate
    - 마이그레이션에 대한 SQL 구문을 보기 위해 사용
    - 마이그레이션이 SQL문으로 어떻게 해석되어서 동작할지 미리 확인 할 수 있음
  - showmigrations
    - 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
    - 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확인 할 수 있음

# CRUD

- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능인create(생성), read(읽기), update(갱신),delete(삭제)를 묶어서 일컫는 말



- shell_plus

  - `pip install django-extensions`

  - ```python
    INSTALLED_APPS = [
    	'''
        'django_extensions',
    	'''
    ]
    ```

  - `pip install ipython`

  - `python manage.py shell_plus`

  

  - **READ(all,get,filter)**

  - ```shell
    #Article이 가지고있는 데이터 모두 다 보여줘
    In [2]: Article.objects.all()
    Out[2]: <QuerySet []> #=> 리스트로 활용 가능
    
    In [3]: article = Article()
    
    In [5]: article
    Out[5]: <Article: Article object (None)>
    
    In [6]: article.title = 'first'	# 작성
    
    In [7]: article.title
    Out[7]: 'first'
    
    In [8]: article.content = 'django!'	# 작성
    
    In [9]: article.content
    Out[9]: 'django!'
    
    In [12]: article.save()	# 저장
    
    In [13]: article
    Out[13]: <Article: Article object (1)>
    # sqlite에서 확인하면 데이터베이스에 저장된거 확인 가능
    
    In [1]: Article.objects.all()
    Out[1]: <QuerySet [<Article: Article object (1)>]>
    
    # 선언과 동시에 초기화
    In [2]: article = Article(title='second',content='django!!')
    
    In [3]: article
    Out[3]: <Article: Article object (None)>
    
    In [4]: article.save()
    
    In [5]: article
    Out[5]: <Article: Article object (2)>
    
    In [6]: article.pk
    Out[6]: 2
    
    In [7]: article.title
    Out[7]: 'second'
    
    # 클래스를 이용하여 바로 생성
    In [9]: Article.objects.create(title='third',content='django!!!')
    Out[9]: <Article: Article object (3)>
    
    # Article 클래스 안에 __str__ 함수 설정후 출력이 바꼈다. 간단하게
    In [4]: Article.objects.get(pk=1)
    Out[4]: <Article: first>
    
    In [5]: article = Article.objects.get(pk=1)
    
    In [6]: article
    Out[6]: <Article: first>
    
    # 첫번째 객체의 content 내용과 같은 5번째 객체
    In [14]: Article.objects.create(title='5555',content='django!')
    Out[14]: <Article: 5555>
    
    In [17]: Article.objects.get(content='django!')
    error : MultipleObjectsReturned
    # => .get()은 pk로만 활용한다.
    
    #content 내용이 django!인 모든 객체를 반환(queryset 반환)
    In [18]: Article.objects.filter(content='django!')
    Out[18]: <QuerySet [<Article: first>, <Article: 5555>]>
    
    # content에 !가 포함되어 있는 객체들
    In [19]: Article.objects.filter(content__contains='!')
    Out[19]: <QuerySet [<Article: first>, <Article: second>, <Article: third>, <Article: 4444>, <Article: 5555>]>
    # pk 가 1보다 큰
    In [20]: Article.objects.filter(pk__gt=1)
    Out[20]: <QuerySet [<Article: second>, <Article: third>, <Article: 4444>, <Article: 5555>]>  
    ```

  - **create** 하는 3가지 방법

    ```shell
    article = Article()
    article.title = ''
    article.content = ''
    article.save()
    
    article = Article(title='',content='')
    article.save()
    
    Article.objects.create(title='',content='')
    ```

  - **update**

    ```shell
    In [22]: article = Article.objects.get(pk=1)
    
    In [25]: article.title = 'byebye'
    
    In [27]: article.save()
    
    In [28]: article
    Out[28]: <Article: byebye>
    ```

  - **delete**

    ```shell
    In [30]: article.delete()
    Out[30]: (1, {'articles.Article': 1})
    # 현재 테이블에는 2,3,4,5 번의 객체가 남아있다 이상황에서 새로운내용을 추가하면?
    # 6번글이 작성
    ```

    

# admin 등록방법

- admin.py

```python
from django.contrib import admin
# 클래스 모델 입력
from .models import Article

# Register your models here.
admin.site.register(Article)
```

```shell
$ python manage.py createsuperuser
Username (leave blank to use 'user1'): admin
Email address:		# 엔터누르면 스킵 가능(옵션)
Password:
Password (again):
Superuser created successfully.
```





- redirect

```python
from django.shortcuts import render, redirect

def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request,'articles/index.html',context)

def create(request):
	'''
	'''

    return redirect('articles:index')
```



- variable routing

```python
# urls.py
urlpatterns = [
    '''
    '''
    path('detail/<int:id>', views.deatil, name='detail')
]

# views.py
def detail(request,id):
    Article.objects.get(pk=id)

    return render('articles/detail.html')

# index.html
{% extends 'base.html' %}

{% block content %}
  {% for article in articles %}
    <p>제목: <a href="{% utl 'articles:detail' article.id %}">{{article.title}}</a>
  '''
  '''
{% endfor %}
{% endblock content %}

# 두개 넘길경우 띄워쓰기 하고 하나더
<p>제목: <a href="{% utl 'articles:detail' article.id article.title %}">{{article.title}}</a>

```



- dumpdata

```bash
# A 켬퓨터 에서 실행
# 데이터베이스의 데이터들을 더미데이터로 변환
$ python manage.py dumpdata articles.article	#앱이름.모델이름(모델이름은 소문자)
# 4칸씩 들여쓰기 해달라
$ python manage.py dumpdata --indent 4 articles.articles
# 4칸씩 들여쓰기 한 덤프데이터를 movies.json 에 저장해라
$ python manage.py dumpdata --indent 4 articles.articles > articles.json

app폴더/fixtures/articles 폴더 생성
articles.json 파일 이동


# B 컴퓨터 에서 실행
$ python manage.py migrate
# 나의 sqlite에 데이터를 저장한다.
$ python manage.py loaddata articles/articles.json


```



- forms.py

> App 폴더 안에 생성

```python
# forms.py

from django import forms
from .models import Article

# 클래스이름은 models.py 에서 정의한 클래스이름+Form
'''
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
'''
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        # field = ('title','content')
        # 모든 필드를 입력받고 싶을때
        fields = '__all__'
    
  
# views.py
'''
def new(request):
    form = ArticleForm()
    
    context = {
        'form' : form
    }

    return render(request,'articles/new.html',context)

def create(request):
    # 값을 받아서 폼 인스턴스 생성.
    form = ArticleForm(request.POST)

    # 유효성 검사
    if form.is_valid():
        # DB에 저장 (Form으로 작성했을 때)
        # cleaned_data : 유효성 검사를 마치면 cleaned_data를 읽을 수 있다.
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article = Article(title=title,content=content)
        # article.save()

        # DB에 저장 (ModelForm 으로 작성 했을때)
        article = form.save() #return 은 저장된 data의 인스턴스

        return redirect('articles:index')

    # 유효성 검사를 실패한 경우 form에 에러메세지가 저장된다.
    context = {
            'form' : form,
        }

    return render(request,'articles/new.html',context)
'''

# new, create를 하나의 함수로
def create(request):
    if request.method == 'POST':
        # def create 동작 : DB에 저장
        form = ArticleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:index')

    else:
        # def new 동작 : page를 보여주는 
        form = ArticleForm()

    context = {
        'form' : form,
    }
    return render(request,'articles/new.html',context)
        
# new.html
{% extends 'base.html' %}

{% block content %}
  <h2>NEW</h2>
  <hr>
  <form action="" method='POST'>
    {% csrf_token %}
    
    {{form.as_p}}	# p태그로 감싸라(table(tr), p , ul(li))    

    <input type="submit" value="작성하기">
  </form>
{% endblock content %}


# views.py
def edit(request,pk):
    article = Article.objects.get(pk=pk)
    
    if request.method == 'POST':
        # instance 속성값을 안 넣으면 새로운 인스턴스가 생성(edit가 아니라  create된다)
        form = ArticleForm(request.POST,instance=article)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form' : form,
    }

    return render(request,'articles/edit.html',context)
    
# edit.html
{% extends 'base.html' %}

{% block content %}
  <h2>EDIT</h2>  
  <form action="" method="POST">
    {% csrf_token %}
    {{form.as_p}}  
  
    <button>수정</button>
  </form>

{% endblock content %}
```

 



# Static

- 기본 static 경로

  - app_name/static/

- Static Files in settings.py

  - `STATIC_ROOT`
    - collectstatic이 배포를 위해 정적 파일을 수집하는 절대 경로
    - collecstatic : 프로젝트 배포 시 흩어져 있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업
  - `STATIC_URL` 
    - STATIC_ROOT에 있는 정적 파일을 참조 할 대 사용할 URL
  - `STATICFILES_DIRS`
    - app내의 static 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 정의

- app 폴더안에 static 폴더 생성

  - `articles\static\articles\css,img,js\index.css ....`

- load static

  - ```html
    # index.html
    {% load static %}
    {% block css %}
      <link rel="stylesheet" href="{% static 'articles/css/index.css' %}">
    {% endblock css %}
    ```





# Media

- 사용자가 웹에서 업로드 하는 정적 파일(img,pdf ...)

- Media Files in settings.py

  - MEDIA_ROOT
    - 사용자가 업로드 한 파일을 보관할 디렉토리의 절대 경로
    - 실제 해당 파일의 업로드가 끝나면 어디에 파일이 저장되게 할 지 경로
  - MEDIA_URL
    - MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
    - 업로드 된 파일의 주소(URL)를 만들어 주는 역할
  - MEDIA_URL 및 STATIC_URL은 서로 다른 값을 가져야 한다.

- `curd/urls.py`(프로젝틒 폴더 내의 urls.py)

  - ```python
    from django.conf import settings
    from django.conf.urls.static import static
    
    urlpatterns = [
        '''
        '''
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    ```

- `settings.py`

  - ```python
    MEDIA_ROOT = BASE_DIR / 'media'
    MEDIA_URL = '/media/'
    ```

  - `models.py`(image 필드 추가)

  - ```python
    from django.db import models
    
    # Create your models here.
    class Article(models.Model):
    	'''
    	'''
        # 비어있어도 된다.
        image = models.ImageField(blank=True)
        '''
        '''
    
        def __str__(self):
            return self.title
    ```

- `views.py`

  - ```python
    # def create()
    def create(request):
        if request.method == 'POST':
            # request.FILES 추가(사용자가 업로드한 파일)
            form = ArticleForm(request.POST,request.FILES)
    
        '''        
        '''
        return render(request,'articles/new.html',context)
    ```

  - 

- `new.html`

  - ```html
    {% extends 'base.html' %}
    
    {% block content %}
      <h2>NEW</h2>
      <hr>
    <!-- enctype="multipart/form-data" 추가 -->
      <form action="" method='POST' enctype="multipart/form-data">
        {% csrf_token %}
        
        {{form.as_p}}    
    
        <input type="submit" value="작성하기">
      </form>
      <button><a href="{% url 'articles:index' %}">BACK</a></button>
    {% endblock content %}
    ```

- `detail.html`

  - ```html
    <!-- 이미지의 경로를 불러온다 -->
    {% if article.image %}
    <img src="{{ article.image.url }}" alt="{{article.image}}" srcset="">
    {% endif %}
    ```

    