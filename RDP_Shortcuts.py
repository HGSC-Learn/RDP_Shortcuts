import os
from time import sleep

red = "\033[1;31;40m"
blue = "\033[1;34;40m"
yelo = "\033[1;33;40m"
green = "\033[1;32;40m"
banner =f"""
 {red}                                                                                     
 {red}    // | |                               {yelo}      //   ) )                               
 {red}   //__| |      __       ( )      ___   {yelo}      //___/ /     / __        ___       ( )  
 {red}  / ___  |   //   ) )   / /     ((   ) )  {yelo}   / __  (      //   ) )   //   ) )   / /   
 {red} //    | |  //   / /   / /       \ \     {yelo}   //    ) )    //   / /   //   / /   / /    
 {red}//     | | //   / /   / /     //   ) )   {yelo}  //____/ /    //   / /   ((___( (   / /     
"""

print(banner)
print("\n")


print(f"{blue}setup & Install {green}({yelo}0{green})")
print(f"{blue}Rdp {yelo}({green}On 1{yelo})")
print(f"{blue}Rdp {yelo}({red}Off 2{yelo})")


usr = input(f"{green} Enter Item: {yelo}")

if usr=="0":
    print(f"{green}Installing.....")
    os.system("sudo apt insatll vncserver")
    os.system("sudo apt insatll xrdp")
    os.system("clear")
    print(f"{green}Installing Done")
elif usr=="1":
    os.system("vncserver")
    sleep(2)
    os.system("service xrdp start")
    os.system("""echo -ne "\033]0;Starting Server\007" && clear;if HOME=/root;USER=root;sudo -u root LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgcc_s.so.1 nohup vncserver :1 -localhost no -name "NetHunter KeX"  >/dev/null 2>&1 </dev/null;then echo "Server started! Closing terminal..";else echo -ne "\033[0;31mServer already started! \n";fi && sleep 2 && exit""")
elif usr=="2":
    os.system("vncserver --kill :1")
    os.system("vncserver --kill :2")
    os.system("vncserver --kill :3")
    os.system("vncserver --kill :4")
    os.system("vncserver --kill :5")    
    os.system("vncserver --kill :6")
    os.system("vncserver --kill :7")
    os.system("vncserver --kill :8")
    os.system("vncserver --kill :9")    
    sleep(2)
    os.system("service xrdp stop")
    os.system("""echo -ne "\033]0;Killing Server\007" && clear;sudo -u root vncserver -kill :1 ;sleep 2 && exit""")
    os.system("""echo -ne "\033]0;Killing Server\007" && clear;sudo -u root vncserver -kill :2 ;sleep 2 && exit""")
    os.system("""echo -ne "\033]0;Killing Server\007" && clear;sudo -u root vncserver -kill :3 ;sleep 2 && exit""")
    os.system("""echo -ne "\033]0;Killing Server\007" && clear;sudo -u root vncserver -kill :4 ;sleep 2 && exit""")
    os.system("""echo -ne "\033]0;Killing Server\007" && clear;sudo -u root vncserver -kill :5 ;sleep 2 && exit""")
    os.system("""echo -ne "\033]0;Killing Server\007" && clear;sudo -u root vncserver -kill :6 ;sleep 2 && exit""")
    os.system("""echo -ne "\033]0;Killing Server\007" && clear;sudo -u root vncserver -kill :7 ;sleep 2 && exit""")
    os.system("""echo -ne "\033]0;Killing Server\007" && clear;sudo -u root vncserver -kill :8 ;sleep 2 && exit""")
    os.system("""echo -ne "\033]0;Killing Server\007" && clear;sudo -u root vncserver -kill :9 ;sleep 2 && exit""")
else:
    print(f"{blue}Enter {green}1{yelo},{red}2 {blue}options")
