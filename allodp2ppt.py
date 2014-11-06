#!/usr/bin/python
import os
import fnmatch
import argparse


pattern = '*.odp'
searchpath = '/home/supportstick/pr/Scientific/'
unoconvPath = '/home/steffen/src/unoconv/unoconv'
overwrite=False

parser = argparse.ArgumentParser(description='Batch convert new or changed odp files to ppt and pdf')
parser.add_argument('-f', action='store_true', default=False, help='force overwrite existing files')
args = parser.parse_args()
overwrite = args.f

for root, dirnames, filenames in os.walk(searchpath):
	for filename in fnmatch.filter(filenames, pattern):
		filename = os.path.join(root, filename)
		#PowerPoint Version
		if not (os.path.exists(os.path.splitext(filename)[0]+'.ppt')) or (overwrite):
			print "generating: "+ os.path.splitext(filename)[0]+'.ppt'
			os.popen(unoconvPath+' -f ppt -o "'+root+'" "'+filename+'"')
		else:
			if os.path.getmtime(os.path.splitext(filename)[0]+'.ppt') < os.path.getmtime(os.path.splitext(filename)[0]+'.odp'):
				print "updating: "+ os.path.splitext(filename)[0]+'.ppt'
				os.popen(unoconvPath+' -f ppt -o "'+root+'" "'+filename+'"')
		# PDF Version
		if not (os.path.exists(os.path.splitext(filename)[0]+'.pdf')) or (overwrite):
			os.popen(unoconvPath+' -f pdf -o "'+root+'" "'+filename+'"')
			print "generating: "+ os.path.splitext(filename)[0]+'.pdf'
		else:
			if os.path.getmtime(os.path.splitext(filename)[0]+'.pdf') < os.path.getmtime(os.path.splitext(filename)[0]+'.odp'):
				print "updating: "+ os.path.splitext(filename)[0]+'.pdf'
				os.popen(unoconvPath+' -f pdf -o "'+root+'" "'+filename+'"')
		# PNG Version
		if not (os.path.exists(os.path.splitext(filename)[0]+'.png')) or (overwrite):
			os.popen(unoconvPath+' -f png -o "'+root+'" "'+filename+'"')
			print "generating: "+ os.path.splitext(filename)[0]+'.png'
		else:
			if os.path.getmtime(os.path.splitext(filename)[0]+'.png') < os.path.getmtime(os.path.splitext(filename)[0]+'.odp'):
				print "updating: "+ os.path.splitext(filename)[0]+'.png'
				os.popen(unoconvPath+' -f png -o "'+root+'" "'+filename+'"')
