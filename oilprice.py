while True:
    print("#"*80)
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*25 + "Welcome" + " "*25 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("#"*80)

    print("#"*80)
    print("###########" + " "*25 + "price oil" + " "*23 + "############")
    print("###########" + " "*57 + "############")
    print("#"*11 + " "*8 + "1.Gasoline 95 ราคา 29.16 BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "2.Gasoline 91 ราคา 25.30 BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "3.Gasohol 91  ราคา 21.68 BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "4.GasoholE20  ราคา 20.2  BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "5.Gasohol 95  ราคา 21.2  BATH" + " "*20+"#"*12)
    print("#"*11 + " "*8 + "6.Diesel ราคา 21.1 BATH" + " "*26+"#"*12)
    print("###########" + " "*57 + "############")
    print("#"*80)

    f = int(input("which type of fuel do you want?"))

    print("#"*80)
    print("###########" + " "*25 + "price oil" + " "*23 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("#"*11 + " "*8 + " "*10 + "1.คำนวณเงินเป็นลิตร" + " "*23 + "#"*12)
    print("#"*11 + " "*8 + " "*10 + "2.คำนวณลิตรเป็นเงิน" + " "*23 + "#"*12)
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("###########" + " "*57 + "############")
    print("#"*80)

    c = int(input())

    p = float(input())

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
    input_exit = input()
    if (input_exit == "exit"):
        break
