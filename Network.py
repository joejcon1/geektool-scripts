#! /usr/bin/python
import envoy

if __name__=='__main__':
	to = 2
	while True:
		r = envoy.run('netstat 1', timeout=to)
		res = r.std_out
		lines = res.split('\n')
		lines = lines[2:]
		sum = 0
		for row in lines:
			cols = row.split()
			if cols != []:
				outgoing = cols[2]
				sum += int(outgoing)
			
		average = sum / to
		kb = sum / 1024
		print str(kb) + 'KB/s' 


