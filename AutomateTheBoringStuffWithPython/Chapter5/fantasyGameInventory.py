
#1st excercise
exampleinventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    total = 0
    print('Inventory:')
    for k,v in inventory.items():
        total += v
        print(str(v)+ ' ' + k)

    print('Total number of items: ' + str(total))

displayInventory(exampleinventory)

#2nd excercise
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item] = inventory[item] + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
