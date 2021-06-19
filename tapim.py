import subprocess
import requests
import time


def telegram_bot_sendtext(bot_message,bot_chatID):
    
    bot_token = ''#put here the bot token
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    print("Enviando mensagem para "+bot_chatID)
    try:
        response = requests.get(send_text)
        return response.json()
    except:
        print("Erro ao enviar mensagem")
        x="Erro, sem internet"
        return x


def ping_test (host,last):
    
    message=""
    temp=""
    original_last=last
    reached = []
    not_reached = []
    new_reached = []
    new_not_reached = []
    var_not_reached = []
    var=0
    while (var<len(hosts)):
        print("host: "+hosts[var]+" Status: "+last[var])
        print ("last[var]="+last[var]+"original_last[var]="+original_last[var])
        var=var+1
    var=0

    while (var<len(hosts)):
        ping_test = subprocess.call('ping %s -n 1' % hosts[var])        #Ping host n times
        ##Testa o Ping Novamente N vezes cado de timeout
        retry_ping=0 #contagem do loop de ping
        max_retry_ping=4 # quantidade maxima de pings a se fazer no loop
        if (ping_test != 0 and original_last[var]=="1"):
            var_not_reached.append(hosts[var])
            while (retry_ping<max_retry_ping):
                print("Tentando pingar novamente... "+hosts[var])
                ping_test = subprocess.call('ping %s -n 1' % hosts[var])        #Ping host n times
                if ping_test == 0:#caso ping positivo o loop é interrompido
                    retry_ping=max_retry_ping
                else:
                    retry_ping=retry_ping+1
        ##
                
        if ping_test == 0:                    #If ping test is 0, it' reachable
            reached.append(hosts[var])
            #print(last[var])
            if last[var]=="0":
                #print("entrei no if")
                last[var]="1"
                new_reached.append(hosts[var])
        else:
            ##not_reached.append(hosts[var])                              #Else, it's not reachable
            if last[var]=="1":
                last[var]="0"
                ##new_not_reached.append(hosts[var])
        var=var+1
    var=0
    #tenta os pings negativos novamente
    while (var<len(hosts)):
        print ("last[var]="+last[var]+"original_last[var]="+original_last[var])
        if ((last[var]=="0" and original_last[var]=="1") or (hosts[var] in var_not_reached)):
            print("Entrei no IF")
            ping_test = subprocess.call('ping %s -n 1' % hosts[var])        #Ping host n times
            ##Testa o Ping Novamente N vezes cado de timeout
            retry_ping=0 #contagem do loop de ping
            max_retry_ping=4 # quantidade maxima de pings a se fazer no loop
            if ping_test == 0:
                print("Voltou!!!")
            else:
                while (retry_ping<max_retry_ping):
                    print("Tentando pingar novamente..."+hosts[var]+" na segunda parte" )
                    ping_test = subprocess.call('ping %s -n 1' % hosts[var])        #Ping host n times
                    if ping_test == 0:#caso ping positivo o loop é interrompido
                        retry_ping=max_retry_ping
                    else:
                        retry_ping=retry_ping+1
            ##
                    
            if ping_test == 0:                    #If ping test is 0, it' reachable
                reached.append(hosts[var])
                #print(last[var])
                if last[var]=="0":
                    #print("entrei no if")
                    last[var]="1"
                    if original_last[var]=="0":
                        new_reached.append(hosts[var])
            else:
                not_reached.append(hosts[var])                              #Else, it's not reachable
                last[var]="0"
                new_not_reached.append(hosts[var])
        elif(last[var]=="0" and original_last[var]=="0"):
            not_reached.append(hosts[var])
        var=var+1
    var=0
    while (var<len(hosts)):
        print("host: "+hosts[var]+" Status: "+last[var])
        var=var+1

    print("{} is reachable".format(reached))
    print("{} not reachable".format(not_reached))
    print("{} is reachable".format(new_reached))
    print("{} not reachable".format(new_not_reached))
    arquivo = open("last.txt", "w")
    count=0
    status = list()
    while(count<len(hosts)):
        status.append(hosts[count]+":"+last[count]+"\n")
        count=count+1
    arquivo.writelines(status)
    arquivo.close()
    temp=""
    #time.sleep(1)
    if(len(new_reached)>0 or len(new_not_reached)>0):
        message="Olá, esse é o relatorio de mudanças da sua rede%0A"
        count=0
        while (count<len(new_reached)):
            temp=temp+new_reached[count]+"✅%0A"
            count=count+1
        message=message+temp
        count=0
        temp=""
        while (count<len(new_not_reached)):
            temp=temp+new_not_reached[count]+"❌%0A"
            count=count+1
        message=message+temp
        telegram_bot_sendtext(message,"")#put here the chat_id of the destiny
        temp=""
    return last


hosts = ["10.33.1.254","10.3.0.132","10.33.3.254","10.33.4.254","10.33.5.254","10.33.6.254","10.33.7.254","10.33.8.254","10.33.99.254"]#Hosts list
last=["1","1","1","1","1","1","1","1","1"]
var=1
while (var==1):
    last=ping_test(hosts,last)
    time.sleep(1)
