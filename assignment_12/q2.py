class Inventory:
    def __init__(self, name = "DEFAULT", balance = 0, max_weight = 0):
        self.__player_name = name
        self.__balance = balance
        self.__max_weight = max_weight
        self.__items = []

    def collect(self, item):
        if self.__proper_item(item):
            if self.get_inv_weight() + item[2] <= self.__max_weight:
                self.__items.append(item)
            else:
                raise Warning("Exceeds maximum weight, cannot collect item")
            
    def get_inv_weight(self):
        return sum(item[2] for item in self.__items)
    
    def get_player_name(self):
        return self.__player_name
    
    def get_balance(self):
        return self.__balance
    
    def get_inv_value(self):
        return sum(item[1] for item in self.__items)
    
    def drop(self, item):
        if self.__proper_item(item):
            if item in self.__items:
                self.__items.remove(item)
                return item
            else:
                raise Warning("Item not found in inventory")
            
    def sell(self, item):
        if self.__proper_item(item):
            if item in self.__items:
                self.__balance += item[1]
                self.__items.remove(item)
                return item
            else:
                raise Warning("Item not found in inventory")

    def buy(self, item):
        if self.__proper_item(item):
            if self.__balance >= item[1] and self.get_inv_weight() + item[2] <= self.__max_weight:
                self.__balance -= item[1]
                self.__items.append(item)
            else:
                raise Warning("Insufficient balance or exceeds maximum weight, cannot buy item")

    def __proper_item(self, item):
        if not isinstance(item, tuple) or len(item) != 3:
            raise ValueError("Item should be a tuple of form (string, int, int)")
        return True

    def __iter__(self):
        return iter(sorted(self.__content, key=lambda item: item[1], reverse=True))

    def __len__(self):
        return len(self.__items)
