# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os

'''search all fils under given dir'''
def walk(directory):
	for path, dirs, files in os.walk(directory):
		for f in files:
			print os.path.join(path, f)

#--------------------------------------------------------------------
if __name__ == '__main__':
	walk(os.getcwd())