# CORS

- pip 설치

```bash
$ pip install django-cors-headers
```

- settings.py 수정

```python
INSTALLED_APPS = [
    '''
    # django cors
    'corsheaders',

    '''
]

MIDDLEWARE = [
    # django cors middleware setting
    # 왠만하면 위쪽에 위치시키는 게좋다 적어도 CommonMiddleware보다는 위에
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 1. 특정 Origin만 선택적으로 허용
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000"
]

# 2. 모든 Origin 허용
# CORS_ALLOW_ALL_ORIGINS = True
```

