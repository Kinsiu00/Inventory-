# Inventory Project

Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track 
of various products and can sum up the inventory value.

![inv](https://user-images.githubusercontent.com/11141681/48005646-f0fa5080-e0e1-11e8-852a-dcc35b5b4e8e.png)

## Project Description

Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track 
of various products and can sum up the inventory value.

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

There are no additional installation of packages or libraries required for this project. However, Python 3 must be installed in order to run this program.

### Instructions 

The folder contains three program files which are `inventory.py`, `product.py`, and `main.py` . In order for us to begin running our program we use run the following command `python3 main.py`. By running this file we are importing from our other two remaining classes and this helps to establish a seemless connection between each of them.

For example in order to import our classes we use:
```
from product import Product
```

## List of Methods Used

We use the `input` method in our program so that you can use this to read data from the user in this case the input we used to [C] Create, [R] Read, [U] Update, [D] Delete, & [Q] Quit:

```
cmd = input('\nHello, ' + username + '\nHow may I help you?\n[C]reate new product\n[R]ead your product list / See Sum\n[U]pdate a product\n[D]elete a product\n[Q]uit\n>>>')
```
## References

* [StackOverflow](https://stackoverflow.com/questions/50771281/trying-to-set-up-a-simple-inventory-management-program) - Stack Overflow is a question and answer site for professional and enthusiast programmers. It is primarily used as a forum to help address questions and provide a collaborated community to answer programming/code related issues. 



