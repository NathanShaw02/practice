### TODO:
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28

### TODO: Declare the Pants Class 
### TODO: write an __init__ function to initialize the attributes
class Pants():
    def __init__(self,color,waist_size,length,price):
        """Method for initializing a Pants object

        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
    """
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price


    def change_price(self,new_price):
        self.price = new_price

    def discount(self,discount_percentage):
        return self.price*(1-discount_percentage)
    
def check_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12

    pants.change_price(10)
    assert pants.price == 10 

    assert pants.discount(.1) == 9

    print('You made it to the end of the check. Nice job!')

check_results()