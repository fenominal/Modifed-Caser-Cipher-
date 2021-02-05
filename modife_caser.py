def encryption(pt,key):
 ptlist = list(pt)
 ct= " "
 for i in range(len(ptlist)):
     asc = ord(ptlist[i])
     if i % 2 == 0:
         asc = asc + ((key + 1 )%26)
     else :
         asc = asc + ((key - 1 )%26)

     if ptlist[i].isupper():
         if asc > 90:
             asc = asc - 26
     elif ptlist[i].islower():
         if asc > 122:
             asc = asc - 26
     newch = chr(asc)
     ct = ct + newch
 return ct

def decryption(ct,key):
 cflist = list(ct)
 pt = " "
 for i in range(len(cflist)):
     asc = ord(cflist[i])
     if i % 2 == 0:
         asc = asc - ((key + 1 )%26)
     else :
         asc = asc - ((key - 1 )%26)
     if cflist[i].isupper():
         if asc <65:
             asc = asc + 26
     elif i.islower():
         if asc < 97:
             asc = asc + 26
     newch = chr(asc)
     pt = pt + newch
 return pt

choice = int(input("1.Encryption 2.Decryption "))
if choice == 1:
 pt = input("Enter any text: ")
 key = int(input("Enter key: "))
 cf = encryption(pt,key) 

 print ("orignal text: ",pt)
 print ("encrypt text:",cf)
elif choice == 2:
 cf = input("Enter any text: ")
 key = int(input("Enter key: "))
 pt = decryption(cf,key)
 print ("orignal text: ",cf)
 print ("encrypt text:",pt)