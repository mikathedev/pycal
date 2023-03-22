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
        ansdenom =denom
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