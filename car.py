class Car:

    def setColor(self, color, brand, model):
        
        self.color = color
        self.brand = brand
        self.model = model

car1 = Car()

brand = input ('would you order buying a car from which company? ')
model = input ('enter the model you selected? ')
color = input ('and what color? ')
car1.setColor(color,brand,model)
print ('your order was registred. your', car1.brand,car1.model,car1.color ,'will be reday as soon as possible!')