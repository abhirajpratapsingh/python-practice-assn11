# Q 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method

decimal = int ( input ( 'enter number you want to convert in octal number :' ) )
oct = [ ]
remain = 1
while True :
    remain = decimal % 8
    oct . append ( remain )
    decimal = decimal // 8
    if decimal == 0 : break
oct . reverse ( )
print ( 'the converted octal number is' )

for element in oct : print ( element , end = '' )
