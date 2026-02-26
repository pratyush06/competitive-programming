def place():


def backtrack(elements, divisor, no_of_element,choosen_element, memo, curr_idx=None):
    if curr_idx is None:
        curr_idx = 0
    
    if curr_idx==len(elements) or len(choosen_element)==no_of_element:
        return 0
    
    response = backtrack(elements, divisor, no_of_element, choosen_element, memo, curr_idx+1)
    if place():
        (elements[curr_idx]+backtrack(elements, divisor, no_of_element, choosen_element, memo, curr_idx+1))%divisor



N=10,
Q=2
elements = [1,2,3,4,5,6,7,8,9,10]
D=5
no_of_element=1

# D=5
# no_of_element=2
