# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re

def match(text):
	m = re.match(r"\w+\.py", text)
	return bool(m)

#--------------------------------------------------------------------
if __name__ == '__main__':
	print match('123.py')