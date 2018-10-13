# Server info
Basic script that shows useful information about the server it runs on.

## Usage
### Basic usage
Run ```python info.py``` in the target Linux console.<br>
This should output something like this
```
 -- Permissions
[*] SUDO: *yes/no*
 -- Machine Info
[*] OS: *OS*
[*] Distribution: *Distro*
[*] CPU: *number of cores*x *processor*
[*] RAM: *number* kB
 -- Connection
[*] COUNTRY: *country code*
[*] CITY: *city*
[*] ORG: *internet provider*
```

### Help command
Run ```python info.py -h``` in the target Linux console.<br>
This should output something like this
```
Optional arguments:

-h, --help: Shows this dialog and kills the program.
-ip: Shows the machine's public IP in the 'Connection' section.
```

### Show machine's IP
Run ```python info.py -ip``` in the target Linux console.<br>
This should ouput something like this
```
 -- Permissions
[*] SUDO: *yes/no*
 -- Machine Info
[*] OS: *OS*
[*] Distribution: *Distro*
[*] CPU: *number of cores*x *processor*
[*] RAM: *number* kB
 -- Connection
[*] IP: *ip*
[*] COUNTRY: *country code*
[*] CITY: *city*
[*] ORG: *internet provider*
```
