"""Latency and throughput measurement profile for Gaggle server. 

Instructions:
SSH into each node and `cd /local/repository`. If on the server node, run 
`./setup_server.sh` to install relevant packages and start the server 
in the newly-created tmux session with `node index.js`. If on a client node,
run `./setup_client.sh` to install relevant packages. To run the client 
(also in a newly-created tmux session) with the default options, run 
`node index.js`. To see the configurable options, run `node index.js -h`. 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the emulab extensions library.
import geni.rspec.emulab

# Describe the parameter(s) this profile script can accept.
portal.context.defineParameter( "numClients", "Number of clients", portal.ParameterType.INTEGER, 1 )
#portal.context.defineParameter( "baseIP", "IP address of server node", portal.ParameterType.STRING, "192.168.1." )
portal.context.defineParameter( "HW", "Type to hardware to request", portal.ParameterType.STRING, "c220g5" )
portal.context.defineParameter( "DI", "Disk Image", portal.ParameterType.STRING, "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD" )

# Retrieve the values the user specifies during instantiation.
params = portal.context.bindParameters()

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()

ifaces = []
site = "site"

# Setup LAN
lan = request.LAN("lan")
# bandwidth in Kbps
#lan.bandwidth = 100000
# latency in ms
#lan.latency = 10
# packet loss rate is: 0.0 <= loss <= 1.0
#lan.plr = 0.05

# Server node
node_server = request.RawPC("node_server")
node_server.hardware_type = params.HW
node_server.disk_image = params.DI
#node_server.addService(pg.Execute(shell="sh", command="/local/repository/setup_server.sh"))

# Add server node to LAN
node_server.Site(site)
server_iface = node_server.addInterface("iface0") #"eth1"
#server_iface.addAddress(pg.IPv4Address(params.baseIP + "0", "255.255.255.0"))
lan.addInterface(server_iface)

for i in range(1, params.numClients + 1):
    # Client node
    node_client = request.RawPC("node_client" + str(i))
    node_client.hardware_type = params.HW
    node_client.disk_image = params.DI
    #node_client.addService(pg.Execute(shell="sh", command="/local/repository/setup_client.sh"))

    # Add client node to LAN
    node_client.Site(site)
    client_iface = node_client.addInterface("iface" + str(i)) #"eth1"
    #client_iface.addAddress(pg.IPv4Address(params.baseIP + str(i), "255.255.255.0"))
    lan.addInterface(client_iface)

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
