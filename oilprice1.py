print("################################################################################")
print("###########                                                         ############")
print("###########                                                         ############")
print("###########                                                         ############")
print("###########                     Welcome                             ############")
print("###########                                                         ############")
print("###########                                                         ############")
print("###########                                                         ############")
print("###########                                                         ############")
print("###########                                                         ############")
print("################################################################################")


print("################################################################################")
print("###########                          price oil                      ############")
print("###########                                                         ############")
print("###########        1.Gasoline 95 ราคา 29.16 BATH                    ############")
print("###########        2.Gasoline 91 ราคา 25.30 BATH                    ############")
print("###########        3.Gasohol 91  ราคา 21.68 BATH                    ############")
print("###########        4.GasoholE20  ราคา 20.2  BATH                    ############")
print("###########        5.Gasohol 95  ราคา 21.2  BATH                    ############")
print("###########        6.Diesel ราคา 21.1 BATH                          ############")
print("###########                                                         ############")
print("################################################################################")

       
f = int(input("which type of fuel do you want?"))

print("################################################################################")
print("###########                           price oil                      ###########")
print("###########                                                          ###########")
print("###########                                                          ###########")
print("###########                                                          ###########")
print("###########         1.คำนวณเงินเป็นลิตร                                 ###########")
print("###########         2.คำนวณลิตรเป็นเงิน                                 ###########")
print("###########                                                          ###########")
print("###########                                                          ###########")
print("###########                                                          ###########")
print("################################################################################")

c = int(input())

p  = float(input())

if (f == 1):
	if c == 1:
		total = p / 29.16
	elif c == 2:
		total = p * 29.16
elif (f == 2):
	if c == 1:
		total = p / 25.30
	elif c == 2:
		total = p * 25.30
elif (f == 3):
	if c == 1:
		total = p / 21.68
	elif c == 2:
		total = p * 21.68
elif (f == 4):
	if c == 1:
		total = p / 20.2
	elif c == 2:
		total = p * 20.2
elif (f == 5):
	if c == 1:
		total = p / 21.2
	elif c == 2:
		total = p * 21.2
elif (f == 6):
	if c == 1:
		total = p / 21.1
	elif c == 2:
		total = p * 21.1
print(total)