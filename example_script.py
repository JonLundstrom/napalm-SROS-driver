from napalm import get_network_driver

driver = get_network_driver("sros")
optional_args = {'port': 830}
device = driver("138.120.181.55", "netconf", "n37c0nf20", 60, optional_args)
device.open()
print(device.get_facts())
print(device.get_optics())
device.close()
