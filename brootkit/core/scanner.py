from brootkit.core.prints import print_info, print_error, print_table, table_success, table_error, Constant
from brootkit.core.utils import information
from brootkit.fnc.ntauth.ntauth import *

functions = {
	"elevate": (
		ntauth_info
	)
}

class scanner():
	def __init__(self, uac=True, persist=True, elevate=True):
		self.uac = uac
		self.persist = persist
		self.elevate = elevate
		Constant.output = []

	def start(self):
		print_info("Comparing build number ({buildnumber}) against 'Fixed In' build numbers".format(buildnumber=information().build_number()))
		print_table()
		for i in functions:
			if i == "uac" and not self.uac or i == "persist" and not self.persist or i == "elevate" and not self.elevate:
				continue

			for info in functions[i]:
				if int(info["Works From"]) <= int(information().build_number()) < int(info["Fixed In"]):
					table_success(id=info["Id"], type=info["Type"], description=info["Description"])
				else:
					table_error(id=info["Id"], type=info["Type"], description=info["Description"])
		return Constant.output

class function():
	def __init__(self, uac=True, persist=True, elevate=True):
		self.uac = uac
		self.persist = persist
		self.elevate = elevate
		Constant.output = []

	def run(self, id, payload, **kwargs):
		print_info("Attempting to run method ({id}) configured with payload ({payload})".format(id=id, payload=payload))
		for i in functions:
			if i == "uac" and not self.uac or i == "persist" and not self.persist or i == "elevate" and not self.elevate:
				continue

			for info in functions[i]:
				if id in str(info["Id"]):
					if int(info["Works From"]) <= int(information().build_number()) < int(info["Fixed In"]):
						f = globals()[info["Function Name"]]
						if "name" not in f.__code__.co_varnames and "add" in f.__code__.co_varnames:
							f(payload, add=kwargs.get("add", True))
						elif "name" in f.__code__.co_varnames and "add" in f.__code__.co_varnames:
							f(payload, name=kwargs.get("name", "WinPwnage"), add=kwargs.get("add", True))
						else:
							f(payload)
					else:
						print_error("Technique not compatible with this system.")
					return Constant.output
				else:
					pass