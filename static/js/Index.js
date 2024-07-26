{% extends 'base.html' %}
{% load static %}
{% block title %}
LATESTNEWS
{% endblock %}

{% block x %}
<style>
    .pic:hover
    {
    box-shadow:0px 0px 10px #00796B;
    }
    .bg-gcolor
    {
    background:#e3e3e3;
    }
</style>
<div class="row ">
           <div class="row bg-gcolor">
           <div class="col-sm-12 pt-3">
                     <div class="row">
                   {% if ncat %}
                   {% for x in ncat %}
                   <div class="col-sm-2 py-3">
                           <div class="card-body">
                               <a href="/user/viewnews?ab={{x.id}}" style="text-decoration:none;"><h5 class="card-title text-center text-darkcolor">{{x.category}}</h5></a>
                           </div>
                   </div>
                   {% endfor %}
                   {% endif %}
               </div>
           </div>
           </div>
          <div class="row bg-gcolor">
           <div class="col-sm-12 pt-3">
                     <div class="row">
                   {% if ncity %}
                   {% for x in ncity %}
                   <div class="col-sm-1 py-4">
                          <!-- <img src="/{{x.cpic}}" class="img-card-top pic"/>-->
                           <div class="card-body">
                               <a href="/user/citynews?ab={{x.id}}" style="text-decoration:none;"><h6 class="card-title text-center text-darkcolor">{{x.ncity}}</h6></a>
                           </div>
                   </div>
                   {% endfor %}
                   {% endif %}
               </div>
           </div>
           </div>
          <hr>
           <div class="fs-2 text-center">Latest<b class="text-darkcolor">News<i class="fa-solid fa-newspaper"></i></b></div>
           <div class="row">
           <div class="col-sm-1"></div>
           <div class="col-sm-10">
                <!--start card-->
                  <div class="row g-0">
                     {% if data %}
                      {% for x in data %}
                      <div class="col-sm-6 pt-3 ps-3">
                       <div class="card mb-3" style="max-width: 700px;">
                         <div class="row g-0 ">
                           <div class="col-md-4">
                            <img src="/{{x.npic}}" class="img-fluid rounded-start img-thumbnail pic" style="min-height:200px;" alt="...">
                           </div>
                         <div class="col-md-8">
                         <div class="card-body">
                            <h5 class="card-title">{{x.ntitle}}</h5>
                                 <span>{{x.nhead}}</span><br><br>
                                 <a href="/user/details?n={{x.id}}" class="btn btn-sm btn-mycolor bg-danger fw-bold">Veiw More
                                 <i class="fa-solid fa-eye"></i>
                                 </a><br><br>
                             <b> {{x.ncategory}}</b><br>
                             <i class="fa-solid fa-city"></i> {{x.ncity}}
                             <span class="text-muted float-end"><i class="fa-solid fa-calendar-days"></i> Date:
                             {{x.ndate}}</span>
                         </div>
                         </div>
                       </div>
                       </div>
                      </div>
                         {% endfor %}
                        {% endif %}
                <!--end card-->
             </div>
             </div>
           <div class="col-sm-1"></div>
</div>

{% endblock %}