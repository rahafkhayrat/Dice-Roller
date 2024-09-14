import random
 
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
   
dice=[]
total=0


while True:
    try:
        num_of_dice = int(input("How many dice?: "))
        if num_of_dice <= 0:
            print("Please enter a number greater than 0.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")


for die in range (num_of_dice):
      
    dice.append(random.randint(1,6))
    

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()    
    
    
for die in dice :
    total+=die
    

    

print(f"total:{total}")        
