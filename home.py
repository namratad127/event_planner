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
<link rel="stylesheet" href="css/bootstrap.min.css" />
<script src="jquery-3.3.1.slim.min.js"></script>
<script src="popper.min.js"></script>
<script src="bootstrap.min.js"></script>
<script src="js/wow.js"></script> 
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"/>
<style>
.A
{
background-color:#b7005b;
}
.img1
{
height:60px;
}
.mnu
{
color:#941b0a;
}
.mnu:hover
{
color:black;
}
.img2
{
height:500px;
}
.svr
{
	background-color:black;
	color:white;
	border-radius:25px;
}
.svr:hover
{
	background-color:yellow;
	color:blue;
}




* {
    margin: 0; 
	padding: 0;
}
body {
	background: white; 
	font-family: arial, verdana, tahoma;
}

/*Time to apply widths for accordian to work
Width of image = 640px
total images = 5
so width of hovered image = 640px
width of un-hovered image = 40px - you can set this to anything
so total container width = 640 + 40*4 = 800px;
default width = 800/5 = 160px;
*/

.accordian {
	width: 805px; height: 320px;
	overflow: hidden;
	
	/*Time for some styling*/
	margin: 100px auto;
	box-shadow: 0 0 10px 1px rgba(0, 0, 0, 0.35);
	-webkit-box-shadow: 0 0 10px 1px rgba(0, 0, 0, 0.35);
	-moz-box-shadow: 0 0 10px 1px rgba(0, 0, 0, 0.35);
}

/*A small hack to prevent flickering on some browsers*/
.accordian ul {
	width: 1200px;
	/*This will give ample space to the last item to move
	instead of falling down/flickering during hovers.*/
}

.accordian li {
	position: relative;
	display: block;
	width: 160px;
	float: left;
	
	border-left: 1px solid #888;
	
	box-shadow: 0 0 25px 10px rgba(0, 0, 0, 0.5);
	-webkit-box-shadow: 0 0 25px 10px rgba(0, 0, 0, 0.5);
	-moz-box-shadow: 0 0 25px 10px rgba(0, 0, 0, 0.5);
	
	/*Transitions to give animation effect*/
	transition: all 0.5s;
	-webkit-transition: all 0.5s;
	-moz-transition: all 0.5s;
	/*If you hover on the images now you should be able to 
	see the basic accordian*/
}

/*Reduce with of un-hovered elements*/
.accordian ul:hover li {width: 40px;}
/*Lets apply hover effects now*/
/*The LI hover style should override the UL hover style*/
.accordian ul li:hover {width: 640px;}


.accordian li img {
	display: block;
}

/*Image title styles*/
.image_title {
	background: white;
	position: absolute;
	left: 0; bottom: 0;	
width: 640px;	

}
.image_title a {
	display: block;
	color: #fff;
	text-decoration: none;
	padding: 40px;
	font-size: 20px;
}
------

.carousel-control.left,.carousel-control.right  {background:none;width:25px;}
.carousel-control.left {left:-25px;}
.carousel-control.right {right:-25px;}
.broun-block {
    background: url("http://myinstantcms.ru/images/bg-broun1.jpg") repeat scroll center top rgba(0, 0, 0, 0);
    padding-bottom: 34px;
}
.block-text {
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 3px 0 #2c2222;
    color: #626262;
    font-size: 14px;
    margin-top: 27px;
    padding: 15px 18px;
}
.block-text a {
 color: #7d4702;
    font-size: 25px;
    font-weight: bold;
    line-height: 21px;
    text-decoration: none;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
}
.mark {
    padding: 12px 0;background:none;
}
.block-text p {
    color: #585858;
    font-family: Georgia;
    font-style: italic;
    line-height: 20px;
}
.sprite {
	background-image: url('');
}
.sprite-i-triangle {
    background-position: 0 -1298px;
    height: 44px;
    width: 50px;
}
.block-text ins {
    bottom: -44px;
    left: 50%;
    margin-left: -60px;
}


.block {
    display: block;
}
.zmin {
    z-index: 1;
}
.ab {
    position: absolute;
}

.person-text {
    padding: 10px 0 0;
    text-align: center;
    z-index: 2;
}
.person-text a {
    color: #ffcc00;
    display: block;
    font-size: 14px;
    margin-top: 3px;
    text-decoration: underline;
}
.person-text i {
    color: #fff;
    font-family: Georgia;
    font-size: 13px;
}
.rel {
    position: relative;
}



</style>




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
</head>
<body>
<!--header line-->
<div class="container-fluid">
<div class="row A m-0 p-0">
<div class="col-sm-6 text-light text-center h5 "><i class="fa fa-envelope "></i>divinemuhurat@gmail.com</div>
<div class="col-sm-5 text-light text-center h5"> <i class="fa fa-phone fa-1x "></i>+91-7985396269</div>
<div class="col-sm-1"></div>
</div>
<!-- Menu -->
<div class="row m-0 p-0">
<div class="col-sm-4">
<img src="wedding logo.jpg" class="img-fluide img1 ml-5 mt-1 "/>
</div>
<div class="col-sm-8 ">
<ul class="nav text-center mt-2 h5 nav-tabs nav-justified">
<li class="nav-item pr-2">
<a href=".py" class="nav-link mnu">Home</a>
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
<!-- Slide imeges-->
<div class="container-fluid">
<div class="row">
<div class="col-sm-12">
<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
<div class="carousel-inner">
<div class="carousel-item active">
<img src="wedding-photography-bhopal-india.jpg" class="d-block w-100 img2" data-wow-iteration="infinite" alt="..."> 

</div>
<div class="carousel-item">
<img src="slider06.jpg" class="d-block w-100 img2" alt="..." data-wow-iteration="infinite">
</div>
<div class="carousel-item">
<img src="bg_deco1.jpg" class="d-block w-100 img2" alt="..." data-wow-iteration="infinite">
</div>
</div>
<a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
<span class="carousel-control-prev-icon" aria-hidden="true"></span>
<span class="sr-only">Previous</span>
</a>
<a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
<span class="carousel-control-next-icon" aria-hidden="true"></span>
<span class="sr-only">Next</span>
</a>
</div>
</div>
</div>
<div class="row">
<div class="col-sm-12 bg-dark">
<div class="container">
<div class="row">
<div class="col-sm-12 bg-light"><marquee class="h2">Nominated among Top 12 Best Wedding Planners Worldwide and Top 3 in Europe by ELLE International Bridal Awards 2017.
</marquee></div>
</div>
</div>
</div>
</div>
</div>

<div class="container">
<div class="sub-title2 text">
<h2 class="text-center mt-3 mb-2">International Wedding Planner</h2><hr/>
<div class="icon"><em class="icon icon-heading-icon"></em></div>
</div>
<div class="row mb-3">
<div class="col-lg-12">
<div class="hotel-info tab-content" id="venues">
<div class="event-info">
<div class="service-details">
<div class="row mt-2">
<div class="col-sm-6">
<div class="img">
<img src="indian-wedding-decor-ideas-corners_home-elements-and-style.jpg" width="100%" alt="International Wedding Planner" class="img-responsive" style="height:630px;"/>
</div>
</div>
<div class="col-sm-6">
<h2>The Best Wedding Planners in India</h2><hr/>
<p class="text-justify"><strong>Divine Muhurat</strong> is a well-known wedding planning organization. The organization has been started by professionals with a rich experience in planning and managing a vast number of weddings programs. The company is an International Wedding planner that can ensure your wedding day is truly a memorable one that you would cherish for the rest of your life. We guarantee that you will never stop talking about how well your dream wedding was planned and organized.</p>
<h3 class="h1-heading">Our Credentials</h3><hr/>		
<p class="text-justify margin-0"><strong>Divine Muhurat</strong> has expertise in the field of wedding planning. Right from planning the dates and arrangements till the successful hosting of all rituals and the reception, our team strives to provide the best service. We provide a one-stop solution for all your needs.
The success we have had in planning and conducting weddings in India and abroad are a testament to our expertise. Our credentials explain why we are among the <strong>Best Wedding Planners in India:</strong></p>
<ul class="customList">
<li> 10+ years of experience in the wedding planning industry</li>
<li>More than 1100 events successfully conducted</li>
<li>On an average 150 events conducted every year, achieving total customer satisfaction</li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

<br/>
<!-- who we are-->
<div class="jumbotron jumbotron-fluid">
  <div class="container-fluid" style="height:200px;">
  <p class="h2 text-center">Services</p>
  <p class="text-justify">We have the complete solution to present you a memorable  wedding ceremony - for our services. 
  Finalizing Wedding venues
  . We are a well-known <strong>Destination Wedding Planning in India</strong> conducting weddings exotic
  foreign locales like Antalya and Bali. As a reputed Wedding Planner in Jaipur, Wedding
  Planner in Delhi, Wedding Planner in Gujarat and other cities we can also help you choose perfect Indian destinations. 
  We also arrange photography and videography to capture the memories of your fairytale wedding.
  From the planning phase until completion of all wedding ceremonies, Wedding planner offers the best of services customized for your 
  specific requirements. Do contact us for your wedding needs, we guarantee that we will create an 
  experience that will remain for a lifetime.</p>
  
</div>
</div>
  <br/>
 <div class="container">
	<div class="row">
  <div class="col-sm-3">
		   <div class="card-body svr">
		  <img src="fireplace.png" class="text-center" height="100px" width="100px"/><br/>
          <span class="text h5">Wedding Venues</span>
			</div>
</div>

<div class="col-sm-3">
		  <div class="card-body svr">
		  <img src="wedding-greeting-card.png" class="text-center" height="100px" width="100px"/><br/>
          <span class="text h5">Wedding Cards</span>
		</div>
</div>

<div class="col-sm-3">
		  <div class="card-body svr">
		   <img src="wedding-arch.png" height="100px" class="text-center" width="100px"/><br/>
          <span class="text h5"><b>Wedding Decorators</b></span>
		</div>
</div>

<div class="col-sm-3">
		  <div class="card-body svr">
		   <img src="musical-note.png" class="text-center" height="100px" width="100px"/><br/>
          <span class="text h5">Ceremonial Music</span>
		  </div>
		
		
		
		
</div>
</div>
</div>


 <div class="container-fluid mt-2 mb-3">
	<div class="row">
  <div class="col-sm-3">
		  <div class="card-body svr">
		  <img src="bride.png" class="text-center" height="100px" width="100px"/><br/>
          <span class="text h5">Bridal Designers</span>
		</div>
</div>

<div class="col-sm-3">
		   <div class="card-body svr">
		  <img src="photo-camera.png"  class="text-center" height="100px" width="100px"/>
          <span class="text h5">Photography</span>
		</div>
</div>

<div class="col-sm-3">
		   <div class="card-body svr">
		  <img src="video-camera.png" class="text-center" height="100px" width="100px"/>
          <span class="text h5">Videography</span>
			</div>
</div>

<div class="col-sm-3">
		  <div class="card-body svr">
		  <img src="wedding-planner.png" style="text-align:center" height="100px" width="100px"/><br/>
          <span class="text h5">Wedding Planners</span>
		</div>
			
</div>
</div>
</div>
<br/>

<div class="container-fluid">
<div class="row">

<div class="col-sm-6 mb-3">
<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="beach-weddings-goa.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="wedding_decoration.jpg" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="weddings-in-udaipur.jpg" class="d-block w-100" alt="...">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>
<div class="col-sm-6">
<h3>Who We Are</h3>
<p style="text-align:justify;">Divine Muhurat Planners is a team of qualified and experienced Wedding Industry experts, 
who go the extra mile in providing you with a unique and personalized, tailor-made event. Our team's more than proud to
 bring you the very best in wedding planning and management. As we believe in upholding the traditions, breaking the monotony,
 and transporting weddings to a whole new level of revelry! Rest assured, we provide you with exclusive pre to post wedding 
 facilities that you'll find nowhere else, and all this with our repute, signature styles and that endearing touch.</p>

</div>
</div>

</div>
<br/>


<!---------Our Works---------->

  <div class="container-fluid">
<div class="row">
<div class="col-sm-12 h1 text-center mb-3">
Our Works
</div>
</div>


<div class="col-sm-12 text-center mb-3">
<p class="h4">An Event gives birth to other Events in life. Is not it? Enjoyed at some event will leave you with good memories.</p>

</div>


<div class="row mb-3">
<div class="col-sm-4"><img src ="cost-of-destination-wedding-packages-in-jaipur-and-pushkar-in-less-than-30-lakhs-destinationweddingseries-1.jpg" class="img-fluide" height="35%" width="100%"/></div>
<div class="col-sm-4"><img src ="beach-weddings-goa.jpg" class="img-fluide" height="35%" width="100%"/></div>
<div class="col-sm-4"><img src ="c4b83ff327f55e9f59285481575bbbdf.jpg" class="img-fluide" height="35%" width="100%"/></div>

</div>

<div class="row mb-3">
<div class="col-sm-4"><img src ="nice-wedding-planner-events-elizabeth-r-events-limited-foremost-celebrity-events-management-mm.jpg" class="img-fluide" height="35%" width="100%"/></div>
<div class="col-sm-4"><img src ="Mehendi-2.jpg" class="img-fluide" height="35%" width="100%"/></div>
<div class="col-sm-4"><img src="1390431bd18bc45b4c4bb198e8b44758.jpg" class="img-fluide" height="35%" width="100%"/></div>
</div>

</div>

<br/>



<!---------portfolio---------->
<div class="container-fluid">
<div class="row">
<div class="col-sm-12 h1 text-center mb-3">
Portfolio
</div>
</div>
</div>

<div class="accordian">
    <ul>
		<li>
			<div class="image_title">
				<a href="#">Haldi</a>
			</div> 
			<a href="#">
				<img src="b31a7baa87a3b96867f6552b76f0a033.jpg"/>
			</a>
		</li>
		<li>
			<div class="image_title">
				<a href="#">Mehendi</a>
			</div>
			<a href="#">
				<img src="Mehendi-2.jpg"/>
			</a>
		</li>
		<li>
			<div class="image_title">
				<a href="#">Sangeet</a>
			</div>
			<a href="#">
				<img src="banner-image.jpg"/>
			</a>
		</li>
		<li>
			<div class="image_title">
				<a href="#">Wedding</a>
			</div>
			<a href="#">
				<img src="beach-weddings-goa.jpg"/>
			</a>
		</li>
		<li>
			<div class="image_title">
				<a href="#">Vidaai</a>
			</div>
			<a href="#">
				<img src="1390431bd18bc45b4c4bb198e8b44758.jpg"/>
			</a>
		</li>
	</ul>
</div>


 <!--footer-->
<div class="row bg-dark">
<div class="col-sm-6"><p class="text-white text-center h5">Design & Developed By:Namrata Dubey & Anchitya Singh</p></div>
<div class="col-sm-6"><p class="text-white text-center h5">Powered By:Digicoders technologies</p></div>
</div>
</div>			
   </div>


</body>
</html>"""