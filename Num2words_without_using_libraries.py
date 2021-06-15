## Number to Words Converter ##

num_1= {0: 'Zero', 1: 'One', 2:'Two', 3: 'Three', 4: 'Four', 5: 'Five',6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
10: 'Ten',11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',15: 'Fifteen', 16: 'Sixteen', 17:
'Seventeen', 18: 'Eighteen',19: 'Nineteen'}

num_2 = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty',6: 'Sixty', 7:'Seventy',8: 'Eighty',
9:'Ninety',10:'Hundred'}

print('### Welcome to number to word converter ###')

while True:
   print('~'*45)
   number=input('Enter a number / quit : ')
   print('~'*45)

   if number=='quit':
      break
   try:
      def word(num):
         if (0<= int(num) <= 19):
            print('The number',num,'in words =',num_1[num])

         elif (20<= int(num) <= 100):
            S1=(num//10)
            S2=(num%10)

            if S2!=0:
               print('The number',num,'in words =',(num_2[S1]+'-'+num_1[S2]))
            else:
               print('The number',num,'in words =',num_2[S1])
         else:
            print('Enter the number between the 0 to 100 range')
            word(int(number))
   except:
      print('Please enter the number')
