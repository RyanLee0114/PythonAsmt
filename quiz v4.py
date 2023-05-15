qa = {
'What is 2 x 5?': 'e',
'What is - 15 + 15?': 'c',
'What is 253 x 34?': 'b',
'What is 250 x 4?': 'b',
'What is 76 x 6 - 24?': 'a',
'What is 7291 + 8830?': 'c',
'What is 3 + 23?': 'd',
'What is 372910/5?': 'b',
'What is 761 x 28?': 'e',
'What is -45 + 55?': 'a'
}

options = [
[' a. 5', ' b. 3', ' c. 29', ' d. 47', ' e. 10'],
[' a. 30', ' b. 18', ' c. 0', ' d. -30', ' e. 169'],
[' a. 54637', ' b. 28690543', ' c. 93930', ' d. 01039', ' e. 8602'],
[' a. 750', ' b. 1000', ' c. 10000', ' d. 100', ' e. 500'],
[' a. 432', ' b. 463', ' c. -992', ' d. 264', ' e. 89'],
[' a. 16121', ' b. 36719', ' c. 18382', ' d. 18302', ' e. 94002'],
[' a. 74', ' b. -26', ' c. 36', ' d. 26', ' e. 10'],
[' a. 73920', ' b. 36210', ' c. 74582', ' d. 9030', ' e. 193910'],
[' a. 24713', ' b. 21308', ' c. 38210', ' d. 3721', ' e. 28491'],
[' a. 10', ' b. -10', ' c. 100', ' d. 20', ' e. -100']
]

score = 0
q_num = 0
user_name = input('Enter your name : ')

for q, a in qa.items():
   print ('--------------------','Question',q_num + 1,'--------------------')
   print (q)
   for o in options[q_num]:
       print (o)
   q_num += 1
   ans = input('Enter your answer: ')
   while ans.lower() not in ['a', 'b', 'c', 'd','e']:
      print("Your answer can only be a,b,c,d or e.")
      ans = input('Enter your answer: ')
   if ans == a:
      print ('Correct')
      score += 1
   else:
      print ('Incorrect') 
      print('Correct answer is --> ',a)
   print('Your score: ', score)

print ('--------------------Total score--------------------')
print(user_name,', Your score: ', score)
if score < q_num /2:
    print("Try harder!")
else:
    print("Well done!")
print ('------------------------------------------------------------')





