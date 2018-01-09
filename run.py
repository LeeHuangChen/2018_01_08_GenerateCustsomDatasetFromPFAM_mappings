import Functions as func

def FamilyArr():
	families=[]
	
	families.append("Neur_chan_memb")
	families.append("Cu_amine_oxidN3")
	families.append("RNA_pol_Rpb2_1")
	families.append("TetR_N")
	families.append("KOW")
	families.append("Pkinase_Tyr")
	#families.append("")
	return families

def main():
	#create the family to arr dict
	#func.CreateFamilyToArrDict()

	
	func.GenerateBorderMappingsForGivenFamilies(FamilyArr())

if __name__ == '__main__':
	main()