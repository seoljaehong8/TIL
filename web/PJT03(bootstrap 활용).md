# PJT 03(2021-02-05)

> 이번 프로젝트에서는 Bootstrap을 이용하여 웹 페이지를 구성해보았다.
>
> 이번 raedme 에서는 나중에 쉽게 찾아볼 수 있도록 각각의 기능을 구현하는 코드위주로 작성해보았다.



- 항상 까먹는 html 파일안에 링크 올려주기

```html
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">    
</head>  


<body>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

</body>
```



- nav-bar

  > 여기서는 기본 nav-bar를 구성하고 화면이 작아지면 3메뉴표시가 표시되록 하였다.
  >
  > sticky-top 클래스를 주며 항상 상단에 고정되도록 하였다.
  >
  > 로그인 메뉴를 클릭하였을때 modal창이 뜨며 로그인창이 나타나오게 하였다. 여기서 주의할점은 <nav> 태그 안에 modal 기능을 구현하였을때 화면이 흐려지며 로그인 창이 클릭이 안된다는 점이었다. 혹시 기능상 문제가 생긴다면 modal class를 nav태그 밖으로 구성하자.

```html
<nav class="sticky-top navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container-fluid  bg-dark">
      <a href="02_home.html">
        <img src="images/logo.png" alt="Cinema">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link active text-white text-decoration-none" aria-current="page" href="02_home.html">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-white text-decoration-none" href="03_community.html">Community</a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-white text-decoration-none" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">
              Login
            </a>
            <!-- Modal -->
          </li>          
        </ul>        
      </div>
    </div>
  </nav>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Login</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label">Username</label>
              <input type="email" class="form-control" id="exampleInputEmail1">                    
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label">Password</label>
              <input type="password" class="form-control" id="exampleInputPassword1">
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="exampleCheck1">
              <label class="form-check-label" for="exampleCheck1">Check me out</label>
            </div>                  
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="submit" class="btn btn-primary">Submit</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</nav>
```



- footer

  > fixed-bottom 클래스를 주며 항상 하단에 고정되도록 하였다.
  >
  > 본문과의 내용겹침을 방지하기 위하여 bgcolor을 흰색으로 주어 구분하였다.

```html
<footer class="fixed-bottom text-center footer_bgcolor">
    <p>Web-bootstrap PJT, by JaeHong Seol</p>
</footer>
```

```css
.footer_bgcolor {
  height: 30px;
  background-color: white;
}
```



- carousel

  > bootstrap의 carousel 클래스를 주어 여러장의 사진을 직접 넘겨보거나 자동으로 다음 사진으로 넘어가도록 기능을  추가하였다.

```html
<header>
    <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="2000">
          <img src="images/header1.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item" data-bs-interval="2000">
          <img src="images/header2.jpg" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item" data-bs-interval="2000">
          <img src="images/header3.jpg" class="d-block w-100" alt="...">
        </div>
      </div>
      <a class="carousel-control-prev" href="#carouselExampleInterval" role="button" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </a>
      <a class="carousel-control-next" href="#carouselExampleInterval" role="button" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </a>
    </div>
  </header>
```



- card

  >  bootstrap의 card 클래스를 사용하여 화면 너비에 맞춰 3장, 2장, 1장 씩 영화들의 정보를 담은 카드들을 보여주었다.

```html
<section>
    <div class="container">
      <article>
        <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-6">
          <div class="col my-5 pb-5">
            <div class="card">
              <img src="images/movie5.jpg" class="card-img-top" alt="...">
              <div class="card-body text-center">
                <h5 class="card-title">LEON</h5>
                <p class="card-text">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Vero delectus, aperiam aliquid voluptas illum doloremque necessitatibus ratione.</p>
              </div>
            </div>
          </div>
          <div class="col my-5 pb-5">
            <div class="card">
              <img src="images/movie6.jpg" class="card-img-top" alt="...">
              <div class="card-body text-center">
                <h5 class="card-title">Joker</h5>
                <p class="card-text">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Amet, doloremque enim? Excepturi dignissimos qui dicta. Itaque asperiores nobis modi facere!</p>
              </div>
            </div>
          </div>
        </div>
      </article>
    </div>
  </section>
```



- table	

  > bootstrap의 table 클래스를 이용하여 표를 만들었다.
  >
  > pagination 클래스를 이용하여 표 목록을 앞 뒤로 넘어갈 수 있는 기능을 만들었다.
  >
  > section class에서 d-none, d-lg-block 의 기능으로 화면너비에 따라 이 표가 사라졌다가 다시 보였다가 하는 기능도 추가하였다.

```html
<div class="main container">
    <div class="row">
        <section class="col-0 col-lg-10 d-none d-lg-block">
        <table class="table table-striped table-hover">
          <thead>
            <tr class="text-center bg-dark text-white">
              <th scope="col">영화 제목</th>
              <th scope="col">글 제목</th>
              <th scope="col">작성자</th>
              <th scope="col">작성시간</th>
            </tr>
          </thead>
          <tbody class="text-center">
            <tr>
              <th scope="row">Great Movie Title</th>
              <td>Movie Ever</td>
              <td>user</td>
              <td>1 minutes ago</td>
            </tr>
            <tr>
              <th scope="row">Great Movie Title</th>
              <td>Movie Ever</td>
              <td>user</td>
              <td>1 minutes ago</td>
            </tr>
          </tbody>
        </table>
        <nav aria-label="Page navigation" class="d-flex justify-content-center">
          <ul class="pagination">
            <li class="page-item"><a class="page-link" href="#">Previous</a></li>
            <li class="page-item"><a class="page-link" href="#">1</a></li>
            <li class="page-item"><a class="page-link" href="#">2</a></li>
            <li class="page-item"><a class="page-link" href="#">3</a></li>
            <li class="page-item"><a class="page-link" href="#">Next</a></li>
          </ul>
        </nav>   
      </section>
```



> flex, grid 기능을 굉장히 많이 사용하였으며 두 기능을 적절히 잘 써주어 내가 원하는 기능을 충분히 만들수 있게 공부할 것!!!
>
> breakingpoint 가 중요한데 그 기준을 다시 한번 보고 넘어가도록 하자.
>
> xs : 576px 이하
>
> sm : 576px 이상
>
> md : 768px 이상
>
> lg : 992px 이상
>
> xl : 1200px 이상
>
> xxl : 1400px 이상



















