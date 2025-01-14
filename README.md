# sucrack
Bruteforce password of local linux user via su for priviledge escalation


## Usage
This Script makes repeated login attempts to a user with the su command.
It is usefull if the following conditions are met:
  * acces to python and the su command
  * no acces to /etc/shadow
  * wordlist tailored to the user or misconfigured ratelimit for su

Otherwise an attack is not realistic.
  
## Installation

#### pip
```sh
  pip install pexpect 
  git clone https://github.com/winter1245/sucrack
  cd sucrack
  python3 sucrack.py user 2
```

#### arch

```sh
  pacman -S python-pexpect
  git clone https://github.com/winter1245/sucrack
  cd sucrack
  python3 sucrack.py user 2 wordlist.txt
```

#### Syntax

```sh
  python3 sucrack.py [user to attack] [ratelimit float] [optional wordlistpath]
```


