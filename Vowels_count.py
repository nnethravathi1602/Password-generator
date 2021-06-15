#Enter a sentence and find out vowels
sentence=input("Your sentence : ")
print(sentence)
count=0
for k in sentence:
   if k=='a' or k=='A':
     count+=1
   elif k=='e' or k=='E':
      count+=1
   elif k=='i' or k=='I':
     count+=1
   elif k=='o' or k=='O':
      count+=1
   elif k=='u' or k=='U':
      count+=1
print("\nTotal vowels in your sentence are",count)
