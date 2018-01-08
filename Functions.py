import Configurations as conf
from cPickle import dump
import util

#create the familyToArrDict
def CreateFamilyToArrDict():
	#create the generated folder
	util.generateDirectoriesMult([conf.GeneratedFolder])

	#import all the mapping lines excluding the header
	mappingLines=open(conf.mappingFile,"r").read().split("\n")[1:]

	#dictionary of lines from the mapping file
		#key: PFAM_ACC
		#val: arrays of arrays of values in the lines
	FamToArrDict={}
	util.progressbarGuide(20)
	for i, line in enumerate(mappingLines):
		util.progressbar(i, len(mappingLines),20)

		if len(line)>0:
			#format:
			#0      1           2               3               4           5           6           7
			#PDB_ID	CHAIN_ID	PdbResNumStart	PdbResNumEnd	PFAM_ACC	PFAM_Name	PFAM_desc	eValue
			arr=line.split("\t")
			acc=arr[4]
			if acc in FamToArrDict.keys():
				FamToArrDict[acc].append(arr)
			else:
				FamToArrDict[acc]=[arr]

	#dump the dictionary to disc
	with open(conf.FamToArrDictLoc,"wb") as f:
		dump(FamToArrDict,f)

def GenerateBorderMappingsForGivenFamily(famAcc):
	print 0

def main():
	print "main function currently not programmed"

if __name__ == '__main__':
	main()