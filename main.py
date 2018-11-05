from inventory import Inventory

if __name__ == '__main__':
    username = input("Hello welcome to Productland! What is your name? ")
    inventory = Inventory()
    cont = True
    while cont:
        cmd = input('\nHello, ' + username + '\nHow may I help you?\n[C]reate new product\n[R]ead your product list / See Sum\n[U]pdate a product\n[D]elete a product\n[Q]uit\n>>>')
        if cmd.lower() not in ['c', 'r', 'u', 'd','q']:
            print('!! Unknown command {} !!'.format(cmd))
        else:
            if cmd.lower() == 'q':
                cont = False
            elif cmd.lower() == 'd':
                pid = input("Please enter product id you want to delete: ")
                inventory.delete_product(pid)
            elif cmd.lower() == 'c':
                name, price, quantity, _id = "", "", "", ""
                inventory.define_product()
                print("New product is added to inventory with id: {}".format(_id))
            elif cmd.lower() == 'r':
                inventory.list_products()
            elif cmd.lower() == 'u':
                pid = input("Please enter product id you want to update: ")
                inventory.update_product(pid)
        print("\n")
    
