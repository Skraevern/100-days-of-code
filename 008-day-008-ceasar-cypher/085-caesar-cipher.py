import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = ""
text = ""
shift = ""
again = "yes"

def user_inputs():
    global direction, text, shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    while direction != "encode" and direction != "decode":
        print('Please try again. Or press "control + c" to quit')
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

def caesar(string, shift_amount, direction):
    
    encrypted_text = ""
    for letter in string:
        if letter not in alphabet:
            encrypted_text += str(letter)
        else:  
            for i in range(0, len(alphabet)):
                if letter == alphabet[i]:
                    if direction == "encode":
                        while i + shift_amount >= 26:
                            shift_amount -= 26
                        encrypted_text += alphabet[i + shift_amount]
                    if direction == "decode":
                        while i + shift_amount <= -1:
                            shift_amount += 26
                        encrypted_text += alphabet[i - shift_amount]
  
    print(f'The {direction}d text is "{encrypted_text}"')
        
print(art.logo)
while again == "yes":
    user_inputs()
    caesar(text, shift, direction)
    again = input('Type "yes" if you want to go again. Type "no" if you want to quit. ')
print("Goodbye")

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

# -------------------------------------------------------------------------------------


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.