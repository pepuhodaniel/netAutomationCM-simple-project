import telnetlib
import getpass
print("===================================================")
print("NetAutomation Using Telnetlib")
print("Configure Cisco Device")
print("===================================================")
loop = "y"
while(loop == "y"):
    if loop !="y":
           break
    print("Enter the IP Address, Username, and Password")
    host = raw_input("masukan IP telnet:")
    user = raw_input("masukan username:")
    password = getpass.getpass()

    # print list
    print("===============================================")
    print("Silahkan Pilih konfigurasi")
    print("1. Change Hostname")
    print("2. Create Vlan")
    print("3. Show Vlan")
    print("4. Time Setting")
    print("===============================================")

    tn = telnetlib.Telnet(host)
    tn.read_until("Username:")
    tn.write(user + "\n")
    if password:
       tn.read_until("Password:")
       tn.write(password + "\n")
       opt = raw_input("Silahkan pilih konfigurasi: ")

    #option
    if opt=="1":
       tn.write("en\n")
       tn.read_until("Password:")
       tn.write("1234\n")
       tn.write("configure terminal\n")
       hostname = raw_input("1. Enter the hostname : ")
       tn.write("hostname {}\n".format(hostname))
       tn.write("end\n")
       tn.write("exit\n")
       print tn.read_all()

    elif opt=="2":
        tn.write("en\n")
        tn.read_until("Password:")
        tn.write("1234\n")
        tn.write("configure terminal\n")
        vlan = raw_input("2. Add new Vlan : ")
        vlan_name = raw_input("2. Add name : ")
        tn.write("vlan {}\n".format(vlan))
        tn.write("name {}\n".format(vlan_name))
        tn.write("end\n")
        tn.write("exit\n")
        print tn.read_all()

    elif opt=="3":
        tn.write("en\n")
        tn.read_until("Password:")
        tn.write("1234\n")
        tn.write("show vlan brief\n")
        tn.write("exit\n")
        print tn.read_all()

    elif opt=="4":
        tn.write("en\n")
        tn.read_until("Password:")
        tn.write("1234\n")
        clock_set = raw_input("4. Add Time(ex: 10:50:00): ")
        date_set = raw_input("4. Add Date(ex :01): ")
        month_set = raw_input("4. Add Month(ex: Jan): ")
        year_set = raw_input("4. Add Year(ex :2021): ")
        tn.write("clock set {} {} {} {}\n".format(clock_set,date_set,month_set,year_set))
        tn.write("exit\n")
        print tn.read_all()

        


    else:
        print("Incorrect Option!!!")

    print("======================================") 
    loop = raw_input("Config again? (y,n) ")
    print("======================================")   
