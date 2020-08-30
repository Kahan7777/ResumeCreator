import os
import pdfkit
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from resg import app, db, bcrypt
from resg.forms import RF, LF, UA
from resg.models import User
from flask_login import login_user, current_user, logout_user, login_required

def r_1_download():
    name = current_user.name + ".html"
    sname = r"resg\static\ " + current_user.name +".pdf"
    f = open(name, "w")
    f.write(f"""
    
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Untitled Document</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

            <!-- jQuery library -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            
            <!-- Popper JS -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            
            <!-- Latest compiled JavaScript -->
            <link href="https://fonts.googleapis.com/css?family=Calistoga" rel="stylesheet">
            <link href='https://fonts.googleapis.com/css?family=Forum' rel='stylesheet'>
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
        </head>
        <body class="img-fluid">
        	  <div class="container">
	  <div class="row" style="background-color:#5849c4">
				  <div class="col-md-5 offset-lg-1">
				  <p class="lead text-light" style="font-size: 200%"><b>{ current_user.name }</b></p>
				  </div>
				  <div class="col-md-6 " style="text-align: center">
					  <h3 class=" lead text-white" style="font-size: 150%; padding:12px">{ current_user.prof }</h3>
				  </div>
			  </div>
			  <hr>
    			<div class="row">
			    <div class="col-lg-6">
					<div class="container-fluid">
					<h3 style="padding-left:20px;border-bottom:2px solid #AAAAAA">Project-1</h3>
					
					<p style="margin-left: 40px">{ current_user.project1 }
					</p>
					<hr>
					<hr>
					</div>
					<div class="container-fluid">
					<h3 style="padding-left:20px;border-bottom:2px solid #AAAAAA">Project-2</h3>
					
					<p style="margin-left: 40px">{ current_user.project2 }
					</p>
					<hr>
					<hr>
					</div>
					<div class="container-fluid">
					<h3 style="padding-left:20px;border-bottom:2px solid #AAAAAA">Project-3</h3>
					
					<p style="margin-left: 40px">{ current_user.project3 }
					</p>
					<hr>
					<hr>
					</div>
					<div class="container-fluid">
					<h3 style="padding-left:20px;border-bottom:2px solid #AAAAAA">Project-4</h3>
					
					<p style="margin-left: 40px">{ current_user.project4 }
					</p>
					<hr>
					<hr>
					</div>
					<div class="container-fluid">
					<h3 style="padding-left:20px;border-bottom:2px solid #AAAAAA">Information</h3>
					
					<h5>{ current_user.age }</h5>
					<h5>{ current_user.residence }</h5>
					<hr>
					<hr>
					</div>
				</div>
			    <div class="offset-lg-1 col-lg-4">
					<h3 style="font-size:50">Skills</h3>
					<ul>
						<li>{ current_user.skills1 }</li>
						<li>{ current_user.skills2 }</li>
						<li>{ current_user.skills3 }</li>
						<li>{ current_user.skills4 }</li>
				
					</ul>
					<hr>
					<hr>
					<h3 style="font-size:50">Achievments</h3>
					<ul>
						<li>{ current_user.ach1 }</li>
						<li>{ current_user.ach2 }</li>
						<li>{ current_user.ach3 }</li>
						<li>{ current_user.ach4 }</li>
					
					</ul>
					<hr>
					<hr>
					<h3 style="font-size:50">Education</h3>
					<ul>
						<li>{ current_user.schoolname }</li>
						<li>{ current_user.degree }</li>
						<li>{ current_user.study }</li>
						<li>{ current_user.date }</li>
					
					</ul>
					<hr>
					<hr>
					<h3 style="font-size:50">Experience</h3>
					<ul>
						<li>{ current_user.employer }</li>
						<li>{ current_user.jobtitle }</li>
					
				  </ul>
					<hr>
					<hr>
				</div>
		
					
		
    </div>
	
			  
		  </div>
		  <div class="container">
			  <h3 class="text-dark">Timeline</h3>
			  <br>
			 <hr style="border:3px solid #444DF8" >
		  </div>
        </body>
        <!-- body code goes here -->
    </html>""")
    f.close()
     
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    options = {'enable-local-file-access': None}
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(name, sname, configuration=config, options=options)

def r_2_download():
    name = current_user.name + ".html"
    sname = r"resg\static\ " + current_user.name +".pdf"
    f = open(name, "w")
    f.write(f"""
    
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Untitled Document</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

            <!-- jQuery library -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            
            <!-- Popper JS -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            
            <!-- Latest compiled JavaScript -->
            <link href="https://fonts.googleapis.com/css?family=Calistoga" rel="stylesheet">
            <link href='https://fonts.googleapis.com/css?family=Forum' rel='stylesheet'>
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
        </head>
        <body class="img-fluid">
        	  <div class="container">
	    <div class="row">
	      <div class="lead col-lg-5" style="background-color:#BBBBBB; text-align:left; padding-left:50px; font-size: 230%; ">{ current_user.name }</div>
	      <div class="col-lg-7 text-center" style="background-color:#BBBBBB; font-size:200%; border-left:2px solid black;">{ current_user.prof }</div>
        </div>
		<div class="row">
		  <div class="col-lg-2">
		    <div class="row">
		      <div class="col-lg-1" style="border-left:10px ridge #2C84FD; m"><br><br><br><br><br><br><br><br><br><br><br><br><br></div>
		      <div class="col-lg-4"><i class="fas fa-arrow-right" style="font-size: 24; color:#1CA0FA;"></i></div>
	        </div>
		  </div>
		  <div class="col-lg-3">
			  <h5>Achivements</h5>
			  <div style="padding-left:20px;">
				  <div class="card bg-light mb-1">
                	<p>{ current_user.ach1 } </p>
                 </div>
				  
				 <div class="card bg-light mb-1">
                	<p>{ current_user.ach1 } </p>
                 </div>
				  
				  <div class="card bg-light mb-1">
                	<p>{ current_user.ach1 } </p>
                 </div>
				 
				  <div class="card bg-light mb-1">
                	<p>{ current_user.ach1 }</p>
                 </div>
				  
		    </div>
		  </div>
		  <div class="col-lg-3">
		    <div class="row">
		      <div class="col-lg-2"><i class="fas fa-arrow-right" style="font-size:24px;color:#1CA0FA;"></i></div>
		      <div class="col-lg-10">
			    <h5>Skills</h5>
				  <div style="padding-left:20px">
				    <div class="card bg-light mb-1">
						  <p>{ current_user.skills1 }</p>
				    </div>
				    <div class="card bg-light mb-1">
						  <p>{ current_user.skills1 }</p>
				    </div>
				    <div class="card bg-light mb-1">
						  <p>{ current_user.skills1 }</p>
				    </div>
				    <div class="card bg-light mb-1">
						  <p>{ current_user.skills1 }</p>
				    </div>
					  <br>
				  </div>
			  </div>
	        </div>
		  </div>
		  <div class="col-lg-3">
		    <div class="row">
			    <div class="col-lg-2"><i class="fas fa-arrow-right" style="font-size:24px;color:#1CA0FA;"></i></div>
			    <div class="col-lg-10"><h5>Schools And Degrees</h5>
				<div style="padding-left:20px;">
					<div class="card bg-light mb-1">
						  <p>{ current_user.schoolname }e</p>
				  </div>
				    <div class="card bg-light mb-1">
						  <p>{ current_user.degree }</p>
				  </div>
				    <div class="card bg-light mb-1">
						  <p>{ current_user.study }</p>
				  </div>
				    <div class="card bg-light mb-1">
						  <p>{ current_user.date }</p>
				  </div>
				</div></div>
		    </div>
          </div>
	    </div>
		  <hr>
	    <div style="border-top:9px solid #1D80E7">
			  <br>
			  <br>
		  </div>
	    <div class="row">
		    <div class="col-lg-3"><div class="card">
  
  <div class="card-body">
    <h4 class="card-title">Project-1</h4>
    <p class="card-text">
     { current_user.project1 }
    </p>
    
  </div>
</div></div>
		    <div class="col-lg-3"><div class="card">
  
  <div class="card-body">
    <h4 class="card-title">Project-1</h4>
    <p class="card-text">
		{ current_user.project2 }
    </p>
    
  </div>
</div></div>
		    <div class="col-lg-3"><div class="card">
  
  <div class="card-body">
    <h4 class="card-title">Project-1</h4>
    <p class="card-text">
		{ current_user.project3 }
    </p>
    
  </div>
</div></div>
		    <div class="col-lg-3"><div class="card">
  
  <div class="card-body">
    <h4 class="card-title">Project-1</h4>
    <p class="card-text">
		{ current_user.project4 }
    </p>
    
  </div>
</div></div>
	    </div>
      </div>
        </body>
        <!-- body code goes here -->
    </html>""")
    f.close()
     
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    options = {'enable-local-file-access': None}
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(name, sname, configuration=config, options=options)

def r_3_download():
    name = current_user.name + ".html"
    sname = r"resg\static\ " + current_user.name +".pdf"
    f = open(name, "w", encoding='utf-8')
    f.write(f"""
    
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Untitled Document</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

            <!-- jQuery library -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            
            <!-- Popper JS -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            
            <!-- Latest compiled JavaScript -->
            <link href="https://fonts.googleapis.com/css?family=Calistoga" rel="stylesheet">
            <link href='https://fonts.googleapis.com/css?family=Forum' rel='stylesheet'>
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
        </head>
        <body class="img-fluid">
        <div class="row" style="background: url(file:///D:/Python/RG/resg/static/bgimg.jpg)">
            <div class="col-lg-3 offset-lg-2"><img src="file:///D:/Python/RG/resg/static/logo.jfif" class="rounded-circle img-thumbnail img-fluid" alt="Image"></div>
            <div class="col-lg-6">
                <h1 class="lead" style="font-size:400%">{ current_user.name }
                </h1>
                <br>
                <h4 style="font-family:'Forum'; ">{ current_user.prof }</h4>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-9">
            
        <div class="row">
        <div class="col-lg-2"></div>
                <div class="col-lg-2" style="background-color:#CFCFCF"><br><p style="font-size:125%">Achievements</p></div>
                <div class="col-lg-7">
                    <br>
                <div class="row">
                    <div class="col-md-1"><i class="fas fa-angle-double-right" style="font-size:170%; color:#1CDB1F"></i></div>
                        <div class="col-md-10">
                            <div class="card bg-light pl-3">

                                { current_user.ach1 }<br>
                                { current_user.ach2 }<br>
                                { current_user.ach3 }<br>
                                { current_user.ach4 }<br>

                            </div>
                    </div>
                </div>
                </div>
        </div>
            <div class="row">
            <div class="col-lg-2"></div>
            <div class="col-lg-2" style="background-color:#CFCFCF"><br><p style="font-size:125%">Skills</p></div>
            <div class="col-lg-7">
                <br>
                <div class="row">
                    <div class="col-md-1"><i class="fas fa-angle-double-right" style="font-size:170%; color:#1CDB1F"></i></div>
                        <div class="col-md-10">
                            <div class="card bg-light pl-3">

                                { current_user.skills1 }<br>
                                { current_user.skills2 }<br>
                                { current_user.skills3 }<br>
                                { current_user.skills4 } <br>

                            </div>
                    </div>
                </div>
            </div>
            </div>
            <div class="row">
                <div class="col-lg-2"></div>
                <div class="col-lg-2" style="background-color:#CFCFCF"><br><p style="font-size:125%">Projects</p></div>
                <div class="col-lg-7">
                    <br>
                <div class="row">
                    <div class="col-md-1"><i class="fas fa-angle-double-right" style="font-size:170%; color:#1CDB1F"></i></div>
                        <div class="col-md-10">
                            <div class="card bg-light pl-3">

                                { current_user.project1 }<br>
                                { current_user.project2 }<br>
                                { current_user.project3 }<br>
                                { current_user.project4 } <br>

                            </div>
                    </div>
                </div>
                </div>
        </div>
        </div>		
        <div class="col-lg-3">
                <div class="row">
                    <div class="col-md-6">
                        <p>Address</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.residence }</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Phone No.</p>
                    </div>
                    <div class="col-md-6">
                        <p>+91 999955551</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Jobtitle</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.jobtitle }</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Employer</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.employer }</p>
                    </div>
                </div>
            <hr class="alert-dark">
                <div class="row">
                    <div class="col-md-6">
                        <p>School Name</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.schoolname }</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Degree</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.degree }</p>
                    </div>
                </div>
            <div class="row">
                    <div class="col-md-6">
                        <p>Study</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.study }</p>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-6">
                        <p>Date of Graduation</p>
                    </div>
                    <div class="col-md-6">
                        <p>{ current_user.date }</p>
                    </div>
                </div>
            </div>
        </div>
        <!-- body code goes here -->
    </html>""")
    f.close()
     
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    options = {'enable-local-file-access': None}
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(name, sname, configuration=config, options=options)
def r_4_download():
    name = current_user.name + ".html"
    sname = r"resg\static\ " + current_user.name +".pdf"
    f = open(name, "w", encoding="utf-8")
    f.write(f"""
    
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Untitled Document</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

            <!-- jQuery library -->
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            
            <!-- Popper JS -->
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
            
            <!-- Latest compiled JavaScript -->
            <link href="https://fonts.googleapis.com/css?family=Calistoga" rel="stylesheet">
            <link href='https://fonts.googleapis.com/css?family=Forum' rel='stylesheet'>
            <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
        </head>
        <body class="img-fluid">
            <div class="container">
		  <div class="row">
			  <div class="col-md-3">
				  <div style="background-color:peachpuff">
					  <div style="text-align: center">
					  <img src="file:///D:/Python/RG/resg/static/logo.jfif" class="rounded-circle img-thumbnail img-fluid" alt="Image" ></div>
					  <div class="ml-3">
				  	<h5>{ current_user.name }</h5>
					<p><i>{ current_user.prof }</i></p>
					<p><i>{ current_user.age }</i></p>
					<p><i>{ current_user.residence }</i></p>
					<hr>
					<h6>Experience</h6>
					<p><i>{ current_user.jobtitle }</i></p>
					<p><i>{ current_user.employer }</i></p>
					<hr>
						  <h6>Education</h6>
						  <p><i>{ current_user.schoolname }</i></p>
						  <p><i>{ current_user.degree }</i></p>
						  <p><i>{ current_user.study }</i></p>
						  <p><i>{ current_user.date }</i></p>
					  </div>
				  </div>
			  </div>
			  <div class="col-md-9">
				  <div class="row">
					  <div class="col-md-4">
				  <h3 style="color:peru; border-bottom:2px groove #000000; text-align:center">Achievements</h3>
				  <div class="pl-4">
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.ach1}
					  </p>
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.ach2}
					  </p>
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.ach3}
					  </p>
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.ach4}
					  </p>
			    </div>
			  </div>
			  <div class="col-md-4">
				  <h3 style="color:peru; border-bottom:2px groove #000000; text-align:center">Skills</h3>
				  <div class="pl-4">
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.skills1 }
					  </p>
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.skills2 }
					  </p>
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.skills3 }
					  </p>
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.skills4 }
					  </p>
			    </div>
			  </div>
			  <div class="col-md-4">
				  <h3 style="color:peru; border-bottom:2px groove #000000; text-align:center">Projects</h3>
				  <div class="pl-4">
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.project1 }
					  </p>
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.project2 }
					  </p>
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.project3 }
					  </p>
					  <p style="border-left-width:2px; border-left-style: solid; border-left-color: darkgoldenrod; padding-left:3px; ">
						{ current_user.project4 }
					  </p>
			    </div>
			  </div>
				  </div>
				  <div class="row">
				  	<div class="col-md-4">Hardware Managment 💦</div>
					  <div class="col-md-6">
					  <div class="progress">
						<div class="progress-bar" role="progressbar" style="width: 90%; background-color:yellow" aria-valuenow="41" aria-valuemin="10" aria-valuemax="100"></div>
					</div></div>
					 </div>
				  	<div class="row">
				  	<div class="col-md-4">Problem Solving 💦</div>
					  <div class="col-md-6">
					  <div class="progress">
						<div class="progress-bar" role="progressbar" style="width: 80%; background-color:orange" aria-valuenow="41" aria-valuemin="10" aria-valuemax="100"></div>
					</div></div>
					 </div><div class="row">
				  	<div class="col-md-4">Data Formatting 💦</div>
					  <div class="col-md-6">
					  <div class="progress">
						<div class="progress-bar" role="progressbar" style="width: 70%; background-color:darkorange" aria-valuenow="41" aria-valuemin="10" aria-valuemax="100"></div>
					</div></div>
					 </div>
				  <div class="row">
				  	<div class="col-md-4">Sofware Systems 💦</div>
					  <div class="col-md-6">
					  <div class="progress">
						<div class="progress-bar" role="progressbar" style="width: 60%; background-color:orangered" aria-valuenow="41" aria-valuemin="10" aria-valuemax="100"></div>
					</div></div>
					 </div>
				  <div class="row">
				  	<div class="col-md-4">Probability 💦</div>
					  <div class="col-md-6">
					  <div class="progress">
						<div class="progress-bar" role="progressbar" style="width: 50%; background-color:red" aria-valuenow="41" aria-valuemin="10" aria-valuemax="100"></div>
					</div></div>
					 </div>
				  	<div class="row">
				  	<div class="col-md-4">AI  💦</div>
					  <div class="col-md-6">
					  <div class="progress">
						<div class="progress-bar" role="progressbar" style="width:10%; background-color:darkred" aria-valuenow="41" aria-valuemin="10" aria-valuemax="100"></div>
					</div></div>
					 </div>
				</div>
		    
		  </div>
	  </div>
        </body>
        <!-- body code goes here -->
    </html>""")
    f.close()
     
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    options = {'enable-local-file-access': None}
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(name, sname, configuration=config, options=options)


#SlenderBot Chromium
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['POST','GET'])
def register():
    form = RF()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.pwd.data).decode('utf-8')
        usernew = User(name = form.name.data,
                       password = hashed_password,
                        age = form.age.data,
                       residence = form.residence.data,
                       prof = form.prof.data,
                       ach1 = form.ach1.data,
                       ach2 = form.ach2.data,
                       ach3 = form.ach3.data,
                       ach4 = form.ach4.data,
                       jobtitle = form.jobtitle.data,
                       employer = form.employer.data,
                       schoolname = form.schoolname.data,
                       degree = form.degree.data,
                       study = form.study.data,
                       date = form.date.data,
                       skills1 = form.skill1.data,
                       skills2 = form.skill2.data,
                       skills3 = form.skill3.data,
                       skills4 = form.skill4.data,
                       project1 = form.project1.data,
                       project2 = form.project2.data,
                       project3 = form.project3.data,
                       project4 = form.project4.data)
        #we can try and encrypt stuff but I don't think it is nessesary... We can do that after the project is finished!
        db.session.add(usernew)
        db.session.commit()
        name = current_user.name + ".html"
        sname = "resg/static/" + current_user.name + ".pdf"
        f = open(name, "w")
        f.write("")
        f.close()
        f = open(sname, "w")
        f.write("")
        f.close()
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register1.html", form=form)
@app.route("/login", methods=['POST', 'GET'])
def login():
    form = LF()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash("Unsuccesful", "danger")
            
    return render_template("login.html", form=form)
        
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
@app.route("/account")
@login_required
def account():
    skills = str(current_user.skills1) + " | " + str(current_user.skills2) + " | " + str(current_user.skills3) + " | " + str(current_user.skills4) + " | " 
    return render_template('account.html', skills=skills)

@app.route("/home-resumes")
@login_required
def home_resumes():
    return render_template("home-resume.html")
@app.route("/resume/1")
@login_required
def resume_1():
    r_1_download()
    return render_template("tem1.html")

@app.route("/resume/2")
@login_required
def resume_2():
    r_2_download()
    return render_template("tem2.html")
     

@app.route("/resume/3")
@login_required
def resume_3():
    r_3_download()
    return render_template("tem3.html")

@app.route("/resume/4")
@login_required
def resume_4():
    r_4_download()
    return render_template("tem4.html")

@app.route("/resume/download")
@login_required
def next():
    name = "/static/ " + current_user.name + '.pdf'
    return render_template("download_tem.html", name=name)

@app.route("/account/update", methods=["GET", "POST"])
@login_required 
def accupd():
    form = UA()
    if form.validate_on_submit():
        current_user.name = form.name.data                             
        current_user.age = form.age.data
        current_user.residence = form.residence.data
        current_user.prof = form.prof.data 
        current_user.ach1 = form.ach1.data 
        current_user.ach2 = form.ach2.data 
        current_user.ach3 = form.ach3.data 
        current_user.ach4 = form.ach4.data 
        current_user.jobtitle = form.jobtitle.data 
        current_user.employer = form.employer.data 
        current_user.schoolname = form.schoolname.data 
        current_user.degree = form.degree.data 
        current_user.study = form.study.data 
        current_user.date = form.date.data 
        current_user.skills1 = form.skill1.data 
        current_user.skills2 = form.skill2.data 
        current_user.skills3 = form.skill3.data 
        current_user.skills4 = form.skill4.data 
        current_user.project1 = form.project1.data 
        current_user.project2 = form.project2.data 
        current_user.project3 = form.project3.data 
        current_user.project4 = form.project4.data

        db.session.add()
        db.session.commit()
        return redirect("/account")
    form.name.data = current_user.name
    form.residence.data = current_user.residence
    form.age.data = current_user.age
    form.ach1.data = current_user.ach1
    form.ach2.data = current_user.ach2
    form.ach3.data = current_user.ach3
    form.ach4.data = current_user.ach4
    form.prof.data = current_user.prof
    form.jobtitle.data = current_user.jobtitle
    form.employer.data = current_user.employer
    form.skill1.data = current_user.skills1
    form.skill2.data = current_user.skills2
    form.skill3.data = current_user.skills3
    form.skill4.data = current_user.skills4
    form.schoolname.data = current_user.schoolname
    form.study.data = current_user.study
    form.degree.data = current_user.degree
    form.date.data = current_user.date
    form.project1.data  = current_user.project1
    form.project2.data = current_user.project2
    form.project3.data = current_user.project3
    form.project4.data = current_user.project4
    return render_template("account-update.html", form=form)