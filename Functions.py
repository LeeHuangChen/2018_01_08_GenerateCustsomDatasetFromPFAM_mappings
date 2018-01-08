import Configurations as conf
from cPickle import dump, load
import util
import os

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
	print "Adding information to dictionary..."
	util.progressbarGuide(20)
	for i, line in enumerate(mappingLines):
		util.progressbar(i, len(mappingLines),20)

		if len(line)>0:
			#format:
			#0      1           2               3               4           5           6           7
			#PDB_ID	CHAIN_ID	PdbResNumStart	PdbResNumEnd	PFAM_ACC	PFAM_Name	PFAM_desc	eValue
			arr=line.split("\t")
			fName=arr[5]
			if fName in FamToArrDict.keys():
				FamToArrDict[fName].append(arr)
			else:
				FamToArrDict[fName]=[arr]

	print "Sorting infomation inside dictionary..."
	util.progressbarGuide(10)
	famNames=FamToArrDict.keys()
	for i, famName in enumerate(famNames):
		util.progressbar(i,len(famNames),10)
		FamToArrDict[famName].sort(key=lambda x:x[0])
	
	#dump the dictionary to disc
	with open(conf.FamToArrDictLoc,"wb") as f:
		dump(FamToArrDict,f)

#assumes FamilyToArr dict is generated
def GenerateBorderMappingsForGivenFamily(famName):
	#generate the result folder
	util.generateDirectoriesMult([conf.ResultFolder])

	#import the FamToArrDict
	with open(conf.FamToArrDictLoc,"rb") as f:
		FamToArrDict=load(f)

	#print FamToArrDict.keys()

	borderMapping=FamToArrDict[famName]

	#create output file
	outfiledir=os.path.join(conf.ResultFolder,famName+".txt")
	with open(outfiledir,"w") as f:
		f.write("PDB_ID\tPdbResNumStart\tPdbResNumEnd\teValue\tPFAM_ACC\n")


	write=""
	counter=0
	for arr in borderMapping:
		#format:
		#0      1           2               3               4           5           6           7
		#PDB_ID	CHAIN_ID	PdbResNumStart	PdbResNumEnd	PFAM_ACC	PFAM_Name	PFAM_desc	eValue

		line=arr[0]+'\t'+arr[2]+'\t'+arr[3]+'\t'+arr[7]+'\t'+arr[4]+"\n"
		write+=line
		counter+=1
		if counter>=100:
			with open(outfiledir,"a") as f:
				f.write(write)
				write=""
				counter=0
	with open(outfiledir,"a") as f:
		f.write(write)
		write=""

#assumes FamilyToArr dict is generated
def GenerateBorderMappingsForGivenFamilies(famNameArr):
	for famName in famNameArr:
		GenerateBorderMappingsForGivenFamily(famName)


def main():
	print "main function currently not programmed"

if __name__ == '__main__':
	main()