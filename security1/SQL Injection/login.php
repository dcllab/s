<?php
	$username = $_POST['username'];
	$password = $_POST['password'];
	
	// $username = $mysqli -> real_escape_string($_POST['username']);
	// $password = $mysqli -> real_escape_string($_POST['password']);

	$conn = new mysqli("localhost:3306", "root", "", "samplee");
	$sql = "SELECT * FROM usertable where username = '".$username."' and password = '".$password."'";
	$result = $conn->query($sql);

	if ($result->num_rows > 0)
		header("Location: home.php");
	else
		header("Location: error.php");
?>