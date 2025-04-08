# Some operators checks about the relationship between two values and these operators are called relational operators. Given two numerical values your job is just to find out the relationship between them
# that is (i) First one is greater than the second (ii) First one is less than the second or (iii) First and
# second one is equal.

# Input
# First line of the input file is an integer t (t < 15) which denotes how many sets of inputs are there.
# Each of the next t lines contain two integers a and b (|a|, |b| < 1000000001).
# Output
# For each line of input produce one line of output. This line contains any one of the relational operators
# ‘>’, ‘<’ or ‘=’, which indicates the relation that is appropriate for the given two numbers.


# Q. what is the use of map() function and where to use it?
# ANS. It's a handy built-in function that applies a given function to each item in an iterable
#  (like a list, tuple, etc.) and returns an iterator with the results.
# ex:-list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = map(lambda x, y: x + y, list1, list2)

k = int(input("enter number of input set's"))
for _ in range(k):
    a, b = map(int, input(f"enter{k} pair").split())
    print('<' if a < b else '>' if a > b else '=')


