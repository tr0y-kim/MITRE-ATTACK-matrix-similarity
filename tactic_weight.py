import json
import glob
from itertools import combinations

from numpy import dot
from numpy.linalg import norm
import numpy as np


tactic1 = ['T1189','T1190','T1133','T1200','T1566','T1091','T1195','T1199','T1078'] # 9 techniquess
tactic2 = ['T1059','T1203','T1559','T1106','T1053','T1129','T1072','T1569','T1204','T1047']
tactic3 = ['T1098','T1197','T1547','T1037','T1176','T1554','T1136','T1543','T1546','T1133','T1574','T1525','T1137','T1542','T1053','T1505','T1205','T1078']
tactic4 = ['T1548','T1134','T1574','T1037','T1543','T1484','T1546','T1068','T1574','T1055','T1053','T1078']
tactic5 = ['T1548','T1134','T1194','T1140','T1006','T1484','T1480','T1211','T1222','T1564','T1574','T1562','T1070','T1202','T1036','T1556','T1578','T1112','T1601','T1599','T1027','T1542','T1055','T1207','T1014','T1218','T1216','T1553','T1221','T1205','T1127','T1535','T1550','T1078','T1497','T1600','T1220']
tactic6 = ['T1110','T1555','T1212','T1187','T1606','T1056','T1557','T1556','T1040','T1003','T1528','T1558','T1539','T1111','T1552']
tactic7 = ['T1087','T1010','T1217','T1580','T1538','T1526','T1482','T1083','T1046','T1135','T1040','T1201','T1120','T1069','T1057','T1012','T1018','T1518','T1082','T1016','T1049','T1033','T1007','T1124','T1497']
tactic8 = ['T1210','T1534','T1570','T1563','T1021','T1091','T1072','T1080','T1550']
tactic9 = ['T1560','T1123','T1119','T1115','T1530','T1602','T1213','T1005','T1039','T1025','T1074','T1114','T1056','T1185','T1557','T1113','T1125']
tactic10 = ['T1071','T1092','T1132','T1001','T1568','T1573','T1008','T1105','T1104','T1095','T1571','T1572','T1090','T1219','T1205','T1102']
tactic11 = ['T1020','T1030','T1048','T1041','T1011','T1052','T1567','T1029','T1537']
tactic12 = ['T1531','T1485','T1486','T1565','T1491','T1561','T1499','T1495','T1490','T1498','T1496','T1489','T1529']

# given ==> tactic1 ~ tactic12
def vectorize(tactic, given):
	vector = [0] * len(given)
	idx = 0
	for i in given:
		try:
			a = tactic.index(i)
			vector[idx] = vector[idx] + 1
		except:
			pass
		idx = idx + 1
	return vector

def cos_sim(A, B):
       return dot(A, B)/ (norm(A)*norm(B))


json_file_path = '*.json'

APT_all = []
for filename in glob.glob(json_file_path):
    # Each Json Loaded
    print("[+]" + filename)
    APT_vector = []
    APT_techID = []
    with open(filename, 'r') as f:
        j = f.read()
        json_object = json.loads(j)
        tech_list = json_object["techniques"]
        
        for i in tech_list:
        	APT_techID.append(i["techniqueID"])
        #print(APT_techID)
        APT_vector.append(vectorize(APT_techID,tactic1))
        APT_vector.append(vectorize(APT_techID,tactic2))
        APT_vector.append(vectorize(APT_techID,tactic3))
        APT_vector.append(vectorize(APT_techID,tactic4))
        APT_vector.append(vectorize(APT_techID,tactic5))
        APT_vector.append(vectorize(APT_techID,tactic6))
        APT_vector.append(vectorize(APT_techID,tactic7))
        APT_vector.append(vectorize(APT_techID,tactic8))
        APT_vector.append(vectorize(APT_techID,tactic9))
        APT_vector.append(vectorize(APT_techID,tactic10))
        APT_vector.append(vectorize(APT_techID,tactic11))
        APT_vector.append(vectorize(APT_techID,tactic12))
        go = (filename,APT_vector)  
    APT_all.append(go)

print(APT_all[0][1][0])


nums = list(range(len(APT_all)))
nums_list = list(combinations(nums, 2))   # [(1,2),(1,3)]

#for n in range(12):
sim_list = []
a = 0
for (i,j) in nums_list:
    a = a+1
    
    doc1=np.array(APT_all[i][1][11]) #[i][1][0] for initial acce
    doc2=np.array(APT_all[j][1][11])
    
    
    sim_list.append(cos_sim(doc1, doc2))
avg = np.nansum(sim_list) / np.count_nonzero(~np.isnan(sim_list))
print(avg)
print(len(sim_list))

