import json
from lystener import logMsg

def logSomething(data):

	logMsg('Transaction from darktoons sent :\n%s' % json.dumps(data, indent=2))
	return json.dumps({"success": True, "darktoons": "forever"})