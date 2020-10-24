
<!doctype html>
<html lang="en" dir='ltr'>
<style>
#page{
  font-family:Tajawal;
  text-align: center;
    font-weight: bold;
      color: black;
 
}
#form{
 width: 300px;
  height: 300px;
  background-color: white;
  font-family:Tajawal;
  text-align: left;
  padding: 8px;
  font-weight: bold;
    color: red;

}




#frm{
  background-color: white;
  font-family:Tajawal;
  text-align: right;
  padding: 8px;
  font-weight: bold;
    color: red;
    border-style: solid;
border-width: 5px;
border-color: red;
}

#div{

  background-color: white;
  font-family:Tajawal;
  text-align: right;
  padding: 8px;
  font-weight: bold;
    color: red;
    border-style: solid;
border-width: 5px;
border-color: pink;
}
</style>


  <head>
   
    <title>واجهــة الحجــز</title>
  </head>
  <body id='form'>
  <br><br>
 <form id='frm' action='' method='POST'>
{%csrf_token %}
{{ formregister.as_p}}
<button id="page" type="submit">حـــجز</button>
<br><br><br><br><br><br><br><br><br><br><br>
<div id='div'>
<a  href="{% url 'index' %}"> قائمـة الحجــز </a>
</div>
</form>
  </body>
</html>