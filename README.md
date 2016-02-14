# pcontroller v0.1

### Description: 

A python useful tool for system administrators and malicious persons :).

It allows you to run scheduled jobs on a remote server via github. Once launched on the remote server, it continuously retrieves python modules to be run together with the scheduling of them from a github repository and executes them at run-time without having to re-launch the tool.

### How to use:

1) Install python 2.7

2) Install the tool dependencies: github3.py - Release v1.0.0a2 (https://github3.readthedocs.org/en/develop/)

3) Download the following folders from this project and load them on your github repository: 

     3.1) config/ : it contains the configuration file that lists all the modules that can be executed by the tool.
     
     3.2) cmd/ : it contains modules that the tool should run and the scheduling of them.
     
     3.3) data/ : it will contain the output of the execution of the modules.
     
     3.4) modules/: it contains the python modules that are to be retrieved at runtime by the tool and executed as scheduled in cmd.

4) Download the Code/ folder on the server

5) Change the "pcontroller_constants.py" file and enter your information (editable section).

6) Run the tool: python pcontroller_main.py

### Additional Information

#### 1) Create a module:

 1.1) Change the "config.json" file and enter a new "module" attribute with the module name at the end of the json file. 
      Example:
      
      [
        {
          "module": "bash_who"
        },
        {
          "module": "bash_ls"
        },
        {
          "module": "bash_ps"
        },
        {
          "module" : "new_module_name"
        }
      ]
      
  1.2) Create the module "new_module_name.py" inside the modules/ folder and create a function named "run" that does something. 
       Example: "new_module_name.py"
       
       def run(**args):
        	...
        	
  1.3) Push the updates on your repository

#### 2) Scheduling a new module execution:

  2.1) Change the "cmd.json" and enter the name of module to be executed and how many seconds should be run.
       Example:
       
       [
      	{
      		"module" : "bash_who",
      		"when" : "30"
      	}
      ]

      It will run the bash_who.py module every 30 seconds.
      WARNING: The module must have been previously created! (See point 1)
      
  2.2) Push the updates on your repository
  
  2.3) The tool will run the module at the appointed time and will save the results in the data/ folder without any need to relaunch it.
  
#### References: "Black Hat Python: Python Programming for Hackers and Pentesters"
