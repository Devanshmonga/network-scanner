import scapy.all as scapy
import optparse

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    print("IP\t\t\tMAC ADDRESS")
    print("---------------------------------------------------------")
    clients_list=[]
    for element in answered:
        client_dict={'ip':element[1].psrc , 'mac':element[1].hwsrc}
        clients_list.append(client_dict)
    return (clients_list)


def print_result(result_list):
     print('IP\t\t\tMAC ADDRESS\n---------------------------------------------------------')
     for client in result_list:
         print(client['ip']+'\t\t' +client['mac'])


def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option('-t','--target',dest='target',help='target IP/ IP range')
    (option,arguments)=parser.parse_args()
    return options


options = get_arguments
scan_result=scan(options.target)
print_result(scan_result)