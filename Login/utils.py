def SetUserData(Data=[]):
	global GlobalData
	if Data:
		GlobalData["UserName"]=Data[0]
		GlobalData["Id"]=Data[1]
	else:GlobalData={}
