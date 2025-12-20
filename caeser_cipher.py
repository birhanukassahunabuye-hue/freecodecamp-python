alphabet = 'abcdefghijklmnopqrstuvwxyz'
def caeser_cipher(orginal_text, shift_amount, mode):


    output_text = ""
    if mode=="decode":
       shift_amount *=-1


    for char in orginal_text:
       if char in alphabet:
          index= alphabet.find(char)
          new_index= (index + shift_amount) %26

          output_text +=alphabet[new_index]
       else:
          output_text+=char
    print(f"The {mode}d text is: {output_text}")
while True:
   direction = input("Type 'encode to encrypt, type 'decode' to decrypt, or 'exit' to quit: ").lower()
   if direction=="encode" or direction=="decode":
     text = input("Type your message: ").lower()
     shift = int(input("Type the shift number: "))
     caeser_cipher(text, shift, direction)
   
   elif direction == "exit":
      break
   else:
      print("Invalid option, please try again.")
   

   
   