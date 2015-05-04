#IMPORTS
import zipfile
import argparse
from threading import Thread

#FONCTIONS
#
def testPassword(zFile, password, verbosity):
	try:
		zFile.extractall(pwd=password)
		print '[+] Success with password = ' + password + '\n'
	except :
		if verbosity:
			print 'Fail with password = ' + password + '\n'
		pass
#
def main():	

	#Defining args
	parser = argparse.ArgumentParser()
	parser.add_argument("zname", help="specify zip file")
	parser.add_argument("dname", help="specify dictionary file")
	parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
	
	#Check if args are given
	args = parser.parse_args()
	if (args.zname == None) | (args.dname == None):
		print parser.usage
		exit(0)
	else:
		zname = args.zname 
		dname = args.dname
		verbosity = args.verbose

	print 'Intialisation...'
	
	zFile = zipfile.ZipFile(zname)
	dictionary = open(dname)

	for line in dictionary.readlines():
		password = line.strip('\n')
		thread = Thread(target=testPassword, args=(zFile, password, verbosity))
		thread.start()
			
#Proper Launcher
if __name__ == '__main__':
	main()