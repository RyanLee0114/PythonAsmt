
qa = {
'1.What is 2 x 5? a.5 b.3 c.29 d.47 e.10': 'e',
'2.What is - 15 + 15? a.30 b.18 c.0 d.-30 e.169': 'c',
'3.What is 253 x 34? a.54637 b.28690543 c.93930 d.01039 e.8602': 'b',
'4.What is 250 x 4? a.750 b.1000 c.10000 d.100 e.500': 'b',
'5.What is 76 x 6 - 24? a.432 b.463 c.-992 d.264 e.89': 'a',
'6.What is 7291 + 8830? a.16121 b.36719 c.18382 d.18302 e.94002': 'b',
'7.What is 3 + 23? a.74 b.-26 c.36 d.26 e.10': 'd',
'8.What is 372910/5? a.73920 b.36210 c.74582 d.9030 e.193910': 'b',
'9.What is 761 x 28? a.24713 b.21308 c.38210 d.3721 e.28491': 'e',
'10.What is -45 + 55? a.10 b.-10 c.100 d.20 e.-100': 'a'
}

for q, a in qa.items():
    print(q)

    ans = input('Enter your answer: ')
    if ans == a:
      print ('Correct') 
    else:
      print ('Incorrect') 
      print('Correct answer is --> ',a)




