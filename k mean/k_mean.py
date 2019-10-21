from math import sqrt
import random
import visualise as vs
def calculateCentroid(C):
    x = 0
    y = 0
    l = len(C.x)
    data = zip(C.x,C.y)
    for pts in data:
        x+=pts[0]
        y+=pts[1]

    return [x/l,y/l]

def euclidian_dist(p1,p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

dataSet = []
with open("./data/data.csv","r") as f:
    data = f.readlines()
    for pt in data[1:]:
        pt = pt.strip().split(',')
        dataSet.append([float(pt[0]),float(pt[1])])

c1 = pc1 = random.choice(dataSet)
c2 = pc2 = random.choice(dataSet)
c3 = pc3 = random.choice(dataSet)

#k mean algo
class C:
    x = []
    y = []
    def reset(self):
        self.x = []
        self.y = []
C1 = C()
C2 = C()
C3 = C()
for _ in range(10):
    C1.reset()
    C2.reset()
    C3.reset()
    for pts in dataSet:
        # Find the eucledian distance between all points to the centroid

        d_to_c1 = euclidian_dist(c1,pts)
        d_to_c2 = euclidian_dist(c2,pts)
        d_to_c3 = euclidian_dist(c3,pts)
        p2 =1
        p3 =2

        if (d_to_c1<d_to_c2):
            d_to_c2 = d_to_c1
            p2 = 0

        if (d_to_c3>d_to_c2):
            d_to_c3 = d_to_c2
            p3 = p2

        if(p3 == 0):
            C1.x.append(pts[0])
            C1.y.append(pts[1])
        elif(p3==1):
            C2.x.append(pts[0])
            C2.y.append(pts[1])
        else:
            C3.x.append(pts[0])
            C3.y.append(pts[1])
            

        
        c1 = calculateCentroid(C1) if C1.x !=[] else c1 
        c2 = calculateCentroid(C2) if C2.x !=[] else c2
        c3 = calculateCentroid(C3) if C3.x !=[] else c3

        if (c1==pc1 and c2==pc2  and c3==pc3):
            break



# with open("./data/c1.csv","w") as f:
#     f.write("x,y,class\n")
#     for pt in C1:
#         f.write("{},{},{}\n".format(pt[0],pt[1],1))

# with open("./data/c2.csv","w") as f:
#     f.write("x,y,class\n")
#     for pt in C2:
#         f.write("{},{},{}\n".format(pt[0],pt[1],1))

# with open("./data/c3.csv","w") as f:
#     f.write("x,y,class\n")
#     for pt in C3:
#         f.write("{},{},{}\n".format(pt[0],pt[1],1))
# print(len(C1.x),len(C2.x),len(C3.x))
vs.visualise(C1,C2,C3)