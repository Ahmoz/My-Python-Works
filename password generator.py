#random password generator
import random

#select password lenght
lenght_of_password = int(input("how many characters do you want to?-->>>"))

lenght_of_password2 = lenght_of_password

#password characters
characters_list = [["0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5"],
                   ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z","q","x","w"],
                   ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z","X","Q","W"],
                   ["!",",",".",":",";","_","-","?","/","|","=","&","%","+","#","!",",",".",":",";","_","-","?","/","|","="]]

#password list
user_password = []

#randomly selected characters and appending list
while lenght_of_password>0:
    user_password.append(characters_list[random.randint(0, 3)][random.randint(0,25)])
    lenght_of_password-=1 

#convert to string
user_password1 = ""

#appending string
for x in user_password:
    user_password1  += x
    

#printing password
print(user_password1)