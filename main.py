class Bill:
    """
    Object that contains data about bill, 
    such as total amount and period of the bill
    """
    
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period
        
class Flatmate:
    """
    Create a flatmate person who lives in the flat 
    and pays the share of the bill.
    """
    
    def __init__(self,name,days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def pays(self,bill):
        pass
    
class PDFReport:
    """
    Create a PDF files that ceraetes data about the
    flatmates such as their names, 
    their due amounts and the period of the bill
    """
    
    def __init__(self,filename):
        self.filename = filename
        
    
    def generate(self,flatmate1,flatmate2,bill):
        pass