var AN, PN;

function main()
{
    AN = document.getElementById("AN").value;
	PN = document.getElementById("PN").value;
	if(AN == "" && PN == "")
	{
		alert("Enter Your Credentials");
	}
	else if(AN =="")
	{
		alert("Enter Adhar Number");
	}
	else if(PN == "")
	{
		alert("Enter Your Phone Number");
	}
	else
	{	
		var b[strlen(AN)];
		for(var i=0;i<(AN.length/2);i++)
			b[i] = AN[i];
		alert(b);
		
	}
		
}



function main2()
{
	var otp = document.getElementById("otp").value;
	if(otp == "4347")
	{
		document.getElementById("osub").action = "https://www.google.com"
	}
	else
	{
		alert("Not done");
	}
}

function two()
{
	
	if(AN == "" && PN == "")
	{
		alert("Enter Your Credentials");
	}
	else if(AN =="")
	{
		alert("Enter Adhar Number");
	}
	else if(PN == "")
	{
		alert("Enter Your Phone Number");
	}
	else
	{
		alert("OTP : 4347")
	}
}