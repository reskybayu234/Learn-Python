# Lists are used to store multiple items in a single variable

variables = ["resky","bayu","andhika"]
print("data = ",variables)

# Access List Items
# List items are indexed and you can access them by referring to the index number

accessList = ["resky","bayu","andhika","a","b"]
print(accessList[-2])
print(accessList[0:2])

# Changes List Items
changeList = ["resky","bayu","andhika","a","b"]
changeList[1] = "gura"
print("change = ",changeList)

# Add List Items
# to add an item to the end of the list, use the append() method
addList = ["resky","bayu","andhika","a","b"]
addList.append("mera")
print("add = ",addList)

insertList = ["resky"]
insertList.insert(1,"bayu")
print("insert =",insertList)

extendList = ["resky"]
extendList2 = ["bayu"]
extendList.extend(extendList2)
print("extend = ", extendList)

# Remove Specified Index
removeList = ["resky","bayu","andhika"]
removeList.pop(1)
print("remove = ",removeList)

# Loop Lists
loopList = ["resky","bayu","andhika"]
for x in loopList:
    print("x = ",x)

loopIndex = ["resky","bayu","andhika"]
for i in range(len(loopIndex)):
    print("loopIndex = ",loopIndex[i])

whileLoop = ["resky","bayu","andhika"]
i = 0
while i < len(whileLoop):
    print(whileLoop[i])
    i = i + 1

# List Comprehension
nama = ["resky","bayu","andhika"]
newList = []

for x in nama:
    if "z" in x:
        newList.append(x)
        print("newList = ",type(newList)) 
        