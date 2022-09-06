# Q 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)


decimal_num = int ( input ( 'enter decimal number you want to convert binary :' ) )
bin_num = [ ]
remender = 1
while True :
    remender = decimal_num % 2
    bin_num . append ( remender )
    decimal_num = decimal_num // 2
    if decimal_num == 0 :
        break
bin_num . reverse ( )
print ( 'the converted binary number is ' , end = '' )
for element in bin_num : print ( element , end="" )