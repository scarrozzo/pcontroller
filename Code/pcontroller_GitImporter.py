import base64
import imp
import sys

from pcontroller_Git import Git
import pcontroller_constants

class GitImporter(object):

	def __init__(self):
		self.current_module_code = "";
		self.gitConnection = Git();

	def find_module(self, fullname, path=None):
		if pcontroller_constants.PCONFIGURED:
			print("[*] Attempting to retrieve %s" % fullname);
			new_library = self.gitConnection.get_file_contents("modules/%s" % fullname);
			if new_library is not None:
				self.current_module_code = base64.b64decode(new_library);
				return self;
		return None;

	def load_module(self, name):
		module = imp.new_module(name);
		exec(self.current_module_code, module.__dict__);
		sys.modules[name] = module;
		return module;