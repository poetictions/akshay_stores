import getpass, sys
user_details = ""


products = {"Toiletries": [{"id":11, "name": "Toiletry Bag", "price": 1357, "discount": 0, "buying_price": 900},
                           {"id":12, "name": "SPC Plastic Multipurpose Cosmetic Toiletries", "price": 500, "discount": 55, "buying_price": 100},
                           {"id":13, "name": "Tide Plus Double Power Detergent Washing Powder", "price": 930, "discount": 8, "buying_price": 731},
                           {"id":14, "name": "Dettol Liquid Disinfectant", "price": 193, "discount": 24, "buying_price": 99},
                           {"id":15, "name": "Colgate Strong Teeth", "price": 325, "discount": 0, "buying_price": 232},
                           {"id":16, "name": "Colgate Visible White O2 manual Toothbrush", "price": 250, "discount": 20, "buying_price": 200}],
            "Food": [{"id":21, "name": "Fresh Banana Yelakki", "price": 135, "discount": 32, "buying_price": 90},
                     {"id":22, "name": "Fresh Organic French Beans", "price": 51, "discount": 0, "buying_price": 44},
                     {"id":23, "name": "Purina Supercoat Adult Dry Dog Food", "price": 695, "discount": 70, "buying_price": 121},
                     {"id":24, "name": "Aveeno Skin Relief Moisturizing Lotion", "price": 695, "discount": 0, "buying_price": 590},
                     {"id":25, "name": "True Elements Chia Seeds", "price": 500, "discount": 33, "buying_price": 300},
                     {"id":26, "name": "Assorted pack of Ragi, Jowar & Moringa crispies", "price": 240, "discount": 0, "buying_price": 100}],
            "Electronics": [{"id":31, "name": "OnePlus Nord 2T 5G", "price": 32914, "discount": 12, "buying_price": 21000},
                            {"id":32, "name": "boAt Xtend/Xtend RTL Smartwatch", "price": 7990, "discount": 62, "buying_price": 2000},
                            {"id":33, "name": "pTron Solero A15 3.5mm Male to Male Aux Cable", "price": 699, "discount": 0, "buying_price": 550},
                            {"id":34, "name": "Salcon 4 Mosfet Flat Audio Board", "price": 2499, "discount": 0, "buying_price": 1200},
                            {"id":35, "name": "65W OnePlus Warp Charge Type-C to Type-C Cable", "price": 999, "discount": 90, "buying_price": 860},
                            {"id":36, "name": "Smart Phones Auto Timer Lock Box", "price": 14652, "discount": 57, "buying_price": 12004}]
            }

            
class ViewProducts:
    def __init__(self):
        pass
    
    def all_products(self):        
        print("Toiletries")
        for i in range(6):
            print("\nProductID",products["Toiletries"][i]["id"], "\nName: ",products["Toiletries"][i]["name"],"\nPrice: ","INR", products["Toiletries"][i]["price"])
            if products["Toiletries"][i]["discount"] != "0":
                print("Discount: ", products["Toiletries"][i]["discount"],"%", "\nDiscounted Price: ","INR", round(int(products["Toiletries"][i]["price"]) - (int(products["Toiletries"][i]["discount"]) * int(products["Toiletries"][i]["price"]))/100, 2))
            else:
                pass
        
        print("\nFood")
        for i in range(6):
            print("\nProductID",products["Food"][i]["id"], "\nName: ",products["Food"][i]["name"],"\nPrice: ","INR", products["Food"][i]["price"])
            if products["Food"][i]["discount"] != "0":
                print("Discount: ", products["Food"][i]["discount"],"%", "\nDiscounted Price: ","INR", round(int(products["Food"][i]["price"]) - (int(products["Food"][i]["discount"]) * int(products["Food"][i]["price"]))/100, 2))
            else:
                pass
            
        print("\nElectronics")    
        for i in range(6):
            print("\nProductID",products["Electronics"][i]["id"], "\nName: ",products["Electronics"][i]["name"],"\nPrice: ","INR", products["Electronics"][i]["price"])
            if products["Electronics"][i]["discount"] != "0":
                print("Discount: ", products["Electronics"][i]["discount"], "%", "\nDiscounted Price: ","INR", round(int(products["Electronics"][i]["price"]) - (int(products["Electronics"][i]["discount"]) * int(products["Electronics"][i]["price"]))/100, 2))
            else:
                pass
        
    def one_type(self, product_type):
        print(product_type)
        for i in range(6):
            print("\nProductID",products[product_type][i]["id"], "\nName: ",products[product_type][i]["name"],"\nPrice: ","INR", products[product_type][i]["price"])
            if products[product_type][i]["discount"] != "0":
                print("Discount: ", products[product_type][i]["discount"],"%", "\nDiscounted Price: ","INR", round(int(products[product_type][i]["price"]) - (int(products[product_type][i]["discount"]) * int(products[product_type][i]["price"]))/100, 2))
            else:
                pass
            
    def searched_product(self, search):
        a = ("Toiletries", "Food", "Electronics")
        for i in range(3):
            for j in range(6):
                if search in (products[a[i]][j]["name"]).lower():
                    print("\nProductID",products[a[i]][j]["id"], "\nName: ",products[a[i]][j]["name"],"\nPrice: ","INR", products[a[i]][j]["price"])
                    if products[a[i]][j]["discount"] != "0":
                        print("Discount: ", products[a[i]][j]["discount"],"%", "\nDiscounted Price: ","INR", round(int(products[a[i]][j]["price"]) - (int(products[a[i]][j]["discount"]) * int(products[a[i]][j]["price"]))/100, 2))
                    else:
                        pass                    
                    
                else:
                    pass
                    
    def all_discounted_products(self):
        a = ("Toiletries", "Food", "Electronics")
        for i in range(3):
            for j in range(6):
                if products[a[i]][j]["discount"] != "0":
                    print("\nProductID",products[a[i]][j]["id"], "\nName: ",products[a[i]][j]["name"],"\nPrice: ","INR", products[a[i]][j]["price"], "\nDiscount: ", products[a[i]][j]["discount"],"%", "\nDiscounted Price: ","INR", round(int(products[a[i]][j]["price"]) - (int(products[a[i]][j]["discount"]) * int(products[a[i]][j]["price"]))/100, 2))
                else:
                    pass
                
class ShoppingCart:
    def __init__(self):
        pass
    
    def add_item(self):
        global cart
        cart = []
        a = int(input("ID of the product you want to add to your cart: "))
        b = int(input("Quantity: "))
        cart.append([a,b])
    
    def delete_item(self):
        a = int(input("ID of the product you want to delete from your cart: "))
        for i in cart:
            if a == (cart[i])[0]:
                cart.pop(i)
            else:
                pass
            
    def view_cart(self):
        for i in range(len(cart)):
            print("ProductID: ", (cart[i])[0], "Quantity: ", (cart[i])[1] )
            
            
class Bill:
    def __init__(self):
        pass
    
    def calculate_bill(self):
        global sub_total1, sub_total2
        global bill
        sub_total1, sub_total2 = 0,0
        a = ("Toiletries", "Food", "Electronics")
        bill = [("ProductID", "Name", "DiscountedPrice", "Quantity", "TotalDiscountedPrice", "ActualPrice", "TotalActualPrice")]
        for i in range(len(cart)):
            for j in range(3):
                for k in range(6):
                    if (cart[i])[0] == products[a[j]][k]["id"]:
                        
                        actual_price = int(products[a[j]][k]["price"])
                        total_actual_price = actual_price*cart[i][1]
                        
                        discounted_price = round(int(products[a[j]][k]["price"]) - (int(products[a[j]][k]["discount"]) * int(products[a[j]][k]["price"]))/100, 2)
                        total_discounted_price = discounted_price*cart[i][1]
                                                
                        bill.append((cart[i][0], products[a[j]][k]["name"], discounted_price,cart[i][1], total_discounted_price,actual_price, total_actual_price))
                        sub_total1 += total_discounted_price
                        sub_total2 += total_actual_price
                        
    def display_bill(self):
        for i in range(1, len(bill)+1):
            print(i, "\n", "Name: ", (bill[i])[1], "\nPrice: ", (bill[i])[5] , "\nDiscounted Price: ", (bill[i])[2], "\nQuantity: ", (bill[i])[3], "\nTotal: ", (bill[i])[4])
        print("GST: 5%", "\nSub-Total: ", sub_total1 + (sub_total1*(5))/100, "\nYou Saved: ",( sub_total2 + (sub_total2*(5))/100) - (sub_total1 + (sub_total1*(5))/100))
    
    

class AdminPrivileges:
    def __init__(self):
        pass
    
    
    def view_all_products(self):        
        print("Toiletries")
        for i in range(6):
            print("\nProductID",products["Toiletries"][i]["id"], "\nName: ",products["Toiletries"][i]["name"],"\nPrice: ","INR", products["Toiletries"][i]["price"])
            if products["Toiletries"][i]["discount"] != "0":
                print("Discount: ", products["Toiletries"][i]["discount"],"%", "\nDiscounted Price: ","INR", round(int(products["Toiletries"][i]["price"]) - (int(products["Toiletries"][i]["discount"]) * int(products["Toiletries"][i]["price"]))/100, 2), "Buying_Price: ","INR", products["Toiletries"][i]["buying_price"])
                d = round(int(products["Toiletries"][i]["price"]) - (int(products["Toiletries"][i]["discount"]) * int(products["Toiletries"][i]["price"]))/100, 2)
                b = int(products["Toiletries"][i]["buying_price"])
                profit = d -b
                if profit >0:
                    print("Profit: ",profit )
                else:
                    loss = profit
                    print("No profit :( There was loss..")
                    print("Loss: ",0-loss , "\n")
                    
        
            else:
                pass
        
        print("\nFood")
        for i in range(6):
            print("\nProductID",products["Food"][i]["id"], "\nName: ",products["Food"][i]["name"],"\nPrice: ","INR", products["Food"][i]["price"])
            if products["Food"][i]["discount"] != "0":
                print("Discount: ", products["Food"][i]["discount"],"%", "\nDiscounted Price: ","INR", round(int(products["Food"][i]["price"]) - (int(products["Food"][i]["discount"]) * int(products["Food"][i]["price"]))/100, 2), "Buying_Price: ","INR", products["Food"][i]["buying_price"])
                d = round(int(products["Food"][i]["price"]) - (int(products["Food"][i]["discount"]) * int(products["Food"][i]["price"]))/100, 2)
                b = int(products["Food"][i]["buying_price"])
                profit = d -b
                if profit >0:
                    print("Profit: ",profit )
                else:
                    loss = profit
                    print("No profit :( There was loss..")
                    print( "Loss: ",0-loss, "\n" )
                    
        
            else:
                pass
            
        print("\nElectronics")    
        for i in range(6):
            print("\nProductID",products["Electronics"][i]["id"], "\nName: ",products["Electronics"][i]["name"],"\nPrice: ","INR", products["Electronics"][i]["price"])
            if products["Electronics"][i]["discount"] != "0":
                print("Discount: ", products["Electronics"][i]["discount"],"%", "\nDiscounted Price: ","INR", round(int(products["Electronics"][i]["price"]) - (int(products["Electronics"][i]["discount"]) * int(products["Electronics"][i]["price"]))/100, 2), "Buying_Price: ","INR", products["Electronics"][i]["buying_price"])
                d = round(int(products["Electronics"][i]["price"]) - (int(products["Electronics"][i]["discount"]) * int(products["Electronics"][i]["price"]))/100, 2)
                b = int(products["Electronics"][i]["buying_price"])
                profit = d -b
                if profit >0:
                    print("Profit: ",profit )
                else:
                    loss = profit
                    print("No profit :( There was loss..")
                    print("Loss: ",0-loss, "\n" )
                    
        
            else:
                pass
            
            
class User:
    def __init__(self):
        pass
          
    def category(self,category):        
        if category == "customer".lower():
            a = input("Are you a student? Enter y/n: ")
            if a.lower() == "y":
                b = int(input("Select a transaction option\n 1. SWD\n 2. UPI\n 3.Cash\n"))
                if b == 1:
                    user = User()
                    user.student()
                elif b == 2:
                    users = User()
                    users.main_student()
                elif b == 3:
                    users = User()
                    users.main_student()
            elif a.lower() == "n":
                b = int(input("Select a transaction option\n 1.UPI\n 2.Cash\n"))
                if b == 1 or b == 2:
                    users = User()
                    users.main_student()
                else: 
                    print("Invalid input. Please try again :( ")
                    users = User()
                    users.category(category)
                    
        elif category == "admin".lower():
            user = User()
            user.admin()
        
    def student(self):
        print("Login here\n")
        id_number = input("ID Number: ")
        name = input("Name: ")
        room_number = input("Room Number: ")
        user_details = (id_number, name, room_number)
        print("Welcome,", user_details[1])
        users = User()
        users.main_student()
        
        
    def admin(self):
        global n
        print("Login here\n")
        username = input("Username: ")
        password = getpass.getpass(("Password: "))
        user_details = (username, password)
        print("Welcome,", user_details[0],)
        users = User()
        users.main_admin()
        
    def main_admin(self):
        n = int(input("Select functionality:\n 1. View Products\n 2. Log out\n 3. Exit Akshay Stores\n"))
        if n == 1:
            adminuser = AdminPrivileges()
            adminuser.view_all_products()
            users = User()
            users.main_admin()
        elif n == 2:
            main()
        elif n == 3:
            print("Thank you for visiting. See you soon :) ")
            sys.exit()
            
    def main_student(self):
        n = int(input("Select functionality:\n 1. View all products\n 2. View products of one category\n 3. Search products\n 4. View all discounts\n 5. Add item to cart\n 6. Delete item from cart\n 7. View cart\n 8. Show bill\n 9. Log out\n 10. Exit Akshay Stores\n "))
        if n == 1:
            viewview = ViewProducts()
            viewview.all_products()
            users = User()
            users.main_student()
        elif n == 2:
            t = int(input("Choose category:\n 1. Toiletries\n 2. Food\n 3. Electronics\n"))
            if t == 1:
                types = "Toiletries"
            elif t == 2:
                types = "Food"
            elif t == 3:
                types = "Electronics"
            else:
                print("Invalid input :(")
                users = User()
                users.main_student()         
                
            viewview = ViewProducts()
            viewview.one_type(types)
            users = User()
            users.main_student()
        elif n == 3:
            search = input("Search: ")
            viewview = ViewProducts()
            viewview.searched_product(search)
            users = User()
            users.main_student()
        elif n == 4:
            viewview = ViewProducts()
            viewview.all_discounted_products()
            users = User()
            users.main_student()
        elif n == 5:
                d = "y" 
                while d == "y".lower():
                    user_cart = ShoppingCart()
                    user_cart.add_item()
                    d = input("Do you wish to add more items? Type y/n: ")
                users = User()
                users.main_student()
        elif n == 6:
                d = "y" 
                while d == "y".lower():
                    user_cart = ShoppingCart()
                    user_cart.delete_item()
                    d = input("Do you wish to delete more items? Type y/n: ")
                users = User()
                users.main_student()
        elif n == 7:
            user_cart = ShoppingCart()
            user_cart.view_cart()
            users = User()
            users.main_student()
        elif n == 8:
            view_bill = Bill()
            view_bill.calculate_bill()
            view_bill.display_bill()
            users = User()
            users.main_student()
        elif n == 9:
            main()
        elif n ==10:
            print("Thank you for visiting. See you soon :) ")
            sys.exit()
        else:
            print("Invalid input. Please try again :( ")
            users = User()
            users.main_student()
            
            
def main():
    global category
    print("Welcome to Akshay Stores!")
    category = input("Admin or customer? ")
    user = User()
    user.category(category)
    

if __name__ == "__main__":
    main()
