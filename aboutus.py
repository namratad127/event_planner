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

</head>
<style>
{
 background:#000000 !important;
}

/*

*/

h3 {
  color: blue;
}
.text{
	color: white;
	text-align: center;
}


.folded-corner:hover .text{
	visibility: visible;
	color: white;
}
.Services-tab{
	margin-top:20px;
	

}

/*
  nav link items
*/
.folded-corner{
  padding: 25px 25px;
  position: relative;
  font-size: 90%;
  text-decoration: none;
  color: #999; 
  background: transparent;
  transition: all ease .5s;
  border: 1px solid #cc0d72;
}
.folded-corner:hover{
	background-color: black;
}

/*
  paper fold corner
*/

.folded-corner:before {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  border-style: solid;
  border-width: 0 0px 0px 0;
  border-color: #ddd #000;
  transition: all ease .3s;
}

/*
  on li hover make paper fold larger
*/
.folded-corner:hover:before {
	background-color: #D00003;
  border-width: 0 50px 50px 0;
  border-color: #eee #000;
  
}

.service_tab_1{
	background-color: #000;
}
.service_tab_1:hover .fa-icon-image{
    color: #000;
    transform: rotate(360deg) scale(1.5);
}


.fa-icon-image{
	color: rgba(31,181,172,.9);
	display: inline-block;
    font-style: normal;
    font-variant: normal;
    font-weight: normal;
    line-height: 1;
    font-size-adjust: none;
    font-stretch: normal;
    -moz-font-feature-settings: normal;
    -moz-font-language-override: normal;
    text-rendering: auto;
    transition: all .65s linear 0s;
    text-align: center;
    transition: all 1s cubic-bezier(.99,.82,.11,1.41);
}


</style>
<body>

<div class="container-fluid">
<div class="row">
<!--header line-->
<div class="container-fluid">
<div class="row A m-0 p-0" style="background-color:#cc0d72">
<div class="col-sm-6 text-light text-center h5 "><i class="fa fa-envelope "></i>divinemuhurat@gmail.com</div>
<div class="col-sm-5 text-light text-center h5"> <i class="fa fa-phone fa-1x "></i>+91-7985396269</div>
<div class="col-sm-1"></div>
</div>
<!-- Menu -->
<div class="row m-0 p-0">
<div class="col-sm-4">
<img src="wedding logo.jpg" class="img-fluid img1 ml-5 mt-1" style="height:100px;width:100px;"/>
</div>
<div class="col-sm-8 ">
<ul class="nav text-center mt-2 h5 nav-tabs nav-justified">
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
</div> 

<!-- slide image -->
<div class="container-fluid">
<div class="row">
<div class="col-sm-12 p-0 m-0" style="background-image:url('home-top-slider-item-1.jpg');background-size:100%;100%; height:300px;">

<h1 style="margin-top:120px;margin-left:100px;">ABOUT US</h1>
</div>
</div>

</div>

<br/>
<br/>





<section class="content">
            <div class="container">
                <div class="home-event">
                    <div class="heading">
                        <div class="icon"><em class="icon icon-heading-icon"></em></div>
                        <div class="text">
                            <h1 class="text-center">Welcome to Divine Muhurat</h1>
                        </div>
                        <div class="stickLine"></div>
                    </div>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="text-center h6">
                            	<p>Are you ready to plan your wedding? Divine Muhurat is trusted wedding planner. We'll help
								you to plan the wedding you have always dreamt of... and of course your guest will have a great 
								time too!</p>
                                <p>We are a professional wedding planner and private honeymoon tour operator based in india.
								Our team is excited to help couples from all over the world who plans to celebrate their wedding
								& honeymoon. For more detail and personalized inquiry please contact us at
								<strong><a href="mailto:wandergroup@icloud.com"> divinemuhurat@gmail.com</a></strong> or fill 
								of our contact us form.</p>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
		<br/> <br/>
		
		<div class="container-fluid">
	<div class="row">
	
		<div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 Services-tab  item">
			<div class="folded-corner service_tab_1">
				<div class="text">
					<img src="fireplace.png" height="100px" width="100px"/>
						<p class="item-title">
								<h3> Wedding Venues</h3>
							</p><!-- /.item-title -->
					<p>
						With regards to wedding arranging, picking the ideal wedding setting is by a wide margin a standout amongst the most imperative things you have to choose ahead of time.  
					
					</p>
				</div>
			</div>
	    </div>
		<div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 Services-tab item">
			<div class="folded-corner service_tab_1">
				<div class="text">
					<img src="wedding-greeting-card.png"  height="100px" width="100px"/>
						<p class="item-title">
							<h3> Wedding Cards</h3>
						</p><!-- /.item-title -->
						<p>
							Everything identified with wedding is experiencing developments thus do welcome card. Wedding Invitation card is a standout amongst the most vital piece of wedding.
					    </p>
				</div>
			</div>
		</div>
		<div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 Services-tab item">
			<div class="folded-corner service_tab_1">
				<div class="text">
					<img src="wedding-arch.png" height="100px" width="100px"/>
						<p class="item-title">
							<h3>  Decorators</h3>
						</p><!-- /.item-title -->
					<p>
						Every Small to Big Decoration part of your Wedding and Occasion Function, We resemble one-quit Wedding and Event organizers who oversee everything in your Low and High Budget.
				    </p>
				</div>
			</div>
		</div>
		<div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 Services-tab item">
			<div class="folded-corner service_tab_1">
				<div class="text">
					<img src="musical-note.png" height="100px" width="100px"/>
						<p class="item-title">
							<h3> Ceremonial Music</h3>
						</p><!-- /.item-title -->
					<p>
						With regards to leave an enduring impression of your huge day, the wedding excitement you pick has a significant effect. The sort of stimulation you pick can represent the moment of truth your wedding occasion.
						
					</p>
				</div>
			</div>
		</div>
		
		</div>
		</div>
		
		
		<div class="container-fluid">
	<div class="row">
    
		<div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 Services-tab item">
			<div class="folded-corner service_tab_1">
			<div class="text">
				<img src="bride.png" height="100px" width="100px"/>
					<p class="item-title">
						<h3>Bridal Designers</h3>
					</p><!-- /.item-title -->
					<p>
							Wedding day will be day of the prep and lady of the hour. Everybody's eyes are stuck at them thus its essential for them two to look wonderful and best extraordinarily lady they need their best to come on this day.
					</p>
				</div>
			</div>
		</div>
		<div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 Services-tab item">
			<div class="folded-corner service_tab_1">
				<div class="text">
					<img src="photo-camera.png" height="100px" width="100px"/>
						<p class="item-title">
							<h3>Photography</h3>
						</p><!-- /.item-title -->
					<p>
						  There are a lot of minutes that you need to catch. Regardless of whether its mehndi work, ring service, mixed drink party or some other pre-wedding event everybody needs to solidify these unique minutes.
					</p>
				</div>
			</div>
		</div>
		<div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 Services-tab item">
				<div class="folded-corner service_tab_1">
					<div class="text">
						<img src="video-camera.png" height="100px" width="100px"/>
							<p class="item-title">
								<h3> Videography</h3>
							</p><!-- /.item-title -->
						<p>
							Wedding videography isn't only a simple to use work proficient videographers catch your extraordinary story and show it in the manner in which you need it to be seen.
					    </p>
				</div>
			</div>
		</div>
		<div class="col-lg-3 col-md-3 col-sm-12 col-xs-12 Services-tab item">
			<div class="folded-corner service_tab_1">
				<div class="text">
					<img src="wedding-planner.png" height="100px" width="100px"/>
						<p class="item-title">
							<h3> Wedding Planners</h3>
						</p><!-- /.item-title -->
					<p>
						Best Wedding Planner in Delhi! Wedding is the most important day in the life of the groom and the bride to be. It is the magical day that needs to be planned in the best way possible.
					</p>
				</div>
			</div>
		</div>
	   
	</div>
</div>



		<br/> <br/>
		
		
		
		
		<div class="container">
                <div class="row">
                    <div class="col-sm-12">
                        <div class="heading">
                        <div class="icon"><em class="icon icon-heading-icon"></em></div>
                        
                            <h1>WHAT WE CAN DO</h1>
							<br/>
                            <div class="stickLine"></div>
                        </div>
                    
                        <h3 style="color: #000;">Start Planning</h3>
                        <p class="h6">We'll help you to find the perfect venue, and connected with all the local vendors that you will need to make your wedding perfect!</p>
<h3 style="color: #000;">Keep you organized</h3>
                        <p class="h6">Our wedding coordinator will keep you on track, keep you organized through professional management so that not a details missed. Of course, we'll always inform you with new and fresh ideas for your wedding!</p>
<h3 style="color: #000;">You have the question, we have the answer</h3>
                        <p class="h6">Our friendly wedding expertise will answer all the question you have regarding your wedding. Be it the question "do you really need someone to hold your dress while you pee?"</p>
                    </div>
                </div>
            </div>
        </section>
<br/><br/>

  




<!--footer-->
<div class="row bg-dark">
<div class="col-sm-6"><p class="text-white text-center h5">Design & Developed By:Namrata Dubey & Anchitya Singh</p></div>
<div class="col-sm-6"><p class="text-white text-center h5">Powered By:Digicoders technologies</p></div>
</div>
</div>



</body>
</html>"""


