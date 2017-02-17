//
//function printForm(){
//  var fname=document.forms["myform"]["firstname"].value;
//  var lname=document.forms["myform"]["lastname"].value;
//  var mobile=document.forms["myform"]["mobile"].value;
//  var email=document.forms["myform"]["email"].value;
//  var gender=document.forms["myform"]["gender"].value;
//  var address=document.forms["myform"]["address"].value;
//
//
//if(email.length!=0 && mobile.length!=0){
//document.getElementById('printvalue').innerHTML="First Name:  "+fname+"Last Name:   "
//+"<br>"+lname+"<br>Email:  "+email+"<br>Mobile: "+mobile
//+"<br>Gender:  "+gender+"<br>Address:  "+address;
//}
//else{
//  document.getElementById('mobilemsg').innerHTML="Please enter mobile number";
//  document.getElementById('emailmsg').innerHTML="Please enter email address";
//
//}
//}
function firstNameError(){
  var fname=document.forms["myform"]["cust_name"].value;
//  document.write(fname)
  if(fname.length>25){
  myform.cust_name.value="";
    document.getElementById('firstmsg').innerHTML="should be less or equal to than 25 characters";
  }else{
    document.getElementById('firstmsg').innerHTML="";

  }


}

//function mobileError(){
//  var mobile=document.forms["myform"]["mobile"].value;
//  var reg=/[0-9]+/;
//  if(mobile.length ==10 && reg.test(mobile)==true){
//    document.getElementById('mobilemsg').innerHTML="";
//
//  }
//  else{
//    myform.mobile.value="";
//
//    document.getElementById('mobilemsg').innerHTML="should be 10 numbers";
//  }
//
//}


function emailError(){
  var email=document.forms["myform"]["cust_email"].value;

 var reg =  /([A-Za-z0-9])+@([A-Za-z])+\.([A-Za-z]{2,4})/;
 if ((reg.test(email))==false) {
  document.getElementById('emailmsg').innerHTML="enter correct email address";
  myform.cust_email.value="";

}
else {  document.getElementById('emailmsg').innerHTML="";

}

}

function redirecting(){
    window.location = "{% static 'bankWebApp/login.html' %}";
}