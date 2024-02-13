import random
import string
import requests
from django.http import HttpResponse

#Function to generate random password
def random_string(letter_count=5, digit_count=3):  
        str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))  
        str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))  
    
        sam_list = list(str1) # it converts the string to list.  
        random.shuffle(sam_list) # It uses a random.shuffle() function to shuffle the string.  
        final_string = ''.join(sam_list)  
        return (final_string)

# class PassGenerator:
#         password = random_string()
class PassGenerator:
        def __init__(self, password):
                self.password = password

def password_generator(request):
        password = random_string()
        p1 = PassGenerator(password)
        # print("P1 is ",p1.password)
        return HttpResponse(p1.password)