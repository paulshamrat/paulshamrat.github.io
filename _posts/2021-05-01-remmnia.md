---
layout: post
title:  "Remmnia- Remote Desktop Connection on Windows 10"
author: paulshamrat
image: assets/images/remmnia4.png
---
A raw and draft version of "Remmnia; Remote Desktop Connection" on my Ubuntu 20.04 LTS operating system. This is the notebook version during the whole trial and error. Tutorial may contain error as it is directly from my notebook.

## From ubuntu to windows
Inside Windows:
Enabling Remote access of your windows machine:
- Go to control panel
- system and security > system > remote settings > Remote > allow remote connections to this computer
- check mark allow connecction
- Select Users > add > name check name > add > apply > ok 
- You can allow it withoud adding name. 

## Finding out IP address/ Server
- Open cmd> ipconfig 
- This will show if configuration details 
- For myself there was there ip address
		a. ethernet adapter virtual box host only network
		b. ethernet adapter ethernet
		c. ethernet adapter vethernet(wsl)
	- Take the IP address for ethernet adapter ethernet
	- It was 168.192.0.102
	- Now you enabled remote access and got Ip address now rest of the task in your ubuntu
## Inside Ubuntu:
- Open remmina
- Click on the squire plus icon in the top left corner
- Write the ip address in the server option
- Give Username and password of your windows machine
- Save and connect and it will pop up your windows screen to inside your linux desktop

**Hurray; you did it!**

### Reference Tutorial
Follow this youtube video which help me during this activation
Setup and demonstration of remote desktop connections (Linux to Windows 10)
https://www.youtube.com/watch?v=Qb9lN3RCqVM


