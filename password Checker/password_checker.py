#Password Checker Example :
#Set your password :
 #  p4n@in
 #  Enter your Password :
 #  p4n
 #  wrong password ... try 2 more time out of 2
 #  p4n@
#   wrong password ... try 1 more time 1
 #  p4n@34
#   wrong password ... try 0 more time 0
 ##  note : user select right password
 #  then start MCQ EXAM...


 #  1. Who invented Java Programming?
  # 1. ) Guido van Rossum
 #  2. ) James Gosling
 #  3. ) Dennis Ritchie
 #  4. ) Bjarne Stroustrup

 #  Select Answer 2

 #  wrong answer [ Try Next year ]

 #  Note :if select Right Answer
 #  ask 2nd Question ...

 #  2. Which component is used to compile, debug and execute the java programs?
 #  1. ) JRE
 #  2. ) JIT
 #  3. ) JDK
 #  4. ) JVM

 #  Select Answer 2 ... con..

password=(input('set a password : '))

enter=(input('enter passsword: '))

if enter==password:
  print('1 Who invented Java Programming? \n1 Guido van Rossum  \n2.James Gosling \n3.Dennis Ritchie \n4.Bjarne Stroustrup')
  answer=int(input('Enter the answer in number:'))
  if answer==2:
    print('2. Which component is used to compile, debug and execute the java programs? \n1.JRE\n2.JIT\n3. JDK\n4.JVM')
  else:
    print('your answer is wrong try next year')
else:
    if enter!=password:
      password=(input('Enter your password:'))
      if enter!=password:
          password=(input('enter a password:'))
          if enter!=password:
            print('try next year')