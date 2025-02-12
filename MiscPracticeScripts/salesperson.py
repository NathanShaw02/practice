### TODO:
#   Code a SalesPerson class with the following attributes
#   - first_name (string), the first name of the salesperson
#   - last_name (string), the last name of the salesperson
#   - employee_id (int), the employee ID number like 5681923
#   - salary (float), the monthly salary of the employee
#   - pants_sold (list of Pants objects), 
#            pants that the salesperson has sold 
#   - total_sales (float), sum of sales of pants sold

### TODO: Declare the SalesPerson Class 

### TODO: write an __init__ function to initialize the attributes
###    Input Args for the __init__ function:
#        first_name (str)
#        last_name (str)
#        employee_id (int)
# .      salary (float)
#
# You can initialize pants_sold as an empty list
# You can initialize total_sales to zero.
#
###

from pants import Pants
class SalesPerson():
    def __init__(self,first_name,last_name,employee_id,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

### TODO: write a sell_pants method:
#
#    This method receives a Pants object and appends
#    the object to the pants_sold attribute list
#
#    Args:
#        pants (Pants object): a pants object
#    Returns:
#        None

    def sell_pants(self, pants_object):
        self.pants_sold.append(pants_object)

### TODO: write a display_sales method:
#    
#    This method has no input or outputs. When this method 
#    is called, the code iterates through the pants_sold list
#    and prints out the characteristics of each pair of pants
#    line by line. The print out should look something like this
#
#   color: blue, waist_size: 34, length: 34, price: 10
#   color: red, waist_size: 36, length: 30, price: 14.15
#
#
#
###
    def display_sales(self):
        for i in self.pants_sold:
            print("color: "+i.color+", waist_size: "+i.waist_color+", length: "+i.length+", price: "+i.price)

### TODO: write a calculate_sales method:
#      This method calculates the total sales for the sales person.
#      The method should iterate through the pants_sold attribute list
#      and sum the prices of the pants sold. The sum should be stored
#      in the total_sales attribute and then return the total.
#      
#      Args:
#        None
#      Returns:
#        float: total sales
#
###  
    def calculate_sales(self):
        totalSum = 0
        for i in self.pants_sold:
            totalSum+=i.price
        self.total_sales = totalSum
        return self.total_sales

### TODO: write a calculate_commission method:
#
#   The salesperson receives a commission based on the total
#   sales of pants. The method receives a percentage, and then
#   calculate the total sales of pants based on the price,
#   and then returns the commission as (percentage * total sales)
#
#    Args:
#        percentage (float): comission percentage as a decimal
#
#    Returns:
#        float: total commission
#
#
###
    def calculate_commission(self, percentage):
        self.calculate_sales()
        total_commission = self.total_sales*percentage
        return total_commission

def check_results():
    pants_one = Pants('red', 35, 36, 15.12)
    pants_two = Pants('blue', 40, 38, 24.12)
    pants_three = Pants('tan', 28, 30, 8.12)
    
    salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
    
    assert salesperson.first_name == 'Amy'
    assert salesperson.last_name == 'Gonzalez'
    assert salesperson.employee_id == 2581923
    assert salesperson.salary == 40000
    assert salesperson.pants_sold == []
    assert salesperson.total_sales == 0
    
    salesperson.sell_pants(pants_one)
    salesperson.pants_sold[0] == pants_one.color
    
    salesperson.sell_pants(pants_two)
    salesperson.sell_pants(pants_three)
    
    assert len(salesperson.pants_sold) == 3
    assert round(salesperson.calculate_sales(),2) == 47.36
    assert round(salesperson.calculate_commission(.1),2) == 4.74
    
    print('Great job, you made it to the end of the code checks!')
    
check_results()