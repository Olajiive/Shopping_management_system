items = []
while True:
    print('----------------------Welcome to the supermarket------------------------------')
    print('1. View items \n2. Add new items \n3. Purchasing \n4. Searching \n5. Editing \n6. Exit')
    options = input("Enter the number of your choice: ")
    if options == str(1) :
        print("---------------------View Items---------------------")
        print("Total inventory are :", len(items))
        while len(items) != 0:
            print("Available items")
            for item in items:
                for key, value in item.items():
                    print(key, ":", value)
            break
    
    elif options == str(2):
        print("-----------------------Add items---------------------")
        print("Adding new items")
        item = {}
        item["name"] = input('Item name :')
        while True:
            try:
                item["qty"] = int(input("Item quantity: "))
                break
            except ValueError:
                print("Enter numeric figure")
        while True:
            try:
                item["price"] = int(input("Price: "))
                break
            except ValueError:
                print("Enter numeric figure")
        print("Item has been successfully added. ")
        items.append(item)
    
    elif options ==  str(3) :
        print("----------------------purchase items------------------------")
        print(items)
        pur_item = input("Which item do you want to purchase? Enter name: ")
        for item in items:
            if pur_item.lower() == item['name'].lower() :
                if item["qty"] != 0:
                    print('pay', item["price"], "at checkout counter")
                    item["qty"] -= 1
                else:
                    print('Item out of stock')

    elif options == str(4) :
        print("-------------------Search items--------------------")
        fd_item = input('Enter the item \'s name to search in inventory: ')
        for item in items:
            if item["name"].lower() == fd_item.lower() :
                print('The item named' + fd_item + "is  displayed below with its details")
                print(item)
            else:
                print('item not found.')
    
    elif options == str(5) :
        print("-----------------------Edit items-----------------------")
        it_name = input("Enter the name of the item that you want to edit : ")
        for item in items:
            if it_name.lower() == item['name'].lower():
                print(f'current details of {it_name}')
                print(item)
                item["name"] = input("Item name: ")
                while True:
                    try:
                        item["qty"] = int(input("item quantity : "))
                        break
                    except ValueError:
                        print("Enter numeric figure")
                while True:
                    try:
                        item["price"] = int(input('price $ :'))
                        break
                    except ValueError:
                        print("Enter numeric figure")
                
                print("Item has been successfully updated.")
                print(item)
            
            else:
                print('Item not found')
    elif options == str(6) :
        print("------------------------exited----------------------")
        break
    else:
        print("You entered an invalid option")