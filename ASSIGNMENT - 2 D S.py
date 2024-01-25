



# Problem - 1 : Program to interchange first and last number in a list
size = input( "enter size of the list   " )
try:
    int( size )
except:
    print( "enter valid size in numbers  ")
    quit()
def swap( size ):
    swapList = []
    for i in range( 0 , size ):
        a = input( "enter list element   " )
        try:
            int( a )
        except:
            print("enter valid value in numbers  ")
            quit()
        swapList.append( int( a ) )
    print( "list of values before swapping  " , swapList )
    swapList[ 0 ] , swapList[ size - 1 ] = swapList[ size - 1 ] , swapList[ 0 ]
    return ( swapList )
swapList = swap( int( size ) )
print( "list after swapping  " , swapList)




# Program - 2 : Program to find a srting is palindrome or not
string = input( "enter a string  " )
if ( string == string[::-1] ):
    print( "it is a palindrome" )
else:
    print( "it is not a palindrome" )




# Problem - 3 : Problem to find factorial of a number using recursion
num = input( "enter a number to find factorial  ")
try:
    int( num )
except:
    print( "enter the valid number " )
    quit()
if ( int(num) <= 0 ):
    print("enter the valid number ")
    quit()
def fact(num):
    if ( num == 1):
        return (num)
    else:
        return (num * fact(num - 1))
print("factorial of ", num, " is ", fact( int( num ) ))




# Problem - 4 : Problem to create list of tuples of a number and it's cube
size = int( input( "enter size of numbers in the list  " ) )
list1 = [int( input( "enter element  ") )for i in range( 0 , size )]
list3 = []
for i in list1:
    list3.append( ( i , i**3 ) )
print( list3 )




# Program - 5 : Program to print inverted star pattren of user defined number of times
size = int( input( "enter number of lines  " ) )
space = " "
astric = "*"
n =size
for i in range( 0 , size ):
    print( i * space , astric * n )
    n-=1




# Problem - 6 : Problem to swap 2 elements in a list of user choice
size = input( "enter size of the list   " )
try:
    int( size )
except:
    print( "enter valid size in numbers  ")
    quit()
def swap( size ):
    swapList = []
    for i in range( 0 , size ):
        a = input( "enter list element   " )
        swapList.append( a )
    a = int( input( "enter the 1st index of elements to be swapped  ") ) - 1
    b = int( input( "enter the 2nd index of elements to be swapped  ") ) - 1
    print( "list of values before swapping  " , swapList )

    swapList[ a ] , swapList[ b ] = swapList[ b ] , swapList[ a ]
    return ( swapList )
swapList = swap( int( size ) )
print( "list after swapping  " , swapList)




# Problem - 7 : Problem to remove the n'th repeating number in a sentence
string = input( "enter a string  " )
list = []
list = string.split()
print( list )
word = input( "enter the word to remove  " )
num = int(input( "enter the occurence number  " ) ) - 1
count = 0
for i in range( 0 , len( list ) ):
    if ( list[i] == word ) and ( count == num ):
        list.pop(i)
        break
    if ( list[i] == word ):
        count+=1
print( list )




# Problem - 8 : Problem to find the lenght of the string
size = int( input( "enter size of the list   " ) )
swapList = [input( "enter list value  " ) for i in range( 0 , size ) ]
c = 0
for i in range( 0 , size ):
    c+=1
print( len( swapList ) )
print( c )




# Problem - 9 : Problem to find if an element exist in a list
string = input( "enter a string  " )
list = []
list = string.split()
word = input( "enter the word to search  " )
b = 0
for i in list:
    if (i == word):
        b = 1
        break
    else:
        b = 0
if ( b == 1 ):
    print( "yes" )
else:
    print( "no" )




# Problem - 10 : Problem to reverse a list
size = int( input( "enter size of the list   " ) )
swapList = [input( "enter list value  " ) for i in range( 0 , size ) ]
print( swapList )
print( swapList[::-1] )




# Problem - 11 : Problem to swap first and last word in a string
string = input( "enter a sentence  " )
list = []
list = string.split()
print( "list before altering is  " , list )
list[ 0 ] , list[ len( list ) - 1 ] = list[ len( list ) - 1 ] , list[ 0 ]
print( "list after altering is  " , list )




# Problem - 12 : Problem to find if a substring is present in a string or not
string = input( "enter a sentence  " )
word = input( "enter the word to search  " )
if word in string:
    print( "yes" )
else:
    print( "no" )




# Problem - 13 : Problem to print even lenght in a given string
string = input( "enter a sentence  " )
list = []
list = string.split()
for i in list:
    if ( len( i ) % 2 == 0 ):
        print( i )




# Problem - 14 : Problem to accepet the string if only all vowels are present
string = input( "enter a sentence  " )
vowels = [ 'a' , 'e' , 'i' , 'o' , 'u' ]
letters = []
letters.extend( string )
for i in letters:
    if i in vowels:
        vowels.remove( i )
if ( len( vowels ) == 0 ):
    print(  'accepted' )
else:
    print( "not accepted" )
    for i in vowels:
        print("'", i ,"'", end = " , ")
    print(" are not present")




# Problem - 15 : Problem to print only non repeted letters in a string
string = input( "enter a sentence  " )
list = []
list.extend( string )
dict = {}
for i in string:
    dict[ i ] = dict.get( i , 0 ) + 1
for i in dict:
    if ( dict[ i ] > 1 ):
        dict[ i ] = 0
for i in dict:
    if ( dict[ i ] == 1 ):
        print( i , end = "")




# Problem - 15 : Problem to remove all duplicate letters from a string
string = input( "enter a sentence  " )
list = []
list.extend( string )
dict = {}
for i in string:
    dict[ i ] = dict.get( i , 0 ) + 1
for i in dict:
    if ( dict[ i ] > 1 ):
        dict[ i ] = 1
for i in dict:
    if ( dict[ i ] == 1 ):
        print( i , end = "")




# Problem - 15 : Problem to remove all duplicate letters from a string            ??????
string = input("enter a sentence  ")
list = []
list.extend(string)
for i in range(0,len(list) - 1):
    for j in range(i+1,len(list)):
        if (list[i]==list[j]):
            list.pop(j)
print("the string after all duplicate letters been removed is:")
for i in list:
    print(i,end="")




# Problem - 15 : Problem to remove all duplicate letters from a string
string = input("enter a string  ")
unique = set()
newstr = ""
for let in string:
    unique.add(let)
newstr= "".join(sorted(unique))
print(newstr)





# Problem - 15 : Problem to remove all duplicate letters from a string
string = input("enter a sentence  ")
list = []
temp = ""
for i in string:
    if i not in temp:
        temp = temp + i
print(temp)




# Problem - 16 : Problem to find the sum of all values in a dictionary
dict ={}
n = int( input("enter size  "))
for i in range(0,n):
    key = input("enter key ")
    val = int(input("enter value "))
    dict[key] = val
print(dict)
s = 0
for i in dict:
    s = s + dict[i]
print("sum = ",s)




# Problem - 17 : Problem to convert list of tuples into dictionary                  ????????
size = int(input("enter the number of elements  "))
a = [(input("enter value  "))for i,j in range(0,size)]
print(a)




# Problem - 18 : Problem to HANOI TOWER
n = int(input("enter the number of discs  "))
s = "source"
t = "tempravory"
d = "destination"
def hanoi(n,s,t,d):
    if (n==1):
        print("move disc ",n," from ",s," to ",d)
    else:
        hanoi(n-1,s,d,t)
        print("move disc ",n," from ",s," to ",d)
        hanoi(n-1,t,s,d)
a = hanoi(n,s,t,d)
print(a)



# Problem - 19 : Problem to copy even lines of data from one file to another file
f1w = open("text1.txt", "w")
f1w.write("hello\nworld\npython\nlang")
f1w.close()
f1r = open("text1.txt")
f2w = open("text2.txt", "w")
c = 1
print("\ndata in text file 1\n")
for i in f1r:
    print(i)
    if (c%2 != 0):
        f2w.write(i)
    c+=1
f2w.close()
f2r = open("text2.txt")
print("\ndata in text file 2\n")
for i in f2r:
    print(i)




# Problem - 20 : Problem to find if a user entered string contains all unique characters or not
string = input("enter a string  ")
dict = {}
for i in string:
    dict[i] = dict.get(i,0) + 1
b = 0
for i in dict:
    if (dict[i] == 1):
        b = 0
    else:
        b = 1
        break
if (b == 0):
    print("the entered string is unique/it does'nt contain any duplicate or repetations")
else:
    print("the entered string is not unique/it does contain any duplicate or repetations")