from datetime import datetime
from time import strftime
from tkinter import Y
class Shop:
    def __init__(self,company_name,item):
        self.company_name=company_name
        self.item=item
        self.initial_kg=0
     

    def stock_kg(self,kgs):
        datee=datetime.now()
        self.kgs=kgs
        if kgs<=0:
            return f"enter valid kgs"
        else:
            self.initial_kg+=self.kgs
            return f"you have added {self.initial_kg}kgs today {datee.strftime('%d/%m/%y, %H:%M:%S')}"
   
    def sold_stock(self,kgs):
        self.kgs=kgs
        if kgs>self.initial_kg:
            return f"sorry we have less kgs in the stock"
        else:
            self.initial_kg-=self.kgs
            return f"hello you have sold {self.kgs}.and you {self.initial_kg}remaining "    

        
    