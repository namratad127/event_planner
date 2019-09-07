#!C:/Python27/python.exe
print "content-type:text/html\r\n\r\n"

print"""
<html>
<head>
         <meta charset="utf-8"/>
		 <meta name="viewport" content="width=device-width, initial-scale=1" />
	 
	     <link rel="stylesheet" href="css/font-awesome.css"/>
<link rel="stylesheet" href="css/animate.css"/>
<link rel="stylesheet" href="css/hover.css" />
<link rel="stylesheet" href="css/bootstrap.min.css" />
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
		 
.jumbotron {
background: #cc0d72;
color: #FFF;
border-radius: 0px;
}
.jumbotron-sm { padding-top: 24px;
padding-bottom: 24px; }
.jumbotron small {
color: #FFF;
}
.h1 small {
font-size: 24px;
}

		 </style>
</head>
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





<!--body--->
<div class="jumbotron jumbotron-sm">
    <div class="container">
        <div class="row">
            <div class="col-sm-12 col-lg-12">
                <h1 class="h1">
                    Contact us <small>Feel free to contact us</small></h1>
            </div>
        </div>
    </div>
</div>
<div class="container">
    <div class="row">
        <div class="col-md-8">
            <div class="well well-sm">
                <form id="contact" action="contactcode.py" method="post">
                <div class="row">
                    <div class="col-md-6">
                        <div class="form-group">
                            <label for="name">
                                Name</label>
                            <input type="text" class="form-control" id="name" placeholder="Enter name" tabindex="1" name="name" required="required"/>
                        </div>
                        <div class="form-group">
                            <label for="email">
                                Email Address</label>
                            <div class="input-group">
                                <span class="input-group-addon"><span class="glyphicon glyphicon-envelope"></span>
                                </span>
								<input placeholder="Email" class="form-control" type="email" id="email" tabindex="2"  name="email" required>
                                </div>
                        </div>
                        <div class="form-group">
                            <label for="subject">
                                Subject</label>
                            <input id="subject" type="text" name="subject" placeholder="Subject" tabindex="4" class="form-control" required="required">
                                
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="form-group">
                            <label for="name">
                                Message</label>
                            <textarea name="message" id="message" type="text" class="form-control" tabindex="5" rows="9" cols="25" required="required"
                                placeholder="Message"></textarea>
                        </div>
                    </div>
                    <div class="col-md-12">
                        <button type="submit" class="btn  pull-right"  style="background-color:#cc0d72" id="btnContactUs">
                            Send Message</button>
                    </div>
                </div>
                </form>
            </div>
        </div>
        
        </div>
    </div>
</div>



	 
	        
</div><br/><br/>
			
	 <!--footer-->
<div class="row bg-dark">
<div class="col-sm-6"><p class="text-white text-center h5">Design & Developed By:Namrata Dubey & Anchitya Singh</p></div>
<div class="col-sm-6"><p class="text-white text-center h5">Powered By:Digicoders technologies</p></div>
</div>
</div>			
   </div>
</body>
</html>"""