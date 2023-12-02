class Fridge:
    def __init__(self):
        self.contents = []

    def store(self, item):
        self.contents.append(item)

    def take(self, item):
        for i, fridge_item in enumerate(self.contents):
            if fridge_item == item:
                return self.contents.pop(i)
        raise Warning("Item not found in the fridge")

    def find(self, name):
        matching_items = [item for item in self.contents if item[1] == name]
        if matching_items:
            # earliest eating date
            return min(matching_items, key=lambda x: x[0])
        return None

    def take_before(self, date):
        items_to_remove = [item for item in self.contents if item[0] < date]
        for item in items_to_remove:
            self.contents.remove(item)
        return items_to_remove

    def __iter__(self):
        sorted_contents = sorted(self.contents, key=lambda x: x[0])
        return iter(sorted_contents)

    def __len__(self):
        return len(self.contents)
    
if __name__ == "__main__":
    # Creating a fridge
    f = Fridge()

    # Storing items in the fridge
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))

    # Taking out items from the fridge
    try:
        print(f.take((191127, "Butter")))  # This will work
        print(f.take((191207, "Bread")))  # This will raise a Warning
    except Warning as e:
        print(e)

    # Finding an item in the fridge
    print(f.find("Milk"))  # This will return the earliest milk item in the fridge if present

    # Taking out items before a certain date
    print(f.take_before(191200))  # This will return items with eat-by date before 191200

    # Iterating through the fridge contents
    print("Items in the fridge:")
    for item in f:
        print(f"- {item[1]} ({item[0]})")

    # Checking the number of items in the fridge
    print("Number of items in the fridge:", len(f))

