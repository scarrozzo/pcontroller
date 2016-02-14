import subprocess

def run(**args):
	print "[*] In bash_ps.py module";
	proc = subprocess.Popen(["ps -ef"], stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()
	return (out,err);