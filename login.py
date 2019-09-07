#!C:/Python27/python.exe
print "content-type:text/html\r\n\r\n"


print"""
<html>
<head>
	<title>Register</title>
		<meta charset="utf-8"/> 
        <meta name="viewport" content="width=device-width, initial-scale=1" />
		<link rel="stylesheet" href="css/font-awesome.css"/>
		<link rel="stylesheet" href="css/imagehover.css"/>
        <link rel="stylesheet" href="css/animate.css"/>
		<link rel="stylesheet" href="css/bootstrap.min.css" />
		<script src="js/jquery-3.3.1.slim.min.js"></script>
		<script src="js/popper.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
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
        	body {
background:url(ea5e065e1e6aaffd87660b6dca3cdbe7.jpg);
font-family:'PT Sans',Helvetica, Arial, sans-serif;
color:#fff;
   background-repeat: no-repeat;
   background-size:cover;
}

.page-container {
margin: 120px auto 0 auto;
}

h1 {
	font-size: 30px;
	font-weight: 700;
	text-shadow:0 1px 4px rgba(0,0,0,.2);
	text-align:center;
}

form {
position:relative;
width:305px;
margin:15px auto 0 auto;
text-align:center;

}

input {
width:270px;
height:42px;
margin-top:25px;
padding:0 15px;
background:#2d2d2d;
background:rgba(45,45,45,.15);
-moz-border-radius: 6px;
-webkit-border-radius:6px;
text-align:center;
border-radius:6px;
border:1px solid #3d3d3d;
border:1px solid rgba(255,255,255,.15);
-moz-box-shadow:0 2px 3px 0 rgba(0,0,0,.1) inset;
-webkit-box-shadow: 0 2px 3px 0 rgba(0,0,0,.1) inset;
box-shadow: 0 2px 3px 0 rgba(0,0,0,.1) inset;
font-family: 'PT Sans', Helvetica, Arial, sans-serif;
font-size:16px;
color:#fff;
text-shadow:0 1px 2px rgba(0,0,0,.1);
-o-transition: all .2s;
-moz-transition: all .2s;
-webkit-transition: all .2s;
-ms-transition: all .2s;
}

input:-moz-placeholder { color: #fff; }
input:-ms-input-placeholder { color: #fff; }
input::-webkit-input-placeholder { color: #fff; }

input:focus {
outline:none;
-moz-box-shadow:
        0 2px 3px 0 rgba(0,0,0,.1) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
-webkit-box-shadow:
        0 2px 3px 0 rgba(0,0,0,.1) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
box-shadow:
        0 2px 3px 0 rgba(0,0,0,.1) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
}

button {
cursor:pointer;
width:300px;
height:44px;
margin-top:25px;
padding:0;
background:#ef4300;
-moz-border-radius: 6px;
-webkit-border-radius: 6px;
border-radius: 6px;
border:1px solid #ff730e;
-moz-box-shadow:
        0 15px 30px 0 rgba(255,255,255,.25) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
-webkit-box-shadow:
        0 15px 30px 0 rgba(255,255,255,.25) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
box-shadow:
        0 15px 30px 0 rgba(255,255,255,.25) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
font-family:'PT Sans', Helvetica, Arial, sans-serif;
font-size:14px;
font-weight:700;
color:#fff;
text-shadow:0 1px 2px rgba(0,0,0,.1);
-o-transition: all .2s;
    -moz-transition: all .2s;
    -webkit-transition: all .2s;
    -ms-transition: all .2s;
}

button:hover {
    -moz-box-shadow:
        0 15px 30px 0 rgba(255,255,255,.15) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
    -webkit-box-shadow:
        0 15px 30px 0 rgba(255,255,255,.15) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
    box-shadow:
        0 15px 30px 0 rgba(255,255,255,.15) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
}

button:active {
    -moz-box-shadow:
        0 15px 30px 0 rgba(255,255,255,.15) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
    -webkit-box-shadow:
        0 15px 30px 0 rgba(255,255,255,.15) inset,
        0 2px 7px 0 rgba(0,0,0,.2);
    box-shadow:        
        0 5px 8px 0 rgba(0,0,0,.1) inset,
        0 1px 4px 0 rgba(0,0,0,.1);

    border: 0px solid #ef4300;
}



.navbar {
    overflow: hidden;
    background-color: #333;
    font-family: Arial;
}

.navbar a {float: left;font-size: 16px;color: white;text-align: center;padding: 14px 16px;text-decoration: none;}

.dropdown {float: left;overflow: hidden;}

.dropdown .dropbtn {font-size: 16px;border: none;outline: none;color: white;padding: 14px 16px;background-color: inherit;}

.navbar a:hover, .dropdown:hover .dropbtn {background-color: red}

.dropdown-content {display: none;position: absolute;background-color: #f9f9f9;width: 160px;box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);z-index: 1;}

.dropdown-content a {float: none;color: black;padding: 12px 16px;text-decoration: none;display: block;text-align: left;}

.dropdown-content a:hover {background-color: #ddd;}

.dropdown:hover .dropdown-content {display: block;}
















        </style>
</head>
	<body>
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

<!--login-->
<div class="page-container">
            
			
            <form action="log.py" method="POST">
			<h1>LOGIN</h1>
                <input type="text" name="txt1" class="Name" placeholder="Name">
             <br/><br/>
				<input type="password" name="txt2" class="Address" placeholder="password">
				<br/><br/>
                <button  type="submit" value="Add" name="submit"><a href="profile.py">Login</a></button>
				
            </form>
			<div class="d-flex justify-content-center">
					<a href="#">Change password</a>
				</div>
        </div>
	    

<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<!--footer-->
<div class="row bg-dark">
<div class="col-sm-6"><p class="text-white text-center h5">Design & Developed By:Namrata Dubey & Anchitya Singh</p></div>
<div class="col-sm-6"><p class="text-white text-center h5">Powered By:Digicoders technologies</p></div>
</div>
</div>								
	</body>	
</html>"""