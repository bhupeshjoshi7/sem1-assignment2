name = "Bhupesh Joshi" 
SID = str(22106051)
Dpt = "Data Science"
cg = str(9.9)

dis = "Hey, ABC Here. My SID is sid. I am from XYZ department and my CGPA is cg"
dis =dis.replace("ABC",name)
dis =dis.replace("XYZ",Dpt)
dis =dis.replace("sid",SID)
dis =dis.replace("cg",cg)
print(dis)
