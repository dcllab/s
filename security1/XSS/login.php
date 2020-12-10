<?php
	$name = $_POST['username'];
	$id = $_POST['password'];
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "users";
	
	$conn = new mysqli($servername, $username, $password, $dbname);
	
	$sql = "SELECT username, password FROM user WHERE username='$name'";
	echo $sql;
	$result = $conn->query($sql) or die($conn->error);
	$row=$result->fetch_assoc();
	
	echo $name;
	echo $id;
	$user_pass = $_POST['password'];
	$user_name = $row['username'];
	
	if(strcmp($user_pass,$row['password'])!=0) {
		echo "Login failed";
	} else {
		# Start the session session_start();
		setcookie("USER_NAME", $user_name, time()+3600*24*30, '/');
        setcookie("PASSWORD", $user_pass);
		echo "<head> <meta http-equiv=\"Refresh\" content=\"0;url=home.php\" > </head>";
	}
?>