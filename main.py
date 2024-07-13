import hashlib
from urllib.request import urlopen

def readwordlist(url):
  try: 
    wordlistfile = urlopen(url).read()
  except Exception as e:
    print("Hey there was some error while reading the wordlist, error:", e)
    exit()
  return wordlistfile

def hash(wordlistpassword):
  result = hashlib.sha1(wordlistpassword.encode())
  return result.hexdigest()

def bruteforce(guesspasswordlist, actual_password_hash):
  for guess_password in guesspasswordlist:
    if hash(guess_password) == actual_password_hash:
      print("Hey! your password is:", guess_password, 
            "Congrats! I have cracked your password, Please change it")
      exit()
url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'

print("Enter your actual password and let me see if I have it in my files!\n ex: trying entering 'bob' as a password without the ''")
actual_password = input()
actual_password_hash = hash(actual_password)

wordlist = readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')

bruteforce(guesspasswordlist, actual_password_hash)

print("Hey! I couldn't crack your password, as it was not in the wordlist, YOU WIN!!!")