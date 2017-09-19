<?php
$dt = date("Y-m-d");
$uploaddir = "$dt/";
$uploadfile = $uploaddir . basename( $_FILES['file']['name']);
$fname = basename($_FILES['file']['name']);
$username = null;
$password = null;

if(isset($_SERVER['PHP_AUTH_USER'])){
	        $username = $_SERVER['PHP_AUTH_USER'];
		        $password = $_SERVER['PHP_AUTH_PW'];

} else if (isset($_SERVER['HTTP_AUTHORIZATION'])){
	        if (strpos(strtolower($_SERVER['HTTP_AUTHORIZATION']),'basic')===0)
			          list($username,$password) = explode(':',base64_decode(substr($_SERVER['HTTP_AUTHORIZATION'], 6)));
}

if ($username == ("yourusername") && ($password == ("yourpassword"))){


	if (!file_exists($uploaddir)) {
		        mkdir ($uploaddir, 0750, true);
	}

	if(move_uploaded_file($_FILES['file']['tmp_name'], $uploadfile))
	{
		  print "The file has been uploaded successfully \n";
		    print "https://s.james.ac/?d=$dt&f=$fname";
	}
	else
	{
		  print "There was an error uploading the file";
	}
}else{
	print "Wrong credentials";
	exit();
}
?>
