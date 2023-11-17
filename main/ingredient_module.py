class Ingredient:
    def __init__ (self, amount_local, metric_unit_local, name_local):
        self.amount = amount_local
        self.metric_unit = metric_unit_local
        self.name = name_local

    @staticmethod # factory method = method that creates an object
    def from_str_to_ingredient (str_local):
        list_local = str_local.split(', ')
        name = list_local[0]
        rest = list_local[1].split(' ')
        amount = round(float(rest[0]),2)
        metric_unit = rest[1]
        return Ingredient (amount, metric_unit, name)
    
    # getter = method that gives info (i.e. attributes) about the object
    def as_list (self):
        return [self.amount, self.metric_unit, self.name]

    def as_str (self):
        return f'{self.name}, {self.amount} {self.metric_unit}'

    def print_object (self):
        print(f"{self.name}, {self.amount} {self.metric_unit}")