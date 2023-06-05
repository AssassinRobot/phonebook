class car(object):
    def __init__(self,made,model,mark,seris):
        self.mark=mark
        self.model=model
        self.seris=seris
        self.made=made
    def printe(self):
        return f"this car is a {self.mark} {self.model} {self.seris} made in {self.made}"
samand=car(1388,"samand","pejo",88)
#print(samand.printe())
class grade(object):
    def __init__(self,math,sience,poemic,art,english,history):
        math=self.math=math
        sience=self.sience=sience
        poemic=self.poemic=poemic
        art=self.art=art
        english=self.english=english
        history=self.history=history
    def miangin(self):
        return(self.math/6+self.sience/6+self.poemic/6+self.art/6+self.english/6+self.history/6)
grades=grade(18.3,12.9,8.9,4.25,20,19)
#print(grades.miangin())