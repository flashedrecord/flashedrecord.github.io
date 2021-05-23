function dobackground() {
  var ctxt1 = document.getElementById("ctxt");
  if (ctxt1.value != "") {
  document.getElementById("cv1").style.backgroundColor = ctxt1.value;
  }
  ctxt1.value = "";
}
function dobox() {
  var canvas = document.getElementById("cv1");
  var context = canvas.getContext("2d");
  context.fillStyle = document.getElementById("bctxt").value;
  context.fillRect(10,10,100,50);
  
  var ftxt1 = document.getElementById("ftxt").value
  context.fillStyle = document.getElementById("fctxt").value;
  context.font = "bold 35px Arial";
  context.strokeText(ftxt1, 15, 45)
}