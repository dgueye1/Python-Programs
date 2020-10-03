class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return self.name + ' menu available from ' + str(self.start_time) + ' to ' + str(self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for bill in purchased_items:
      if bill in self.items:
        total += self.items[bill]
    return total

class Franchise:

  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return 'This Restaurant is located at: ' + self.address 

  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

class Business:

  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

brunch = {
  'pancakes': 7.50, 'waffles': 9.00,
  'burger': 11.00, 'home fries': 4.50,'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu('Brunch', brunch, 1100, 1600)

early_bird = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early-Bird', early_bird, 1500, 1800)

dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner, 1700, 2300)

kids = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids', kids, 1100, 2100)

print(brunch_menu)
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

basta = Business("Basta Fazoolin' with my heart", [flagship_store, new_installment])
print(flagship_store)
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_m = ('Arepas', arepas_menu, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_m])
arepa = Business("Take a' Arepa", [arepas_place])

print(arepa)
