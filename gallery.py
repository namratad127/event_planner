#!C:/Python27/python.exe
print "content-type:text/html\r\n\r\n"

print"""
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
		
<link rel="stylesheet" href="css/font-awesome.css"/>
<link rel="stylesheet" href="css/animate.css"/>
<link rel="stylesheet" href="css/hover.css" />
<link rel="stylesheet" href="css/bootstrap.min.css"/>
<script src="jquery-3.3.1.slim.min.js"></script>
<script src="popper.min.js"></script>
<script src="bootstrap.min.js"></script>
<script src="js/wow.js"></script> 
<script>
wow = new WOW(
{
boxClass:     'wow',      // default
animateClass: 'animated', // default
offset:       0,          // default
mobile:       true,       // default
live:         true        // default
}
)
wow.init();
</script>
<style>

.gallery-title
{
    font-size: 36px;
    color: black;
    text-align: center;
    font-weight: 500;
    margin-bottom: 70px;
}
.gallery-title:after {
    content: "";
    position: absolute;
    width: 7.5%;
    left: 46.5%;
    height: 45px;
    border-bottom: 1px solid #5e5e5e;
}
.filter-button
{
    font-size: 18px;
    border: 1px solid #42B32F;
    border-radius: 5px;
    text-align: center;
    color: #42B32F;
    margin-bottom: 30px;

}
.filter-button:hover
{
    font-size: 18px;
    border: 1px solid #42B32F;
    border-radius: 5px;
    text-align: center;
    color: #ffffff;
    background-color: #42B32F;

}
.btn-default:active .filter-button:active
{
    background-color: #42B32F;
    color: white;
}

.port-image
{
    width: 100%;
}

.gallery_product
{
    margin-bottom: 30px;
}

</style>
<script>
$(document).ready(function(){

    $(".filter-button").click(function(){
        var value = $(this).attr('data-filter');
        
        if(value == "all")
        {
            //$('.filter').removeClass('hidden');
            $('.filter').show('1000');
        }
        else
        {
//            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
//            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
            $(".filter").not('.'+value).hide('3000');
            $('.filter').filter('.'+value).show('3000');
            
        }
    });
    
    if ($(".filter-button").removeClass("active")) {
$(this).removeClass("active");
}
$(this).addClass("active");

});
</script>
</head>
<body>
<!--header line-->
<div class="container-fluid">
<div class="row A m-0 p-0" style="background-color:#cc0d72">
<div class="col-sm-6 text-light text-center h5 "><i class="fa fa-envelope "></i>divinemuhurat@gmail.com</div>
<div class="col-sm-5 text-light text-center h5"> <i class="fa fa-phone fa-1x "></i>+91-7985396269</div>
<div class="col-sm-1"></div>
</div>

<!-- Menu -->
<div class="row m-0 p-0">
<div class="col-sm-3">
<img src="wedding logo.jpg" class="img-fluid img1 ml-5 mt-1" style="height:100px;width:100px;"/>
</div>
<div class="col-sm-9 ">
<ul class="nav text-center mt-3 h4 nav-tabs nav-justified">
<li class="nav-item pr-2">
<a href="home.py" class="nav-link mnu">Home</a>
</li>
<li class="nav-item pr-2">
<a href="aboutus.py" class="nav-link mnu">About Us</a>
</li>
<li class="nav-item pr-2">
<a href="work.py" class="nav-link mnu">Our Work</a>
</li>
<li class="nav-item pr-2">
<a href="gallery.py" class="nav-link mnu">Gallery</a>
</li>
<li class="nav-item pr-2">
<a href="servies.py" class="nav-link mnu">Services</a>
</li>
<li class="nav-item pr-2">
<a href="Registration1.py" class="nav-link mnu">Register</a>
</li>
<li class="nav-item pr-2">
<a href="login.py" class="nav-link mnu">Login</a>
</li>
<li class="nav-item pr-2">
<a href="contact.py" class="nav-link mnu">Contact Us</a>
</li>
</ul>
</div>
</div>
</div>
 <div class="container">
        <div class="row">
        <div class="gallery col-lg-12 col-md-12 col-sm-12 col-xs-12">
            <h1 class="gallery-title">Gallery</h1>
        </div>
        </div>
        
        
        
        

           <div class="row">
            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow" ><img src="4b1294f65e7e0716e503f10352c2925a.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="4c81e4c70e2a5fe26d1fb46834f3b2b8.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="12a76b62d1c5974489e398628dcad6c7.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

           <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="c4b83ff327f55e9f59285481575bbbdf.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="5864a53a551157c8105246e6aa589ea3.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="60cbba88e17c925689f9ab59ed444d65.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="8e79b423ef8e094c5033c29ec1112ded.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>
            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="e8d13795-7e3b-0094-ad90-d3d8a7608c4b.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="07b31700042723e75b5778614bd13c47.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

           <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="beachweddinggoa.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="banner-image.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="e37fd4266743cdfeeaf8336a7235bbfa.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>
            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="a36939a05b6a96b62ae842d36280d10b.jpg" class="img-fluid" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="fcea969282deb7641f80b5bace89148a.jpg" class="img-fluide"height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="new-gallery4.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>
            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="cost-of-destination-wedding-packages-in-jaipur-and-pushkar-in-less-than-30-lakhs-destinationweddingseries-1.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="28dbb3d6930c2b11e9219b6f03314766.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="ea5e065e1e6aaffd87660b6dca3cdbe7.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>
            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="Haldi-Wedding-name-1200x768.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="Hyatt-Regency-Greenwich-wedding-HariRenu-0608-1.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>

            <div class="gallery_product col-lg-4 col-md-4 col-sm-4 col-xs-6 filter hdpe hvr-Grow Shadow">
                <div class="card shadow"><img src="nice-wedding-planner-events-elizabeth-r-events-limited-foremost-celebrity-events-management-mm.jpg" class="img-fluide" height="350px" width="100%"/></div>
            </div>
        </div>
    </div>
</section>


<!--footer-->
<div class="row bg-dark">
<div class="col-sm-6"><p class="text-white text-center h5">Design & Developed By:Namrata Dubey & Anchitya Singh</p></div>
<div class="col-sm-6"><p class="text-white text-center h5">Powered By:Digicoders technologies</p></div>
</div>
</div>



</body>
</html>"""