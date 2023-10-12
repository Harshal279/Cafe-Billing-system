# class cafe:
#     def __init__(self, Total_cost, age):
#       self.Total_cost = Total_cost
#       self.age = age

running=True
while running:
   print("1.vegn\n2.non veg\n3.bevreges\n4.close")
   choice=int(input("enter the choice"))
   if choice==1:
      veg_running=True
      while veg_running:
         print("1.Chai: A spiced tea made with black tea leaves, milk, sugar, and a blend of aromatic spices like cardamom, ginger, and cloves.\n 2.Samosas: Deep-fried pastry pockets filled with a mixture of potatoes, peas, and spices.\n3.Pakoras: Deep-fried fritters made from various ingredients like onions, potatoes, spinach, or eggplants, coated in gram flour batter.Aloo \n4.Tikki: Spiced mashed potato patties, often served with chutney and yogurt.\n5. close")
         veg_choice=int(input("enter the choice"))
         sub_Total=0
         if veg_choice==1:
            print("\n chai ordered\n")
            sub_Total=sub_Total+10
         elif veg_choice==2:
            print("\n Samosa ordered\n")
            sub_Total=sub_Total+20
         elif veg_choice==3:
            print("\n Pakaoras ordered\n")
            sub_Total=sub_Total+40
         elif veg_choice==4:
            print("\n Tikki ordered\n")
            sub_Total=sub_Total+50
         elif veg_choice==5:
            veg_running=False
            print("\n close\n")
         else:
            print("invalid input")
         print(sub_Total)
         
   elif choice==2:
      pass
   elif choice==3:
      pass
   elif choice==4:
      running=False
