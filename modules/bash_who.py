import subprocess

def run(**args):
	print "[*] In bash_who.py module";
	proc = subprocess.Popen(["who"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	return (out,err);