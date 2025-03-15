def find_carry_numbers(num1, num2, carry_number=0):
    
    if num1==0 or num2 ==0:
        return carry_number
            
    new_num=num1%10+num2%10
    
    num1=num1//10
    num2=num2//10
    
    if new_num>=10:
        num1=num1+get_first_digit(new_num)
        carry_number+=1
        
    return find_carry_numbers(num1, num2, carry_number)

def get_first_digit(new_num):
    
    while new_num>=10:
        new_num//=10
        
    return new_num

# neccassary to pass small number as first argument
print(find_carry_numbers(101, 809))
print(find_carry_numbers(1, 99999))
print(find_carry_numbers(189, 209))
print(find_carry_numbers(1055, 999045))


# findWord(["P>E","E>R","R>U"])


#  p e r u
# p0 0 0 0

# e1 0 0 0

# r0 1 0 0

# u0 0 1 0
