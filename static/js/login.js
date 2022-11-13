
var btn=document.getElementById('btn')

document.getElementById("type").value = "admin";


function chck()
{
	document.getElementById("log").action = '';
	var id = document.getElementById("us").value;
	if (document.getElementById("type").value != "admin")
	{
		alert("staff login");
		document.getElementById("log").action =id+ "/departments";
	}
	else
	{
		alert("admin login");
		document.getElementById("log").action =id+ "/admin";
	}
}



function Func()
{
	var k = document.getElementById("main").innerText
			
			
	if ( k == 3 || k==4)
	{
		
			
		
		
	}
	else
	{
		window.location.reload();
	}

}

var k = document.getElementById("main").innerText; 
if (k == 1 || k == 3 )
{
		if(k==3)
			{
				rightClick()
				document.getElementById("us").style.borderBottom = "1px solid red";
				
			}
		document.getElementById("us").style.borderBottom = "1px solid red";
			
}		//setTimeout(Func,3000)
if(k==2 || k==4)
{
			
		if(k==4)
		{
			rightClick()
			document.getElementById("ps").style.borderBottom = "1px solid red";
				
		}

		document.getElementById("ps").style.borderBottom = "1px solid red";
		
		//setTimeout(Func,5000)

				
}



