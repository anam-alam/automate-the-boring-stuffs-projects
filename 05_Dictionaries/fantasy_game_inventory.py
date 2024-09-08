

inventory = {
            'rope': 1,
            'torch': 6,
            'gold coin': 42,
            'dagger': 1,
            'arrow': 12
}

def display_inventory(inventory):
    total_items = 0
    print("Inventory: ")
    for k,v in inventory.items():
        print(str(v)+' '+ k)
        total_items += v
    print(f"Total number of items: {total_items}")

def add_to_inventory(inventory,added_items):
    for item in added_items:
        inventory[item] = inventory.get(item,0)+1
    return inventory

print("Original Inventory is: ")
display_inventory(inventory)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inventory,dragon_loot)
print("Updated inventory is: ")
display_inventory(inv) 
