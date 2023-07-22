# Python-Rootkit
## Easy way to elevate to the System user account
#### Build using Pyinstaller:
```
pyinstaller --onefile main.py
```
#### Once that's done navigate to dist and run main.exe as Administrator
##### When a Windows computer starts up, the operating system kernel runs with the highest level of privileges, known as kernel mode. The `NT AUTHORITY\SYSTEM` account represents the operating system in kernel mode and has full control over the system, including access to all resources and the ability to execute privileged instructions.
##### thanks to winpwnage for making this possible
