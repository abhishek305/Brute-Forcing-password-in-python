import string
paswd = input("Insert Password to crack: \n")
def Check(charset, pchar):
    for char in charset:
      if char==pchar:
           print("Trying...", char)
           print(" ==>",char, "<==  Matched")
           break
      else:
           print("Trying...",char)
def Bruteforce(paswd):
   print("[+][+] Starting Brute Force...")
   charset = list(string.ascii_letters)
   charset1 = list(string.digits)
   charset2 = list(string.punctuation)
   result=""
   x=0
   while x<=len(paswd)-1:
      pchar=paswd[x]
      if pchar in charset:
              Check(charset,pchar)
              x+=1
              result+=pchar
      elif pchar in charset1:
              Check(charset1,pchar)
              x+=1
              result+=pchar
      elif pchar in charset2:
              Check(charset2,pchar)   
              x+=1  
              result+=pchar
   print(" All Matched - Password Found:", result)
Bruteforce(paswd) 

