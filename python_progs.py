#type casting
# 3 types of it
# implicit conversion
# explicit conversion

# leap year or not
'''year=int(input('enter year'))
if year%4!=0:
    print('not a leap year')
elif year%100==0 and year%400!=0:
    print('not a leap year')
else:
    print('it\'s a leap year')'''

#display 1 to 1000 which are divisible by 3 and 5
'''print('for loop')
for i in range(1,1001):
    if i%3==0 or i%5==0:
        print(i)
print('while loop')
i=0
while(i<1001):
    if i%3==0 or i%5==0:
        print(i)
    i+=1'''

# sum of odd numbers
'''i,sum=0,0
while(i<100):
    if i%2!=0:
        sum+=i
    i+=1
print('sum of odd numbers is ',sum)'''

#display 1 to 1000 which are divisible by 3 and 5 and append to list
'''l=[]
for i in range(1,1001):
    if i%3==0 or i%5==0:
        l.append(i)
print(l)'''

# print all keywords
'''import keyword
print(keyword.kwlist)'''

#sum all elements in list
'''l=eval(input('enter a list'))
print(sum(l))'''

# pattern
'''a,b=6,4
for i in range(0,a+1):
    print(i,end=" ")
print()
for j in range(0,a+1):
    b=a
    a+=1
    b+=1
    print(a,'-',b)'''

# pattern 2
'''v1,v2=5,10
for x in range(1,4):
    v1+=1
    v2-=1
    print(v1,v2)
    print(v2-1,v1+1)'''

# vowel prog
'''s=input()
l=s.split()
print(l)
count=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in l:
    if i[0] in vowels:
        count+=1
        print(i)
print('number of words starting with vowels are ',count)'''

#importing 
'''import math
print(math.exp(2))

from math import exp
print(exp(2))

from math import sin
pi=math.pi
print(sin(pi/6))

print(max(3,4))
print(min(55,83))
print(abs(-60))
print(divmod(27,8))'''

#import from other file
'''from import_file import area_c
radius=int(input('enter radius '))
print(area_c(radius))'''

#rock paper scissor
'''import random
computer=['rock','paper','scissor']
count=0
for i in range(5):
    c_choice=random.choice(computer)
    h_choice=input('enter rock or paper or scissor ')
    if h_choice not in computer:
        print('enter right choice')
    else:
        if h_choice=='rock' and c_choice=='paper':
            print('you lose')
            count-=1
        elif h_choice=='rock' and c_choice=='scissor':
            print('you win')
            count+=1
        elif h_choice=='paper' and c_choice=='scissor':
            print('you lose')
            count-=1
        elif h_choice=='paper' and c_choice=='rock':
            print('you win')
            count+=1
        elif h_choice=='scissor' and c_choice=='paper':
            print('you win')
            count+=1
        elif h_choice=='scissor' and c_choice=='rock':
            print('you lose')
            count-=1
        else:
            print('its a draw')
    print('computer has choosen ',c_choice)
if count>=1:
    print('yay you\'ve won overall')
elif count==0:
    print('it\'s a draw overall')
else:
    print('you\'ve lost overall')
'''


#check prime
'''num=int(input('enter number'))
c=0
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        print('number is not a prime')
        c+=1
        break
if c==0 and num!=2:
    print('number is prime')
else:
    print('number is not a prime')'''

#factorial
'''from math import factorial
print(factorial(5))
num=int(input('enter num'))
f=1
for i in range(1,num+1):
    f=f*i
print(f)'''

#calculate pi
'''def calc_pi(num_terms):
    pi=0
    for i in range(num_terms):
        pi+=((-1)**i)/(2*i+1)
    pi*=4
    return pi
print(calc_pi(10000))'''

#flip a coin
'''import random
coin=random.randint(0,2)
if coin==0:
    print('its a head')
else:
    print('its a tail')'''

#replace space with -
'''a=input('enter string ')
b=a.replace(' ','-')
print(b)'''

#variable arguments
'''def func(*args):
    print(args[0]+args[1])
    print(type(args))
func('one','two')'''

#string functions
'''b=input('enter the sentence ')
print('enter 1 to turn into lower letter\nenter 2 to turn to upper\nenter 3 to find length\nenter 4 to capitalize\nenter 5 to print in title format\nenter 6 to replace\nenter 7 to count a substring\nenter 8 to check startswith\nenter 9 to check endswith\nenter 10 to find a letter')
a=int(input('enter a number between 1 to 10 '))
if a==1:
    print(b.lower())
elif a==2:
    print(b.upper())
elif a==3:
    print(len(b))
elif a==4:
    print(b.capitalize())
elif a==5:
    print(b.title())
elif a==6:
    print(b.replace(' ','.'))
elif a==7:
    print(b.count('i'))
elif(a==8):
    print(b.startswith('a'))
elif(a==9):
    print(b.endswith('h'))
elif(a==10):
    print(b.find('is'))'''

#list functions

'''l=['a','ba',[0,1]]
print(len(l))
l[2][1]='a'
print(l[-2][-1])'''

#sample list
'''def fun1(l):
    l.append(333)
    print(l)
def fun2(l):
    print(len(l))
def fun3(l):
    l.insert(5,80)
    print(l)
def fun4(l):
    l.remove(3)
    print(l)
def fun5(l):
    l.extend([1,1,1,1])
    print(l)
def fun6(l):
    l.pop(2)
    print(l)
l=eval(input('enter the list '))
l=list(l)
print('enter 1 to append\nenter 2 to remove\nenter 3 to find length\nenter 4 to insert\nenter 5 to extend\nenter 6 to pop\n')
print('enter 3 zeros to break out')
a=int(input('enter a number between 1 to 6 '))
while a!=000:
    if a==1:
        fun1(l)
    elif a==2:
        fun4(l)
    elif a==3:
        fun2(l)
    elif a==4:
        fun3(l)
    elif a==5:
        fun5(l)
    elif a==6:
        fun6(l)
    print('enter 1 to append\nenter 2 to replace\nenter 3 to find length\nenter 4 to insert\nenter 5 to extend\nenter 6 to pop\n')
    print('enter space to break out')
    a=int(input('enter a number between 1 to 10 '))'''

#tic tac toe
'''import random
l=[[[' '],[' '],[' ']],[[' '],[' '],[' ']],[[' '],[' '],[' ']]]
def in_range(s):
    if -1<int(s[0])<3 or -1<int(s[1])<3:
        return True
def print_toe(l):
    for i in range(3):
        for j in range(2):
            print('',l[i][j][0],'|',end=" ")
        print('',l[i][2][0],end=" ")
        if i!=2:
            print('\n-------------')
moves=0
def consecutive(l,player):
    if ((int(player[0])!=2 and int(player[1])!=2) and l[int(player[0])+1][int(player[1])+1]==['*'] and (int(player[0])==int(player[1]) or int(player[0])+1==int(player[1])+1)):
        return (player,str(int(player[0])+1)+str(int(player[1])+1),'cross-right-down',str(int(player[0])-1)+str(int(player[1])-1),str(int(player[0])+2)+str(int(player[1])+2))
    elif ((int(player[0])!=0 and int(player[1])!=0) and l[int(player[0])-1][int(player[1])-1]==['*'] and (int(player[0])==int(player[1]) or int(player[0])-1==int(player[1])-1)):
        return (player,str(int(player[0])-1)+str(int(player[1])-1),'cross-left-up',str(int(player[0])-2)+str(int(player[1])-2),str(int(player[0])+1)+str(int(player[1])+1))
    elif ((int(player[0])!=0 and int(player[1])!=2) and l[int(player[0])-1][int(player[1])+1]==['*'] and (int(player[0])==int(player[1]) or int(player[0])-1==int(player[1])+1)):
        return (player,str(int(player[0])-1)+str(int(player[1])+1),'cross-right-up',str(int(player[0])+1)+str(int(player[1])-1),str(int(player[0])-2)+str(int(player[1])+2))
    elif ((int(player[0])!=2 and int(player[1])!=0) and l[int(player[0])+1][int(player[1])-1]==['*'] and (int(player[0])==int(player[1]) or int(player[0])+1==int(player[1])-1)):
        return (player,str(int(player[0])+1)+str(int(player[1])-1),'cross-left-down',str(int(player[0])-1)+str(int(player[1])+1),str(int(player[0])+2)+str(int(player[1])-2))
    elif (int(player[0])!=2 and l[int(player[0])+1][int(player[1])]==['*']):
        return (player,str(int(player[0])+1)+str(int(player[1])),'down',str(int(player[0])+2)+str(int(player[1])),str(int(player[0])-1)+str(int(player[1])))
    elif (int(player[0])!=0 and l[int(player[0])-1][int(player[1])]==['*']):
        return (player,str(int(player[0])-1)+str(int(player[1])),'up',str(int(player[0])-2)+str(int(player[1])),str(int(player[0])+1)+str(int(player[1])))
    elif (int(player[1])!=2 and l[int(player[0])][int(player[1])+1]==['*']):
        return (player,str(int(player[0]))+str(int(player[1])+1),'right',str(int(player[0]))+str(int(player[1])-1),str(int(player[0]))+str(int(player[1])+2))
    elif (int(player[1])!=0 and l[int(player[0])][int(player[1])-1]==['*']):
        return (player,str(int(player[0]))+str(int(player[1])-1),'left',str(int(player[0])-2)+str(int(player[1])+1),str(int(player[0]))+str(int(player[1])-2))
    else:
        return False
#def computer_move(l,computer):
def is_valid(a):
    if '-' not in a[0] and '3' not in a[0]:
        return a[0]
    if '-' not in a[1] and '3' not in a[1]:
        return a[1]
    return False
while moves<9:
    print_toe(l)
    player=input('\nenter matrix coordinates ')
    l[int(player[0])][int(player[1])]=['*']
    if consecutive(l,player):
        a=consecutive(l,player)
        print(a[3:])
        computer=is_valid(a[3:])
        l[int(computer[0])][int(computer[1])]=['o']
        
    else:
        print('no')
        flag,i,j=False,0,0
        while i<3 and flag==False:
            while j<3 and flag==False:
                if l[i][j]==[' ']:
                    l[i][j]=['o']
                    flag=True
                j+=1
            i+=1
            

    print()       
    #print(in_range('-1-1'))
    moves+=1'''

#swap element
'''l=eval(input('enter list'))
l=list(l)
for i in range(1,len(l)):
    if l[i]%7==0:
        l[i],l[i-1]=l[i-1],l[i]
if l[0]%7==0:
    l[0],l[len(l)-1]=l[len(l)-1],l[0]
print(l)'''

#sample
'''b=()
for i in range(2):
    employee_id=input('enter employee id ')
    employee_name=input('enter employee name ')
    employee_salary=input('enter employee employee_salary ')
    date_of_joining=input('enter employee joining date ')
    a=(employee_id,employee_name,employee_salary,date_of_joining)
    b=(b,a)
print(b)'''

'''employee_data = (

   ("E101", "John Smith", 50000.0, "2022-01-15"),

   ("E102", "Jane Doe", 55000.0, "2021-11-20"),

   ("E103", "Michael Johnson", 60000.0, "2022-03-10"),

   ("E104", "Emily Williams", 52000.0, "2022-02-05"),

   ("E105", "William Brown", 58000.0, "2021-09-30")

)

def display_emp_id(empid):
    found=False
    for employee in employee_data:
        if employee[0]==empid:
            print("empname",employee[1])
            print("salary",employee[2])
            found=True
            break
    if not found:
        print("employee with empid not found")

while True:
    print("\n employee management system")
    print('display by emp id')
    print('exit')'''

#add 200 pages to list of chap1 and 400 pages to list of chap 2
'''domains=['google','www.unix','oracle.com']
for i in domains:
    if i[0:3]!='www.':
        i='www'+i
    if i[-1:-4:-1]!='com':
        i=i+'.com'
print(domains)'''


#sample
'''web1={'a','b','c','d'}
web2={'d','e','f','g','a','b'}
print(web1.intersection(web2))
print(web1.union(web2))
print(web1.difference(web2))'''

#word scramble
'''import random
movies = [
    "inception",
    "the shawshank redemption",
    "pulp fiction",
    "the dark knight",
    "forrest gump",
    "the godfather",
    "interstellar",]
r=random.choice(movies)
l=[]
for i in range(len(r)):
    l.append(r[i])
random.shuffle(l)
s=''
for j in range(len(l)):
    s+=l[j]
print('the random shuffled sequence is ',s,'find the correct sequence')
print()
human=input('enter the sequence ')
if human==r:
    print('yay! you\'ve got it right')
else:
    print('try again')'''

#ceaser cipher
'''alpha='abcdefghijklmnopqrstuvwxyz'
Alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
shift=int(input('enter the places have to be shifted '))
print(list(alpha))
sentence=input('enter sentence to encode ')
result=""
for i in sentence:
    if i.isupper():
        result+=chr(ord('A')+((ord(i)+shift-ord('A'))%26))
    else:
        result+=chr(ord('a')+((ord(i)+shift-ord('a'))%26))
print(result)
result1=""
for j in result:
    if i.isupper():
        result1+=chr(ord('A')+((ord(j)-shift-ord('A'))%26))
    else:
        result1+=chr(ord('a')+((ord(j)-shift-ord('a'))%26))
print(result1)'''

#dictionary
'''d={1:'cat',2:'dog'}
print(d.keys())
print(d.items())
print(d.values())'''

#dict functions
'''def clear_dictionary(dictionary):
    dictionary.clear()
    print("Dictionary cleared!")
def copy_dictionary(dictionary):
    new_dict = dictionary.copy()
    print("Dictionary copied successfully:", new_dict)
def create_from_keys():
    keys = input("Enter keys (comma-separated): ").split(',')
    value = input("Enter default value: ")
    dictionary = dict.fromkeys(keys, value)
    print("New dictionary created:", dictionary)
def get_value(dictionary):
    key = input("Enter key: ")
    value = dictionary.get(key, "Key not found")
    print("Value:", value)
def show_items(dictionary):
    print("Items in the dictionary:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")
def show_keys(dictionary):
    print("Keys in the dictionary:", list(dictionary.keys()))
def pop_item(dictionary):
    key = input("Enter key to remove: ")
    value = dictionary.pop(key, "Key not found")
    print(f"Item removed: {key}: {value}")
def pop_last_item(dictionary):
    if dictionary:
        key, value = dictionary.popitem()
        print(f"Last item removed: {key}: {value}")
    else:
        print("Dictionary is empty.")
def set_default(dictionary):
    key = input("Enter key: ")
    value = input("Enter default value: ")
    dictionary.setdefault(key, value)
    print("Value set")
def update_dictionary(dictionary):
    update_dict = eval(input("Enter the dictionary to update (in the form of a Python dictionary): "))
    dictionary.update(update_dict)
    print("Dictionary updated")
if __name__ == "__main__":
    my_dictionary = {}
    while True:
        print("\nDictionary Functions Menu:")
        print("1. Clear Dictionary")
        print("2. Copy Dictionary")
        print("3. Create Dictionary from Keys")
        print("4. Get Value by Key")
        print("5. Show Items")
        print("6. Show Keys")
        print("7. Pop Item by Key")
        print("8. Pop Last Item")
        print("9. Set Default Value")
        print("10. Update Dictionary")
        print("11. Exit")
        choice = int(input("Enter your choice (1-11): "))
        if choice == 1:
            clear_dictionary(my_dictionary)
        elif choice == 2:
            copy_dictionary(my_dictionary)
        elif choice == 3:
            create_from_keys()
        elif choice == 4:
            get_value(my_dictionary)
        elif choice == 5:
            show_items(my_dictionary)
        elif choice == 6:
            show_keys(my_dictionary)
        elif choice == 7:
            pop_item(my_dictionary)
        elif choice == 8:
            pop_last_item(my_dictionary)
        elif choice == 9:
            set_default(my_dictionary)
        elif choice == 10:
            update_dictionary(my_dictionary)
        elif choice == 11:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option (1-11).")'''

#sample
'''dict = {
    'name': 'John Doe',
    'age': 25,
    'email': 'john.doe@example.com',
    'phone_numbers': {
        'home': '123-456-7890',
        'work': '987-654-3210',
        'mobile': '555-555-5555'
    },
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip': '12345'
    }}
dic=eval(input('enter name and phone '))
dict.update(dic)
print(dict)'''

'''questionbank={
    "quiz":{
        "sport":{
            "q1":{
                "question":"WhichoneiscorrectteamnameinNBA?",
                "options":[
                    "NewYorkBulls",
                    "LosAngelesKings",
                    "GoldenStateWarriros",
                    "HustonRocket"
                ],
                "answer":"HustonRocket"
            }
        },
        "maths":{
            "q1":{
                "question":"5+7=?",
                "options":[
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer":"12"
            },
            "q2":{
                "question":"12-8=?",
                "options":[
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer":"4"
            }
        }
    }
}
print(questionbank['quiz']['sport']['q1']['question'])
print(questionbank['quiz']['maths']['q1']['question'])
print(questionbank['quiz']['maths']['q2']['question'])'''

'''data = {"menu": {
 "id": "file",
"value": "File",
"popup": {
  "menuitem": [
    {"value": "New", "onclick": "CreateNewDoc()"},
    {"value": "Open", "onclick": "OpenDoc()"},
    {"value": "Close", "onclick": "CloseDoc()"}
   ]}}}
for i in range(3):
    print(data['menu']['popup']['menuitem'][i]['value'])

lang  = ["spark","spark","spark","java","unix","unix","python","python"]
count={}
for i in lang:
    if i not in count.keys():
        count[i]=1
    else:
        count[i]+=1
print(count)

colors = [

{

"colors": "red",

"values": "#f00"

},

{

"colors": "green",

"values": "#0f0"

},

{

"colors": "blue",

"values": "#00f"

},

{

"colors": "cyan",

"values": "#0ff"

},

{

"colors": "magenta",

"values": "#f0f"

},

{

"colors": "yellow",

"values": "#ff0"

},

{

"colors": "black",

"values": "#000"

}

]
for i in colors:
    print(i['colors'],i['values'])'''

'''dict1={
"id": "0001",
"type": "donut",
"name": "Cake",
"image":
{
"url": "images/0001.jpg",
"width": 200,
"height": 200
},
"thumbnail":
{
"url": "images/thumbnails/0001.jpg",
"width": 32,
"height": 32
}
}'''

#regular expressions
'''import re

 

def search_emails(text):
    pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
    emails = re.findall(pattern, text)
    return emails

 

def check_emails_match(emails):
    pattern = r'\b[a-zA-Z0-9._%+-]+@example\.com\b'
    matching_emails = [email for email in emails if re.match(pattern, email)]
    return matching_emails

 

def substitute_pattern(emails):
    pattern = r'(\w)([\w.]*)(@\w+\.\w+)'
    substitution = r'\1*****\3'
    masked_emails = [re.sub(pattern, substitution, email) for email in emails]
    return masked_emails

 

def main():
    text = """
    Contact us at support@example.com or info@example.org.
    Email addresses: alice@example.com, bob@example.com, charlie@example.org
    """
    emails = search_emails(text)
    print("All found emails:", emails)

 

    matching_emails = check_emails_match(emails)
    print("Matching emails:", matching_emails)

 

    masked_emails = substitute_pattern(emails)
    print("Masked emails:", masked_emails)

 

if __name__ == "__main__":
    main()'''

#class and objects
'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print_details(self):
        print(self.name)
p1=Person('harish',21)
p1.print_details()

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def __eq__(self,other):
        return self.radius==other.radius
c1=Circle(2)
c2=Circle(3)
print(c1==c2)'''

'''class Vehicle():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def get_info(self):
        print(self.make,self.model,self.year)

class Car(Vehicle):
    def __init__(self,make,model,year,doors):
        self.doors=doors
    def get_info(self):
        print(self.doors)


c1=Car('toyota','1',2020,3)
c2=Car('lambo','2',2021,4)
c1.get_info()'''

#file handling
f=open('a.txt','w')
line1='welcome'
f.write(line1)
f.close()
f=open('a.txt','r')
a=f.readline()
print(a)
f.close()





