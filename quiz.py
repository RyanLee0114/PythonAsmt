
qa = {
    '1.How many elements are on the periodic table? a. 101 b. 118 c. 121 d. 212': 'b',
    '2.What is the symbol for mercury on the periodic table?': 'a',
    '3.What kind of bond is formed when a compound is made up of elements that share the same electrons?': 'b',
    '4.Bronze is created by mixing which two metals?': 'b',
    '5.Which element is most abundant in Earth’s crust?': 'a',
    '6.Tufa is a type of?': 'c',
    '7.In 2019, scientists were shocked to find what at the bottom of the Mariana Trench?': 'c',
    '8.Which of the following animals was among those on the first ever hot air balloon flights in 1783?': 'a',
    '9.Heavy metals such as gold were originally created:': 'd',
    '10.Whales communicate through what kind of sound waves?': 'a'
}

for q, a in qa.items():
    print(q)

    ans = input('Enter your answer: ')
    if ans == a:
      print ('Correct') 
    else:
      print ('Incorrect') 
      print('Correct answer is --> ',a)




