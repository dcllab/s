<?php 
	if(false && !isset($_COOKIE['USER_NAME']))
		echo "Need to login";
	else {
		$servername = "localhost";
		$username = "root";
		$password = "";
		$dbname = "users";
		$conn = new mysqli($servername, $username, $password, $dbname);
		if($_SERVER['REQUEST_METHOD'] == "POST") {
			echo "Welcome User";
			$sql="update user set username='".
			$_POST['disp_name']."' where username='".
			$_COOKIE['USER_NAME']."';";
			$result = $conn->query($sql);
			echo "Update Success";
		}
		else {
			if(strcmp($_COOKIE['USER_NAME'],'admin')==0) {
				echo "Welcome admin<br><hr>";
				echo "List of user's are<br>";
				$sql = "select username from user where username!='admin'";
				$result = $conn->query($sql);
				if ($result->num_rows > 0) 
					while($row=$result->fetch_assoc())
						echo " UserName: " . $row["username"]."<br>";
			} else {
				echo "<form name=\"tgs\" id=\"tgs\" method=\"post\" action=\"home.php\">";
				echo "Update name:<input type=\"text\" id=\"disp_name\" name=\"disp_name\" value=\"\">";
				echo "<input type=\"submit\" value=\"Update\">";
			}
		}
	}
?>