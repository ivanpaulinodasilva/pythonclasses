

#a = 27
#b = 93
#if a < b:
#    print("a is less than b")
#elif a > b:
#    print("a is greater than b")
#else: 
#    print ("a is equal to b")
    

    
#a = 16
#b = 25
#c = 27
#if a > b:
#    if b > c:
#        print ("a is greater than b and b is greater than c")
#    else: 
#        print ("a is greater than b and less than c")
#elif a == b:
#    print ("a is equal to b")
#else:
#    print ("a is less than b")
    
    
    
# object_size = 10
#if object_size > 5:
#    print('We need to keep an eye on this object')
#else:
#    print('Object poses no threat.')   
    
object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')