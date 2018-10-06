inventory ={
        'gold':500,
        'pouch':['flin','twine','gemstone'],
        'backpack':['xylophone','dagger','bedroll','bread loaf'],
}
# part 1
inventory['pocket']=[]
print(inventory)
#part 2
inventory['pocket']=['seashell','strange','berry','lint']
print("\n")
print(inventory)
# part 3
del inventory['backpack'][1]
print(inventory)
#part 4
inventory['gold']=50
print(inventory)