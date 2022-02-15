#NAPALM

#Network automation and programmability abstraction layer with multivendoer support
#This code extracts basic device information using get facts function on Cisco devices



from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.122.72', 'arjun', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print ios_output