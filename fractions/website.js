function fractions(){
var numar = prompt("what da numaraqter")
var denom = prompt("what da denomarater")
var what = prompt("what 1 for mfbwn 2 for mfbf and 3 for af")
function mfbwn()
{
var num = prompt("multiplyd by") 
var ans = Number(num)*Number(numar)
alert(ans+"/"+denom)
}

function mfbf(){
    var numar2 = prompt("second numaraqter")
    var denom2 = prompt("second denomarater")
    var ansnuma = Number(numar)*Number(numar2)
    var ansdenom = Number(denom)*Number(denom2)
    alert(ansnuma+"/"+ansdenom)
    
}

function af(){
    var numar2 = prompt("second numaraqter")
    var denom2 = prompt("second denomarater")
    if(denom2 == denom){
        ansnuma = Number(numar)+Number(numar2)
        ansdenom = denom
    }
    else{
        var ansdenom = denom2*denom
    }

}

if (what == "1"){

    mfbwn()
    
}
else {if(what == "2"){
    mfbf()
}
else{if(what == "3"){

af()
}
}
}
}
function cal(){
    var how = prompt("1 to add 2 to subtract 3 to multiply 4 to divide")
var num1 = prompt("Enter first number")
var num2 = prompt("Enter second number")
if(how == "1"){
    var ans = Number(num1)+Number(num2)
    alert(ans)
}
else if(how == "2"){
    var ans = Number(num1)-Number(num2)
    alert(ans)
}
else if(how == "3"){
    var ans = Number(num1)*Number(num2)
    alert(ans)
}
else if(how == "4"){
    var ans = Number(num1)/Number(num2)
    alert(ans)
}

    
}

var cof = prompt("1 for calculater 2 for fractions")
if(cof == "2"){
    fractions()
}

else{
    cal()
}