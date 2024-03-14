#1.WORKING ON LIST
#Initialize an empty list called num
num=[]

#Allow user to enter the number of elements in the list
element=int(input("Enter the number of elements in the list: "))

#Allow user to enter the elements in the list
for i in range(element):
    numbers=int(input(f"Element {i+1}: "))
    num.append(numbers)
print(f"The list is: {num}")

#Compute the sum of elements in the list
total= sum(num)
print(f"The sum of the elements in the list is: {total}")
print()


#2.WORKING ON TUPLES
#Create a tuple of five favourite books
favbooks=("Atomic Habits","Lord of the ring","Here where the sun beams are green","Bake like the best","Good Vibes,Good Life")

#Using for loop to print the books on separate line
print(f"My favourites books are:")
for i in favbooks:
    print(f'{i}')
print()


#3.WORKING ON DICTIONARIES
#Initialize an empty dictionary
personalInfo={}

#Allow user to enter elements in a dictionary
name=input("Enter your name: ")
age=int(input("Enter your age: "))
favColor=input("Enter your favourite color: ")

#Storing the information to the dictionary
personalInfo['name']=name
personalInfo['age']=age
personalInfo['favColor']=favColor

#Print values in the dictionary
print(f'{personalInfo}')
print()


#4.WORKING ON SETS
#Initialize an empty set
setA=set()
setB=set()

#Allow user to enter elements in both sets
for i in range(5):
    element=int(input("Enter elements of setA: "))
    setA.add(element)
print(f'setA: {setA}')
for i in range(5):
    element=int(input("Enter elements of setB: "))
    setB.add(element)
print(f'setB: {setB}')

#Create a new set with elements common to setA and setB
setC = setA & setB
print(f'Elements that are common to both sets are: {setC}')
print()


#5.WORKING ON LIST COMPREHENSION
#Create a list of five words
listwords=['Hello','Fantastic','Python','Number','Bye']

#Using list comprehension to create a new list with words having odd number of characters
oddCharacters =[word for word in listwords if len(word)%2!=0]
print(f'Lists of words with odd number of characters: {oddCharacters}')
