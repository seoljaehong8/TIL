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

 

- Widgets

```python
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title', 
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': 'Please enter your content'
        }
    )
    
    class Meta:
        model = Article
        fields = '__all__'
```



- Error message with Bootstrap

```html
<!-- articles/create.html -->

<form action="" method="POST">
  {% csrf_token %}
  {% for field in form %}
    {% if field.errors %}
      {% for error in field.errors %}
        <div class="alert alert-warning" role="alert">{{ error|escape }}</div>
      {% endfor %}
    {% endif %}
    <div class="form-group">
      {{ field.label_tag }} 
      {{ field }}
    </div>
  {% endfor %}
  <button class="btn btn-primary">작성</button>
</form>
```



- Form과 ModelForm의 핵심 차이점
  - Form
    - 어떤 모델에 저장해야 하는지 알 수 없기 때문에 유효성 검사를 하고 실제로 DB에 저장할 때는  `cleaned_data` 와 `article = Article(title=title, content=content)` 를 사용해서 따로 `.save()` 를 해야 한다.
    - Form Class가 `cleaned_data` 로 딕셔너리로 만들어서 제공해 주고, 우리는 `.get` 으로 가져와서 Article 을 만드는데 사용한다.
  - ModelForm
    - django 가 해당 모델에서 양식에 필요한 대부분의 정보를 이미 정의한다.
    - `forms.py` 에 Meta 정보로 `models.py` 에 이미 정의한  Article 을 넘겼기 때문에 어떤 모델에 레코드를 만들어야 할지 알고 있어서 바로 `.save()` 가 가능하다.



# Static

- 기본 static 경로

  - app_name/static/

- Static Files in settings.py

  - `STATIC_ROOT`
    
    - Django 프로젝트에서 사용하는 모든 정적 파일을 한 곳에 모아넣는 경로
    
    - collectstatic이 배포를 위해 정적파일을 수집하는 절대 경로
    
    - DEBUG=True(개발 단계)로 설정되어 있으면 작용하지 않음
    
    - 개발단계에서는 경로를 작성하지 않아도 문제없이 동작
    
    - 즉, 실제 서비스 배포 환경에서 필요한 경로
    
    - collectstatic이 배포를 위해 정적 파일을 수집하는 절대 경로
    
    - collecstatic : 프로젝트 배포 시 흩어져 있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업
    
      > [참고]
      >
      > collectstatic
      >
      > - 프로젝트 배포시 흩어져 있는 정적 파일들을 모아 특정 디렉토리로 옮기는 작업
      >
      > ```python
      > # settings.py 예시
      > 
      > STATIC_ROOT = BASE_DIR / 'staticfiles'
      > ```
      >
      > ```shell
      > $ python manage.py collectstatic
      > ```
    
  - `STATIC_URL` 
    
    - `STATIC_ROOT`에 있는 정적파일을 참조 할 때 사용할 URL
      - 실제 파일이나 디렉토리가 아니며, URL로만 존재
    - 비어 있지 않은 값으로 설정 한다면 반드시 slash(/)로 끝나야 함
    
  - `STATICFILES_DIRS`
    
    - app내의 static 디렉토리 경로를 사용하는 것 외에 추가적인 정적 파일 경로 정의
    
    - ```html
      <!-- base.html -->
      
      <head>
        {% block css %}{% endblock %}
      </head>
      ```
    
    - ```python
      # settings.py​STATICFILES_DIRS = [    BASE_DIR / 'crud' / 'static',]
      ```
    
    - ```html
      <!-- articles/index.html -->
      
      {% extends 'base.html' %}
      {% load static %}
      
      {% block css %}
        <link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
      {% endblock %}
      ```
    
    - ```css
      /* crud/static/stylesheets/style.css */
      
      h1 {
          color: crimson;
      }
      ```

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

- `crud/urls.py`(프로젝트 폴더 내의 urls.py)

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
        #images폴더를 새로 하나만들고 그 안에 저장
        image = models.ImageField(upload_to='images',blank=True)   
        # 날짜별로 저장
        image = models.ImageField(upload_to='images/%Y/%m/%d/',blank=True)
        '''
    
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



# thumbnail (썸네일)

- `pilkit` 모듈 필요 (이미지를 처리하는 프로세서를 지원, Pillow를 이용)
- `django-imagekit` 장고에서 사용할 수 있는 

순서

- `pip install pilkit`

- `pip install django-imagekit`

- ```python
  # settings.py
  INSTALLED_APPS = [
  
      'imagekit',
  
  ]
  ```

- `models.py`

  - ```python
    from django.db import models
    
    from imagekit.models import ProcessedImageField
    from imagekit.processors import Thumbnail
    
    # Create your models here.
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
    
        # blank : 비어있어도 된다.
        # image = models.ImageField(blank=True)
        # images폴더를 새로 하나만들고 그 안에 저장
        # image = models.ImageField(upload_to='images',blank=True)   
        # 날짜별로 저장
        # image = models.ImageField(upload_to='images/%Y/%m/%d/',blank=True)
        # 썸네일 이미지
        image = ProcessedImageField(
            blank=True,
            processors=[Thumbnail(200,300)],
            format='JPEG',
            options={
                'quality' : 80,
            }
        )
    
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    
        def __str__(self):
            return self.title
    ```

    > 위 코드는 주어진 이미지 파일을 썸네일 파일로 수정하는것이고
    >
    > 밑에 코드는 주어진 이미지 파일은 그대로 놔두고 그 이미지를 이용하여 새로운 썸네일 파일을 만드는 것이다.
    
  - ```python
    from django.db import models
    from imagekit.models import ImageSpecField
    from imagekit.processors import ResizeToFill
    
    class Profile(models.Model):
        avatar = models.ImageField(upload_to='avatars')
        avatar_thumbnail = ImageSpecField(source='avatar',
                                          processors=[ResizeToFill(100, 50)],
                                          format='JPEG',
                                          options={'quality': 60})
    
    profile = Profile.objects.all()[0]
    print(profile.avatar_thumbnail.url)    # > /media/CACHE/images/982d5af84cddddfd0fbf70892b4431e4.jpg
    print(profile.avatar_thumbnail.width)  # > 100
    ```
  



# Auth

- Authenticiation
  - 직원인지
  - 인증
  - 자신이 누구라고 주장하는 사람의 신원을 확인하는것

- Authorization
  - 직책
  - 권한,허가
  - 가고 싶은 곳으로 가도록 혹은 원하는 정보를 얻로고 허용하는 과정
- Django Authentication Syste
  - 인증과 권한부여를 함께 제공
  - django에서는 이러한 기능이 어느정도 결홥되어 일반적으로 `authentication system(인증 시스템)`이라고 한다
  - 크게 `User object`와 `Web request`

- django는 기본적으로 인증에 관련된 `built-in form`들을 제공
  - 회원가입(UserCreationForm), 로그인(AuthenticationsForm)등
- 로그인
  - 로그인은 세션을 create하는 로직과 같다
  - login()
    - Request 객체와 User객체를 통해 로그인
    - Django의 session framework를 통해 사용자의 ID를 세션에 저장

```python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .forms import CustomUserChangeForm

def login(request):
    # 로그인 상태면 로그인 화면으로 가지말고 index화면으로 
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        #form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            # 세션 CREATE
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()

    context = {
        'form' : form,
    }

    return render(request,'accounts/login.html',context)
```



- 로그아웃
  - 로그아웃은 세션을 delete하는 로직과 같다
  - logout()
    - Request객체를 받으며 return이 없다
    - 현재 요청에 대한 DB의 세션 데이터를 삭제하고 클라이언트 쿠키에서도 sessionid를 삭제

```python
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```



- 회원가입

```python
@require_http_methods(['GET','POST'])
def signup(request):
    # 로그인이 되어 있다면
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    
    context = {
        'form' : form,
    }

    return render(request,'accounts/signup.html',context)
```



- 회원탈퇴

```python
@require_POST
def delete(request):
     # 만약 탈퇴하는 사용자의 세션 또한 삭제하고 싶다면 탈퇴 후 로그아웃 함수 호출
        # 로그아웃과 탈퇴의 순서가 바뀌면 안됨 (먼저 로그아웃 해버리면 해당 요청 정보가 없어지기 때문에 탈퇴에 필요한 정보가 없어짐)       
    if request.user.is_authenticated:
        request.user.delete()
    return redirect('articles:index')
```



- 회원정보수정

```python
@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form' : form,
    }

    return render(request,'accounts/update.html',context)
```



- forms.py

```python
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):

    class Meta():
        model = get_user_model()
        fields = ('email','first_name','last_name')
```



- base.html

```html
<body>
  <div class="container">
    <h3>Helllo, {{ request.user }}</h3>
    
    {% if request.user.is_authenticated  %}
      <a href="{% url 'accounts:update' %}">회원정보수정</a>
      <form action="{% url 'accounts:logout' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="Logout">
      </form>    
      <form action="{% url 'accounts:delete' %}" method="POST">
        {% csrf_token %}
        <input type="submit" value="회원탈퇴">
      </form>
    {% else %}
      <a href="{% url 'accounts:login' %}">Login</a>
      <a href="{% url 'accounts:signup' %}">Signup</a>
    {% endif %}

    {% block content %}
    {% endblock %}
  </div>
  {% bootstrap_javascript %}
</body>
```



- user list

```python
# views.py
from django.contrib.auth.forms import get_user_model
def userlist(request):
    users = get_user_model().objects.all()

    context = {
        'users' : users,
    }

    return render(request,'accounts/userlist.html',context)
```

```html
# userlist.html
{% extends 'base.html' %}

{% block content %}
  {% for user in users1 %}
    <p>username : {{user.username}}</p>
    <p>useremail : {{user.email}}</p>
    <hr>
  {% endfor %}
{% endblock content %}
```



- change password

```python
# views.py
def change_pw(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('accounts:update')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form' : form,
    }
    
    return render(request,'accounts/change_pw.html',context)
```



# Snippets

> 내가 원하는 단축키를 설정할수 있다
>
> 원하는 코드 형식을등록하여 빠르게 코딩 가능
>
> html 파일에서 `!` 를 누르는 경우와 비슷
>
> https://snippet-generator.app/ (문법 자동 변환)

```json
{
	// "Print to console": {
	// 	"scope": "javascript,typescript",	# 어떤 언어에서 우리의 스니펫을 작동시킬것인지
	// 	"prefix": "log",	# 단축키(ex : !)
	// 	"body": [
	// 		"console.log("$1");",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }

	"BASE HTML" : {
		"scope" : "html, django-html",
		"prefix": "base html",
		"body": [
			"<!DOCTYPE html>",
			"<html lang=\"en\">",
			"<head>",
			"	<meta charset=\"UTF-8\">",
			"	<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">",
			"	<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
			"	<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl\" crossorigin=\"anonymous\">",
			"	<title>Document</title>",
			"</head>",
			"<body>",
			"",	
			"	<div class=\"container\">",
			"		{% block content %}",
			"		{% endblock content %}",
			"	</div>",
			"",	
			"	<script src=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js\" integrity=\"sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0\" crossorigin=\"anonymous\"></script>",
			"</body>",
			"</html>"
		],
		"description": "Django Base Html"
	},

	"Base Template" : {
		"scope": "html, django-html",
		"prefix": "base template",
		"body": [
			"{% extends 'base.html' %}",
			"",
			"{% block content %}",
			"$0",
			"{% endblock content %}"
		]
	}
}
```





# Model Relationship

## Foreign Key

**개념**

- 외래 키(외부 키)
- RDBMS에서 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키
- 참조하는 테이블에서 1개의 키(속성 또는 속성의 집합)에 해당하고 이는 참조되는 측의 테이블의 기본 키를 가리킴
- 참조하는 테이블의 속성의 행 1개의 값은, 참조되는 측 테이블의 행 값에 대응
  - 이 때문에 참조하는 테이블의 행에는, 참조되는 테이블에 나타나지 않는 값을 포함할 수 없음
- 참조하는 테이블의 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음

**특징**

- 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무결성)
- 외래 키의 값이 부모 테이블의 기본 키 일 필요는 없지만 유일해야 함



## ForeignKey field

> A many-to-one relationship

- 2개의 필수 위치 인자가 필요
  - 참조하는 model class
  - on_delete 옵션



## 1:N model manager

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```

`on_delete`

- ForeignKey의 필수 인자이며, ForeignKey가 참조하고 있는 부모(Article) 객체가 사라졌을 때 달려 있는 댓글들을 어떻게 처리할 지 정의
- Database Integrity(데이터 무결성)을 위해서 매우 중요한 설정이다.



**possible values for `on_delete`**

- `CASCADE` : **부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제**
- `PROTECT` 
- `SET_NULL`
- `SET_DEFAULT`
- `SET()`
- `DO_NOTHING` 
- `RESTRICT`



**1 : N 관계 manager**

- **Article(1)** : **Comment(N)** : `comment_set`
  - `article.comment` 형태로는 가져올 수 없다. 
  - 게시글에 몇 개의 댓글이 있는지 Django ORM이 보장할 수 없기 때문
  - 본질적으로는 Article 클래스에 Comment 와의 어떠한 관계도 연결하지 않음
- **Comment(N)** : **Article(1)** : `article`
  - 댓글의 경우 어떠한 댓글이든 반드시 자신이 참조하고 있는 게시글이 있으므로 `comment.article`와 같이 접근할 수 있음



## Comment 관련 추가 사항

### 댓글 개수 출력

```html
# 1. {{ comments|length }}

# 2. {{ article.comment_set.all|length }}

# 3. {{ comments.count }} 
```





# custom authentication

## User model 대체하기

- 일부 프로젝트에서는 Django의 내장 유저 모델이 제공하는 인증 요구사항이 적절하지 않을 수 있다.
- django는 custom model을 참조하는 `AUTH_USER_MODEL` 설정을 제공하여 default user model을 재정의(override)할 수 있도록 한다.
- django는 새 프로젝트를 시작하는 경우 기본 사용자 모델이 충분하더라도 커스텀 유저 모델을 설정하는 것을 강력하게 권장(highly recommended)
  - 커스텀 유저 모델은 기본 사용자 모델과 동일하게 작동하지만 필요한 경우 나중에 맞춤 설정할 수 있기 때문이다.
- **단, 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 한다.**

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User' 

# accounts/models.py

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


admin.site.register(User, UserAdmin
```



### AUTH_USER_MODEL

- User를 나타내는데 사용하는 모델

- 주의 사항

  - 프로젝트를 진행하는 동안 (즉, 프로젝트에 의존하는 모델을 만들고 마이그레이션 한 후) 설정은 변경할 수 없다. (변경하려면 큰 노력이 필요)
  - 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야 함

  

**데이터베이스 초기화 후 마이그레이션 (프로젝트 중간이라면)**

1. migrations 파일 삭제
2. db.sqlite3 삭제
3. migrations 진행



**`AbstractUser` vs `AbstractBaseUser`**

- `AbstractBaseUser`
  - password 와 last_login 만 기본적으로 제공
  - 자유도가 높지만 필요한 필드는 모두 작성해야 함
- `AbstractUser`
  - 관리자 권한과 함께 완전한 기능을 갖춘 사용자 모델을 구현하는 기본 클래스



## Custom user and built-in auth forms

- 유저모델 대체 후 회원가입 시 에러 발생
- AbstractBaseUser의 모든 subclass와 호환되는 forms
  - AuthenticationForm, SetPasswordForm, PasswordChangeForm, AdminPasswordChangeForm
- User와 연결되어 있어서 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms
  - UserCreationForm, UserChangeForm

```python
# accounts/forms.py

from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('email',)
```



`settings.AUTH_USER_MODEL`

- 유저 모델에 대한 외래 키 또는 다대다 관계를 정의 할 때 사용
- models.py에서 유저 모델을 참조할 때 사용

<br>

`get_user_model()`

- django는 User를 직접 참조하는 대신 django.contrib.auth.get_user_model()을 사용하여 사용자 모델을 참조해야 한다고 권장
- 현재 활성화(active)된 user model을 반환
  - 커스텀한 유저 모델이 있을 경우는 커스텀 유저 모델, 그렇지 않으면 User를 반환
  - 이것이 User를 직접 참조하지 않는 이유
- models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용

```python
# articles/models.py

from django.conf import settings


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

```shell
$ python manage.py makemigrations
```

```shell
# 첫번째 상황(null 값이 허용되지 않는 user_id 가 아무 값도 없이 article 에 추가되려 하기 때문)
$ python manage.py makemigrations
You are trying to add a non-nullable field 'user' to article without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: # 1 입력하고 enter

# 두번째 상황(그럼 기존 article 의 user_id 로 어떤 데이터를 넣을건지 물어봄)
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> # 1 입력하고 enter (그럼 현재 작성된 모든 글은 1번 user가 작성한 것으로 됨)
```

```shell
$ python manage.py migrate
```



# ManyToManyField

**Arguments**

- `related_name`

  - ForeignKey의 related_name과 동일

- `through`

  - django는 다대다 관계를 관리하는 중개 테이블을 자동으로 생성한다.
  - 하지만, 중간 테이블을 직접 지정하려면 through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정할 수 있다.
  - 일반적으로 추가 데이터를 다 대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용

- `symmetrical`

  - ManyToManyField가 동일한 모델을 가리키는 정의에서만 사용

  ```python
  from django.db import models
  
  class Person(models.Model):
      friends = models.ManyToManyField('self')
  ```

  - 예시처럼 동일한 모델을 가리키는 정의의 경우 django는 Person 클래스에 person_set 매니저를 추가 하지 않는다.
  - 대신 대칭적(`symmetrical`)이라고 간주하며, source 인스턴스가 target 인스턴스를 참조하면 target 인스턴스도 source 인스턴스를 참조하게 된다.
  - 즉, 내가 당신의 친구라면 당신도 내 친구가 된다.
  - self와의 관계에서 대칭을 원하지 않는 경우 `symmetrical=False`로 설정한다.

**Related manager**

- 1:N 또는 M:N 관련 컨텍스트에서 사용되는 매니저
- 같은 이름의 메서드여도 각 관계(1:N, M:N)에 따라 다르게 사용 및 동작
  - 1:N에서는 target 모델 객체만 사용 가능
  - M:N 관계에서는 관련된 두 객체에서 모두 사용 가능

**methods**

- `add()`
  - "지정된 객체를 관련 객체 집합에 추가"
  - 이미 존재하는 관계에 add()를 사용하면 관계가 복제되지 않음
- `remove()`
  - "관련 객체 집합에서 지정된 모델 개체를 제거"
  - QuerySet.delete()를 사용하여 관계가 삭제됨
- clear(), set(), create()

**데이터베이스에서의 표현**

- django는 다대다 관계를 나타내는 중개 테이블(intermediary join table)을 만든다.
- 테이블 이름은 앱이름 및 ManyToManyField의 이름과 이를 포함하는 모델의 이름을 조합하여 생성한다.

**중개 테이블 필드 생성 규칙**

1. 소스(source model) 및 대상(target model) 모델이 다른 경우
   - id
   - `<containing_model>_id`
   - `<other_model>_id`
2. ManyToManyField가 동일한 모델을 가리키는 경우
   - id
   - `from_<model>_id`
   - `to_<model>_id`



## LIKE

**model 설정**

```python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    ...
```

```bash
$ python manage.py makemigrations
```

- **현 상황에서는 `related_name` 작성이 필수**
  - M:N 관계 설정 시에 `related_name` 이 없다면 자동으로 `.article_set` 매니저를 사용할 수 있도록 하는 데 이 매니저는 이미 이전 1:N(User:Article) 관계에서 사용 중인 매니저이다.
  - user가 작성한 글들(`user.article_set`)과 user가 좋아요를 누른 글(`user.article_set`)을 django는 구분할 수 없게 된다.
  - user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 `related_name` 추가 작성이 필요하다.

- **이제 사용 가능한 manager는 다음과 같다.**
  - `article.user` : 게시글을 작성한 유저 - 1:N
  - `article.like_users` : 게시글을 좋아요한 유저 - M:N
  - `user.article_set`: 유저가 작성한 게시글들 → 역참조 - 1:N
  - `user.like_articles`: 유저가 좋아요한 게시글들 → 역참조 - M:N



**좋아요 구현**

- `exists()`
  - 최소한 하나의 레코드가 존재하는지 여부를 확인하여 알려 준다. 
- 쿼리셋 cache를 만들지 않으면서 특정 레코드가 존재하는지 검사한다.
  - 결과 전체가 필요하지 않은 경우 유용하다.

```python
# articles/urls.py

urlpatterns = [
    ...,
    path('<int:article_pk>/likes/', views.likes, name='likes'),
]
```

```python
# articles/views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```

```django
<!-- articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p><b>작성자 : {{ article.user }}</b></p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <div>
      <form action="{% url 'articles:likes' article.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <button>좋아요 취소</button>
        {% else %}
          <button>좋아요</button>
        {% endif %}
      </form>
    </div>
    <p>{{ article.like_users.all|length }} 명이 이 글을 좋아합니다.</p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
{% endblock %}
```

- 좋아요 버튼 누른 후 데이터베이스 확인



## Profile

- 자연스러운 follow 흐름을 위한 프로필 페이지 작성

```python
# accounts/urls.py

path('<username>/', views.profile, name='profile'),
```

```python
# accounts/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

```html
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>

<hr>

<h2>{{ person.username }}'s 게시글</h2>
{% for article in person.article_set.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}'s 댓글</h2>
{% for comment in person.comment_set.all %}
  <div>{{ comment.content }}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}'s likes</h2>
{% for article in person.like_articles.all %}
  <div>{{ article.title }}</div>
{% endfor %}

<hr>

<a href="{% url 'articles:index' %}">back</a>
{% endblock  %}
```

```html
<!-- base.html -->

<body>
  <div class="container">
    <h3>Hello, {{ request.user }}</h3>
    {% if request.user.is_authenticated %}
      <a href="{% url 'accounts:profile' request.user.username %}">내 프로필</a>
      <a href="{% url 'accounts:update' %}">[회원정보수정]</a>
      ...
    {% else %}
```

```html
<!-- articles/index.html -->

<p>
  <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
</p>
```



## FOLLOW

**models 작성**

```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- `accounts_user_followings` 중개 테이블 생성 확인

**Follow 구현**

> 자기자신은 follow 하면 안된다.

```python
# accounts/urls.py

urlpatterns = [
    ...,
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```

```python
# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if person != request.user:
            if person.followers.filter(pk=request.user.pk).exists():
            # if request.user in person.followers.all():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
```

**templates**

```html
<!-- accounts/profile.html -->

<div> 
  <div>
    팔로잉 : {{ person.followings.all|length }} / 팔로워 : {{ person.followers.all|length }}
  </div>
  {% if request.user != person %}
    <div>
      <form action="{% url 'accounts:follow' person.pk %}" method="POST">
        {% csrf_token %}
        {% if request.user in person.followers.all %}
          <button>Unfollow</button>
        {% else %}
          <button>Follow</button>
        {% endif %}
      </form>
    </div>
  {% endif %}
</div>
```

**`with` template tag**

- 더 간단한 이름으로 복잡한 변수를 저장한다.

- 주로 데이터베이스에 중복으로 여러번 엑세스 할 때 유용하게 사용한다.
- 변수는 `{% with %}` and `{% endwith %}` 사이에서만 사용 가능하다.

```html
<!-- accounts/profile.html -->

{% with followings=person.followings.all followers=person.followers.all %}
  <div> 
    <div>
      팔로잉 : {{ followings|length }} / 팔로워 : {{ followers|length }}
    </div>
    {% if request.user != person %}
      <div>
        <form action="{% url 'accounts:follow' person.pk %}" method="POST">
          {% csrf_token %}
          {% if request.user in followers %}
            <button>Unfollow</button>
          {% else %}
            <button>Follow</button>
          {% endif %}
        </form>
      </div>
    {% endif %}
  </div>
{% endwith %}
```

