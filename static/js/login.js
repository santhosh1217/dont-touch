var btn=document.getElementById('btn')

document.getElementById("type").value = "admin";

function leftClick() 
{
	window.location.reload();
	btn.style.left='0';
	document.getElementById("type").value = "admin";
	document.getElementById("user").innerHTML = "admin";
	document.body.style.backgroundImage="url(https://s3.amazonaws.com/prod.static-content.quillette.com/2022/06/Student.png)";
	document.getElementById("signup").style.visibility = "visible";
}

function rightClick() 
{
	
	btn.style.left='110px';
	document.getElementById("type").value= "staff";
	document.getElementById("user").innerHTML = "staff";
	document.body.style.backgroundImage="url(https://s3.amazonaws.com/prod.static-content.quillette.com/2022/07/Aging.png)";
	document.getElementById("signup").style.visibility = "hidden";
	
}
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

function rightClick() 
{
	
	btn.style.left='110px';
	document.getElementById("type").value= "staff";
	document.getElementById("user").innerHTML = "staff";
	document.body.style.backgroundImage="url(https://s3.amazonaws.com/prod.static-content.quillette.com/2022/07/Aging.png)";
	document.getElementById("signup").style.visibility = "hidden";
}

function Func()
{
	var k = document.getElementById("main").innerHTML
			
			
	if ( k == 3 || k==4)
	{
		
			
		
		
	}
	else
	{
		window.location.reload();
	}

}

var k = document.getElementById("main").innerHTML 
if (k == 1 || k == 3 )
{
		if(k==3)
			{
				rightClick()
				document.getElementById("us").style.borderBottom = "1px solid red";
				
			}
		document.getElementById("us").style.borderBottom = "1px solid red";
			
}		setTimeout(Func,3000)
if(k==2 || k==4)
{
			
		if(k==4)
		{
			rightClick()
			document.getElementById("ps").style.borderBottom = "1px solid red";
				
		}

		document.getElementById("ps").style.borderBottom = "1px solid red";
		
		setTimeout(Func,3000)

				
}



