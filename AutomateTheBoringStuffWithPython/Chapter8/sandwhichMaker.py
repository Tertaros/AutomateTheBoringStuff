import pyinputplus as pyip


priceList = {"Wheat":1.0,"White":1.0,"Sourdough":1.2,
            "Chicken":1.0,"Turkey":1.0,"Ham":0.8,"Tofu":1.1,
            "Cheddar":0.3,"Swiss":0.35,"Mozzarella":0.4,
            "mayo":0.1, "mustard":0.1, "lettuce":0.1, "tomato":0.2}
def calculatePrice(bread, protein,cheese,mayo,mustard,lettuce,tomato):
    sandwhichprice = 0.0
    sandwhichprice += priceList[bread]
    sandwhichprice += priceList[protein]
    if(cheeseType != "No cheese"):
        sandwhichprice += priceList[cheese]
    if(mayo == "yes"):
        sandwhichprice += priceList["mayo"]
    if(mustard == "yes"):
        sandwhichprice += priceList["mustard"]
    if(lettuce == "yes"):
        sandwhichprice += priceList["lettuce"]
    if(tomato == "yes"):
        sandwhichprice += priceList["tomato"]
    return sandwhichprice

while True:
    totalprice = 0.0
    numberOfSandwhiches = pyip.inputInt(min=1, prompt="How many sandwhiches do you want? \n")
    for sandwhich in range(numberOfSandwhiches):

        bread = pyip.inputMenu(["Wheat", "White", "Sourdough"],prompt="Choose your bread type: \n")
        protein = pyip.inputMenu(["Chicken", "Turkey", "Ham", "Tofu"], prompt="Choose your protein type: \n")
        cheese = pyip.inputYesNo(prompt="Do you want cheese? \n")
        cheeseType = "No cheese"
        if cheese == "yes":
            cheeseType = pyip.inputMenu(["Cheddar", "Swiss", "Mozzarella"], prompt="Choose your cheese sort: \n")
        mayo = pyip.inputYesNo(prompt="Do you want mayo?\n")
        mustard = pyip.inputYesNo(prompt="Do you want mustard?\n")
        lettuce = pyip.inputYesNo(prompt="Do you want lettuce?\n")
        tomato = pyip.inputYesNo(prompt="Do you want tomato?\n")
        totalprice += calculatePrice(bread,protein,cheeseType,mayo,mustard,lettuce,tomato)
    print("The total price of your order is: " + str(totalprice))
