function main()
{
	name = document.getElementById("username").value;
	passwd = document.getElementById("passwd").value;
	if(name == "" && passwd == "")
	{
		
		document.getElementById("error").innerHTML = "Enter your Credentials";
	}
	else if(name == "" && passwd != "")
	{	
		document.getElementById("error").innerHTML  = "Enter Your Name";

	}
	else if(passwd == "" && name != "" )
	{	
		document.getElementById("error").innerHTML = "Enter Your Password";
	}
	else 
	{
		document.getElementById("my-login").action = "./content/home.html";
	}
	
	var x = document.getElementById("error");
	x.style.display = "none"
  	if (x.style.display === "none") {
   		 x.style.display = "block";
  	} 
  	else {
   	 x.style.display = "none";
 	 }
 	 

}