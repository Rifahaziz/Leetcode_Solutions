"""
Goal is to return the nth smallest key's item in a dictionary.
Input = dictionary , n (key) 
Output = n'th smallest item

Dictioonary example: 
{'laptop' : 999 , 'tv : 200 , 'watch : 111 }
So if n is 2, the output should be tv. 
Because when sorted with the items, it becomes 111,200,999. And n=2 means second item. 
Note that n=1 means 0th index of the dictionary. no we used the index as n-1 instead of n.


This question is from the problem set of Meta's coding practice problems.


"""




import math
# Add any extra import statements you may need here
# Add any helper functions you may need here

def return_smallest_key(inputDict, n):
  # Write your code here
  sorted_dict=sorted(inputDict.items(), key=lambda item: item[1])
  print("sorted dict", sorted_dict)
  val=""
  for i in sorted_dict :
    if(n==0 or n>len(inputDict)):
      val=None
    else:
      val=sorted_dict[n-1][0]
      
  print(val)
  return val


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printValue(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printValue(expected)
    print(' Your output: ', end='')
    printValue(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  
  # Testcase 1 
  inputDict1 = {"laptop": 999,"smartphone": 999,"smart tv": 500,"smart watch": 300,"smart home": 9999999}
  n1 = 2
  expected_1 = "smart tv"
  output_1 = return_smallest_key(inputDict1, n1)
  check(expected_1, output_1)
  
  # Testcase 2 
  inputDict2 = {"a": 10,"b": 20}
  n2 = 0
  expected_2 = None
  output_2 = return_smallest_key(inputDict2, n2)
  check(expected_2, output_2)
  
  # Testcase 3 
  inputDict3 = {"a": 1,"b": 2,"c": 3,"d": 4,"e": 5}
  n3 = 6 
  expected_3 = None 
  output_3 = return_smallest_key(inputDict3, n3)
  check(expected_3, output_3)

  # Testcase 4
  inputDict4 =  {"a": 10,"b": 20,"c": 3,"d": 2,"e": 9}
  n4 = 1 
  expected_4 = "d" 
  output_4 = return_smallest_key(inputDict4, n4)
  check(expected_4, output_4)

  # Add your own test cases here
