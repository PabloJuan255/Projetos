#Please do not start the sentence in lower case!
text = '{0}:'
print('AI:Whats you name?')
UserName = input("You:")
print("AI:",UserName,"is a good name.")
print("AI:What do you want to do?")
print('about me,joke')
Answer = input(text.format(UserName))
if Answer == "Joke":
 print ('I’m on a seafood diet.')
 print ('What’s a seafood diet?')
 print ('When I “see food”, I eat it.')
 input()
 print ('Question: Which hand is better to write with?')
 print ('Neither, it’s best to write with a pen.')
 
if Answer == "About me":   
 print('AI:I’m was raised on 2019/12/13, including a simplified,because my Creator does not understand how to install a ChatBot in Python.')
else: 
 print('AI:I’m a joke to you?')

while(True):
  print("AI:What do you want to do?")
  print('about me,joke')
  Answer = input(text.format(UserName))
  if Answer == "Joke":
   print ('Question: Which hand is better to write with?')
   print ('Neither, it’s best to write with a pen.')
     
  if Answer == "About me":   
   print('AI:I’m was raised on 2019/12/13, including a simplified,because my Creator does not understand how to install a ChatBot in Python.')
  else: 
   print('AI:ERROR!')
