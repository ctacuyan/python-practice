alwest = ["Athletics","Angels","Mariners","Astros","Rangers"]
aleast = ["Orioles", "Yankees", "Red Sox", "Rays", "Blue Jays"]
alcentral = ["Twins", "Indians", "Royals", "White Sox", "Tigers"]
nlwest = ["Padres","Giants","Dodgers","Diamondbacks","Rockies"]
nleast = ["Nationals", "Marlins", "Phillies", "Mets", "Braves"]
nlcentral = ["Cubs", "Brewers", "Pirates", "Reds", "Cardinals"]

print(alwest[0])
print(aleast[-1])
print(nlwest[2:])
print(nlcentral[2:4])
print(nleast.index("Mets"))
alwest[0]="World Series champions!"
print(alwest)

print("\nThese are the years in which the popular vote candidate lost: ")
popular1=[1824,1876,1888,2000,2016]
print(popular1)
popular2=["John Quincy Adams", "Rutherford B Hayes","Benjamin Harrison","George W Bush","Donald Trump"]
print("These were history's winners: ")
print(popular2)
print("Let's rewrite history! The popular vote winner becomes president!")
rewrite = ["Andrew Jackson","Samuel Tilden","Grover Cleveland","Al Gore","Hillary Clinton"]
position = [0,1,2,3,4]
for x,y in zip(position,rewrite):
        popular2[x] = y
print(popular2)
print("\n")

primes = [2,3,5,7,11]
primes2 = [13,17,19,23,29]
primes.extend(primes2)
print(primes)
print("\n")

americancities= ["New York City","Los Angeles","Chicago","Houston","Philadelphia"]
print(americancities)
print("Phoenix has surpasssed Philadelpha in population!")
americancities[4]="Phoenix"
print(americancities)
americancities.remove("New York City")
print(americancities)
print("We removed the east coast cities!")
print(americancities.index("Los Angeles"))

print("\n")
numbers = [1,4,54,6,6,6,6,999]
names = ["Bob","Bob","Bob"]
print(numbers)
print(names)
print(numbers.count(6))
print(names.count("Bob"))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
names2 = names.copy()
print(names2)














