#!/usr/bin/python
from __future__ import print_function
from pyPdf import PdfFileWriter, PdfFileReader
import fnmatch
import os
import argparse



def main():
	parser = argparse.ArgumentParser(description='Join pdf files')
	parser.add_argument('slidelist', help='filename of the file containing the slide numbers')
	parser.add_argument('slideDBdirectory', help='directory containing the pdfs')

	args = parser.parse_args()
	
	joinPDF(args.slidelist, args.slideDBdirectory)

def append_pdf(input,output):
	[output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

def joinPDF (slidelist, slideDBdirectory):
	slideDB = os.path.abspath(slideDBdirectory)	
	output = PdfFileWriter()
	excludes=['']
	if os.path.exists(os.path.join(os.path.dirname(slidelist),'exclude.txt')):
		excludes = [exclude.strip() for exclude in open(os.path.join(os.path.dirname(slidelist),'exclude.txt'))]
		# remove commented out excludes
		excludes = [exclude for exclude in excludes if not exclude.startswith('#')]
	slides = [slide.strip()+'.pdf' for slide in open(slidelist)]
	# remove commented out slides
	slides = [slide for slide in slides if not slide.startswith('#')]
	slideFiles = []
	i=1
	log = open(os.path.splitext(slidelist)[0]+'.log', 'w')
	for slide in slides:
		for root, dirnames, filenames in os.walk(slideDB, topdown=True):
			dirnames[:] = [dirname for dirname in dirnames if dirname not in excludes]
			for filename in fnmatch.filter(filenames, slide):
				print(i, filename, dirname, root, file=log)
				i=i+1
				slideFiles.append(os.path.join(root, filename))

	for slideFile in slideFiles:
		append_pdf(PdfFileReader(file(slideFile,"rb")),output)

	outputFileName=os.path.splitext(slidelist)[0]+'.pdf'
	output.write(file(outputFileName,"wb"))

if __name__ == '__main__':
	main()