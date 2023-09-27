class Ingredient:  # defining the class
    def __init__ (self, ammount_local, metric_unit_local, name_local):
        self.ammount = ammount_local
        self.metric_unit = metric_unit_local
        self.name = name_local

    @staticmethod # factory method
    def from_str_to_ingredient (str_local):
        list_local = str_local.split(' ') # turn str to list
        ammount = float(list_local[0])  # use indeces to match each list element to its according object property
        metric_unit = list_local[1]
        name = list_local[2]
        object = Ingredient (ammount, metric_unit, name)
        return object
    
    def print_object (self):
        print(f"Ingredient with ammount: {self.ammount}, metric unit: {self.metric_unit} & name: {self.name}")

# egg = Ingredients(2, "unit(s)", "egg(s)") # defining an object of the class

# print(egg.ammount)
# print(egg.metric_unit)
# print(egg.name)
