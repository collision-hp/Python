#P1                         
''' 
*
**
***
****
'''
for i in range (1,5):
    print('*'*i,end='')
    print()
    
#P2
'''
    *
   **
  ***
 ****
'''
#------X-------X--------X-------
for i in range (1,5):
    print(" "*(4-i),end='')
    print('*'*i,end='')
    print()
    
#P3
'''
****
 ***
  **
   *
'''
#------X-------X--------X-------
for i in range (0,4):
    print(" "*i,end='')
    print("*"*(4-i),end='')
    print()
    
#P4
'''
****
***
**
*
'''
#------X-------X--------X-------
for i in range (0,4):
    print('*'*(4-i),end='')
    print(' '*i,end='')
    print()
    
#P5
'''
* * * *
 * * *
  * *
   *
'''
#------X-------X--------X-------
for i in range (0,4):
    print(' '*i,end='')
    for k in range(0,4-i):
        print('* ',end='')
    print()
    
#P6
'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''
#------X-------X--------X-------
for i in range (0,4):
    print(" "*(3-i),end='')
    print('*'*(2*i+1),end='')
    print()
for i in range(1,4):
    print(" "*(i),end='')
    print("*"*(5-2*(i-1)),end='')
    print()

#P7
'''
     *

   *   *

  *     *

 *       *

***********
'''
#------X-------X--------X-------
for i in range(0,4):
    print(" "*(4-i),end='')
    if i==0:
        print(' *')
    else:
        print("*",end='')
        print(' '*(2*i+1),end='')
        print('*')
    
    print()
print('*'*(2*5+1))
  
#P8
'''
     *

   *   *

  *     *

 *       *

  *     *

   *   *

     *
'''
#------X-------X--------X-------    
for i in range(0,4): 
    print(' '*(4-i),end='')
    if i==0:
        print(' *')
    else:
        print('*',end='')
        print(' '*(2*i+1),end='')
        print('*')
    print()
for i in range(0,3):
    print(' '*(i+2),end='')
    if(i!=2):
        print('*',end='')
        print(' '*(5-2*i),end='')
        print('*')
    else:
        print(' *')
    print()
    
#P9
'''
* * * * *
*       *
*       *
*       *
* * * * *
'''
#------X-------X--------X------- 
for i in range(1,6):
    if (i==1 or i==5):
        print('* '*5)
    else:
        print('* ',end='')
        print('  '*3,end='')
        print('*')
#P10
'''
012345
01234
0123
012
01
0
'''
#------X-------X--------X-------
for i in range(0,6):
    for j in range(0,6-i):
        print(j,end='')
    print()
#P11
'''
1
33
555
7777
99999
'''
#------X-------X--------X------- 
for i in range (0,5):
    for j in range(0,i+1):
        print(2*i+1,end='')
    print()
#P12
'''
1
21
321
4321
54321
'''
#------X-------X--------X-------
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end='')
    print()
#P13
'''
1
24
369
481216
510152025
'''
#------X-------X--------X-------
for i in range(1,6):
    for j in range(1,i+1):
        print(i*j,end='')
    print()
#P14
'''
A
BC
DEF
GHIJ
KLMNO
PQRSTU
VWXYZ[\
'''
#------X-------X--------X-------
ch=65
for i in range(0,7):
    for j in range(0,i+1):
        character=chr(ch)    
        print(character,end='')
        ch+=1
    print()
#P15
'''
    1
   212
  32123
 4321234
543212345
'''
#------X-------X--------X-------
for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range(0,i):
        print(i-j,end='')
    for j in range(1,i):
        print(j+1,end='')
    print()
        