class WeightCalculator:

    #staticmethod
    def calculate_weight(height, age):
        recommended_weight = (height - 100 + age%10)*0.09
        #return recommended_weight
    

h = float(input("enter you height: "))
a = int(input("enter your age: "))

rw = WeightCalculator.calculate_weight(h, a)
print(rw)