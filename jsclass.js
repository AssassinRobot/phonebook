function car(mark,model,seris,made){
    mark=this.mark=mark
    model=this.model=model
    seris=this.seris=seris
    made=this.made=made
    this.print=function(){
        a="this car is a "+mark+" "+model+" "+seris+" made in "+made
        return a
    }
}
samand=new car("pjo","samand","88","1388")
console.log(samand.print())