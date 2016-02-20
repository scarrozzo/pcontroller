import sys
import threading
import time

import pcontroller_constants
from pcontroller_Git import Git
from pcontroller_GitImporter import GitImporter

pcontroller_id = pcontroller_constants.PCONTROLLER_ID
jobs = {}

# general purpose function for modules
def module_runner(module):
	result = sys.modules[module].run();
	gitConnection.store_module_result(result, pcontroller_id, "Auto commit message", module);
	del jobs[module];
	return 


#main
sys.meta_path = [GitImporter()];

gitConnection = Git();
gitConnection.import_modules(pcontroller_constants.PCONFIG);
cmd = gitConnection.get_cmd(pcontroller_constants.PCOMMANDS);

while True:
	cmd = gitConnection.get_cmd(pcontroller_constants.PCOMMANDS);
	for command in cmd:
		if "module" in command and "when" in command:
			if not command["module"] in jobs:
				jobs[command["module"]] = True;
				threading.Timer(int(command["when"]), module_runner, [command['module']]).start();
	time.sleep(1);