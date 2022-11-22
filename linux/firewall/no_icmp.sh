#!/bin/sh
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -F INPUT
iptables -F OUTPUT
iptables -F FORWARD
iptables -F -t nat
iptables -F -t mangle


iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -s 192.168.0.0/24 -j ACCEPT
# example how to allow whole IP network 192.168.0.xxx
iptables -A INPUT -s 193.167.100.97 -j ACCEPT
# DO NOT COMMENT OR MODIFY THIS. THIS IS BACKDOOR TO YOUR SERVER FROM students.oamk.fi

iptables -A INPUT -p tcp --dport 22 -j ACCEPT
# DO NOT COMMENT OR MODIFY THIS. YOU WILL KICK YOURSELF OUT FROM THE SERVER (SSH)
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
# HTTP

iptables -A INPUT -p ALL -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

iptables -A INPUT -p ALL -m conntrack --ctstate NEW,INVALID -j DROP
iptables -A INPUT -p ALL -j DROP

iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD DROP



ip6tables -P INPUT DROP
ip6tables -P OUTPUT ACCEPT
ip6tables -P FORWARD DROP
ip6tables -F INPUT
ip6tables -F OUTPUT
ip6tables -F FORWARD

ip6tables -A INPUT -i lo -j ACCEPT
ip6tables -A INPUT -p TCP --dport 22
ip6tables -A INPUT -m state --state  ESTABLISHED,RELATED -j ACCEPT
ip6tables -A INPUT -p icmpv6 -j ACCEPT # ICMP6  autoconfig etc router advertisements
ip6tables -A INPUT -j DROP

ip6tables -P INPUT ACCEPT
ip6tables -P OUTPUT ACCEPT
ip6tables -P FORWARD DROP


#disable ICMP
iptables -A INPUT -p icmp -j DROP
ip6tables -A INPUT -p icmp -j DROP