class Ingredient:  # defining the class
    def __init__ (self, amount_local, metric_unit_local, name_local):
        self.amount = amount_local
        self.metric_unit = metric_unit_local
        self.name = name_local

    @staticmethod # factory method = method that creates an object
    def from_str_to_ingredient (str_local):
        list_local = str_local.split(' ') # turn 1 str to list
        amount = float(list_local[0])  # use indeces to match each list element to its according object property
        metric_unit = list_local[1]
        name = list_local[2]
        return Ingredient (amount, metric_unit, name)
    
    # getter = method that gives info about the object
    def as_list (self):
        return [self.amount, self.metric_unit, self.name]

    def print_object (self):
        print(f"Ingredient with amount: {self.amount}, metric unit: {self.metric_unit} & name: {self.name}")