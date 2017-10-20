import cisco

with open("running-config.cfg",'r') as current:
	 change_line =  current.read()
current.closed()

reload_file= re.sub(" ip address 172\." , " ip address 192\.", change_line )

with open("running-config.cfg", 'r') as update:
       change_line =  update.read()
update.closed()
