document.getElementById("worker").onchange = () => {
  document.getElementById("addressFormItem").style.display = "none";
  document.getElementById("address").value = "";
};
document.getElementById("customer").onchange = () => {
  document.getElementById("addressFormItem").style.display = "block";
};
