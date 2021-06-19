# TAPIM
## Telegram And Python pIng Monitor

This project it's a simple script for send mensages with telegram when as host go up or down, it's very simple to use, you just need to put de telegram bot id and de chat_id of de addressee and put to run

## Get Start
Download or clone the repository OBS: The script create/edit a file named "last.txt" when are running remember to give the permissions on the folder
### Config
To config the script it's very simples you only go to need the bot_token, chat_id and the IP of the hosts for ping
#### Set bot_token
Inside the def telegram_bot_sendtext there are a var named bot_token it's just put the token here
```python
def telegram_bot_sendtext(bot_message,bot_chatID):    
    bot_token = ''#put here the bot token
```
### Set chat_id
Inside the def ping_test there are a call for telegram_bot_sendtext and you need to put the chat_id on the second parameter
```python
def ping_test (host,last):
  [...]
    telegram_bot_sendtext(message,"")#put here the chat_id of the addressee
```
Obs: You can send for multiple addressee calling the function( `telegram_bot_sendtext` ) many times
### Set hosts
On the script there are two variables named hosts and last, the both are arrays, aond you out the IP adresss of the hosts on the host array and you need to put the same number of hosts variables on the last using the number 1, I think this is confused, see the exemple below
```python
hosts = ["10.33.1.254","10.3.0.132"]#Hosts list
last=["1","1"]
```

## FAQ
### What's "last.txt"
You can use use this file for get the hosts/server status with another application
```
10.33.1.254:1
10.3.0.132:1
```
the file have the n lines with the ip and the status `ip:status` 0 for down and 1 for up
