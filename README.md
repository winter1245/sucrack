# sucrack
Bruteforce password of local linux user via su for priviledge escalation

Make sure you have proper authorisation before doing any testing.


## Usage
This Script makes repeated login attempts to a user with the su command.
It is usefull if the following conditions are met:
  * acces to python and the su command
  * no acces to /etc/shadow
  * wordlist tailored to the user or misconfigured ratelimit for su

Otherwise an attack is not realistic.
  
## Installation

#### pipx
```sh
  pipx install git+https://github.com/winter1245/sucrack
```

#### Syntax

```sh
  sucrack.py [user to attack] [ratelimit float] [optional wordlistpath]
```


