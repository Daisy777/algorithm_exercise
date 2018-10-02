i = 4
d = 4.0
s = 'HackerRank '
# Read and save an integer, double, and String to your variables.
inI = int(input())
inD = float(input())
inS = input()
# Print the sum of both integer variables on a new line.
print(inI + i)
# Print the sum of the double variables on a new line.
print('{:.1f}'.format(inD+d))
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(''.join([s, inS]))