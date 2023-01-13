import random as rd
def main():
 alpha_LowChars=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 randomNum=rd.randint(15,25)
 alpha_UpperChars=[alpha_UpperChar.upper() for alpha_UpperChar in alpha_LowChars]
 alpha_Chars=alpha_LowChars+alpha_UpperChars
 alpha_Chars.extend(str(range(10)))
 symbols = ['+', '-', '*', '/', '%', '&', '|', '^', '~', '=', '!', '<', '>']
 all_Chars=alpha_Chars+symbols
 rdChars=[]
 for rand in range(randomNum):
  rdChars.append(rd.choice(all_Chars))
 rdPass="".join(rdChars)
 print("Here is your Password:",rdPass)
 inChoice=input("Enter 'Y/N' or 'y/n' to continue:\n>> ")
 if inChoice=="Y" or inChoice=="y":
  main()
 elif inChoice=="N" or inChoice=="n":
  exit()
 else:
  print("Invalid Choice. Please enter either 'Y/N' or 'y/n' to continue:\n>> ")
  main()
main()