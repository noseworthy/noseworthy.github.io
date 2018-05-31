import jnettools.toolselements.NetworkElement
import jnettools.tools.Routing
import jnettools.tools.RouteInspector

ne = jnettools.tools.elements.NetworkElement('171.0.2.45')
try:
    routing_table = ne.getRoutingTable()
except jnettools.tools.elements.MissingVar:
    logging.exception ('No routing table found')
    ne.cleanup('rollback')
else:
    num_routes = routing_tables.getSize()
    for RToffset in range(num_routes):
        route = routing_table.getRouteByIndex(RToffset)
        name = route.getName()
        ipaddr = route.getIPAddr()
        print "%15s -> %s"% (name,ipaddr)
finally:
    ne.cleanup('commit')
    ne.disconnect()
