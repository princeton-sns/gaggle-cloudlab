"""Latency and throughput measurement profile for Gaggle server. 

Instructions:
Log into each node, the repository is mounted at `/local/noise`.
The number of nodes and hardware type are parameterized so you can 
configure based on availability and need. Once instantiated, `cd /local/noise`.
Start the server with `node index.js`. Configurable client options can be seen 
by running `node index.js -h`. Then start each client with `node index.js [options]`.
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

#ifaces = []
#site = "site"

# Setup LAN
#lan = request.LAN("lan")
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
node_server.addService(pg.Execute(shell="sh", command="/local/repository/cloudlab_server_setup.sh"))

# Add server node to LAN
#node_server.Site(site)
#server_iface = node_server.addInterface("eth1")
##server_iface.addAddress(pg.IPv4Address(params.baseIP + "0", "255.255.255.0"))
#lan.addInterface(server_iface)

for i in range(1, params.numClients + 1):
    # Client node
    node_client = request.RawPC("node_client" + str(i))
    node_client.hardware_type = params.HW
    node_client.disk_image = params.DI
    node_client.addService(pg.Execute(shell="sh", command="/local/repository/cloudlab_client_setup.sh"))

    # Add client node to LAN
    #node_client.Site(site)
    #client_iface = node_client.addInterface("eth1")
    ##client_iface.addAddress(pg.IPv4Address(params.baseIP + str(i), "255.255.255.0"))
    #lan.addInterface(client_iface)

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
