class OnlineShop:
    def __init__(self):
        self.caps_price = 5
        self.shirts_price = 10
        self.hoodies_price = 20
        
    
    def cal(self, caps, shirts, hoodies):
        tc = (caps * self.caps_price) + (shirts * self.shirts_price) + (hoodies * self.hoodies_price)
        return tc

c = int(input("Enter the number of caps: "))
s = int(input("Enter the number of shirts: "))
h = int(input("Enter the nummber of hoodies: "))

shop = OnlineShop().cal(c,s,h)
# tot_cost = shop.cal(c,s,h)
print(f"the total cost is: {shop}")