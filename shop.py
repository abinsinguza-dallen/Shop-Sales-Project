from datetime import datetime
from time import strftime
from tkinter import Y
class Shop:
    def __init__(self,company_name,item):
        self.company_name=company_name
        self.item=item
        self.initial_kg=0
        self.price=10000
        self.daily=0
        self.weekkly=[]
        self.total_kgs=[]
        self.sold_kgs=[]
     

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
            self.sold_kgs.append(self.kgs)
        return f"hello you have sold {self.kgs}.and you {self.initial_kg}remaining "    

    def products_sold(self,kgs):
        ttl_kg=0
        for k in self.sold_kgs:
            ttl_kg+=k
        if kgs>ttl_kg:
            return "invalid kilogrames"    
        else:
            self.daily=self.price*kgs
            self.total_kgs.append(kgs)
            self.weekkly.append(self.daily)
            return self.daily
    
    def weekly_collections(self):
        sum=0
        for y in self.weekkly:
            sum+=y
        total=0
        for m in self.total_kgs:
            total+=m    
        return f"hello your weekly collections is UGX{sum}  from {total} kilograms"



    