import subprocess

def run(**args):
	print "[*] In bash_ls.py module";
	proc = subprocess.Popen(["ls"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	return (out,err);