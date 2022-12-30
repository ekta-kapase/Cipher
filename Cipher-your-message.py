#Code by Ekta Kapase

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(plain_text, shift_no):
  if shift_no >= 26:
    shift_no %= 26
  if direction == "decode":
    shift_no *= -1
  caesar_text = ""
  for i in plain_text:
    if i in alphabet:
      position = alphabet.index(i)
      new_position = position + shift_no
      new_letter = alphabet[new_position]
      caesar_text += new_letter  
    else:
      caesar_text += i
  print(f"Your {direction}d text is {caesar_text}")

from art import logo

print(logo)

start = "yes"
while start == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift)

  start = input(
      "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

print("Thank you for using Caesar cipher! Goodbye! ")
