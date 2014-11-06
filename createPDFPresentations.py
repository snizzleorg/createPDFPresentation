
#!/usr/bin/python
import fnmatch
import os
import createPDFPresentation

talksDir ='/home/supportstick/pr/Scientific/talks'
dbDir='/home/supportstick/pr/Scientific/folienDB/'

for root, dirnames, filenames in os.walk(talksDir):
	for filename in fnmatch.filter(filenames, '*.txt'):
		if filename != 'exclude.txt' and filename != 'README.txt': 
			if not os.path.exists(os.path.join(root,os.path.splitext(filename)[0]+'.pdf')):
				print "generating " + os.path.splitext(filename)[0]+'.pdf'
				createTalk.joinPDF(os.path.join(root, filename),dbDir)					
			else:
				if os.path.getmtime(os.path.join(root,os.path.splitext(filename)[0]+'.pdf')) < os.path.getmtime(os.path.join(root,os.path.splitext(filename)[0]+'.txt')):
					print "updating " + os.path.splitext(filename)[0]+'.pdf'
					createTalk.joinPDF(os.path.join(root, filename),dbDir)