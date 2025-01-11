bString = "02020a03070a03060a040b0a03040a040f0a01010a01050a1428321e28321e323c324646283c463c50500a141e0a1e28"
bString = bString.replace(" ", "")
print(bString)
n=2 #byte length
bList = [bString[i:i+n] for i in range(0, len(bString), n)]
bList = [int(bList[i], 16) for i in range(0, len(bList))]

print(len(bList))

iLength = 2
jLength = 4
kLength = 2
lLength = 3
mLength = 0

# 2 dimensions
#finalList = [[bList[j + i*jLength] for j in range(0,jLength)] for i in range(0, iLength)]

# 3 dimensions
#finalList = [[[bList[k + j*kLength + i*kLength*jLength] for k in range(0,kLength)] for j in range(0,jLength)] for i in range(0, iLength)]

# 4 dimensions
finalList = [[[[bList[l + k*lLength + j*lLength*kLength + i*lLength*kLength*jLength] for l in range(0, lLength)] for k in range(0,kLength)] for j in range(0,jLength)] for i in range(0, iLength)]

#5 dimensions
#finalList = [[[[[bList[m + l*mLength + k*mLength*lLength + j*mLength*lLength*kLength + i*mLength*lLength*kLength*jLength] for m in range(0, mLength)] for l in range(0, lLength)] for k in range(0,kLength)] for j in range(0,jLength)] for i in range(0, iLength)]


print(finalList)

# floatData = [
#   ["Mario","807B84F8",-0.65,0.55,-0.2,1.5,-2.1,-1,0.05,1,0,0  ],
#   ["Luigi","807B851C",-0.65,0.65,0.3,1.9,-1.8,-1,0.05,1,0,1  ],
#   ["DK","807B8540",-0.55,0.65,0.4,1.4,-2.65,-1,0.05,1,1,2  ],
#   ["Diddy","807B8564",-0.55,0.55,-0.3,1.8,-1.7,-1,0.05,1,0,3  ],
#   ["Peach","807B8588",-0.75,0.5,0.1,1.5,-1.9,-1.3,0.05,1,0,4  ],
#   ["Daisy","807B85AC",-0.65,0.6,-0.2,1.6,-2,-1.3,0.05,1,0,5  ],
#   ["Yoshi","807B85D0",-0.65,0.65,0.2,1.5,-2.05,-1,0.05,1,0,6  ],
#   ["Baby Mario","807B85F4",-0.75,0.55,-0.5,1.7,-1.8,-1.3,0.05,1,0,7  ],
#   ["Baby Luigi","807B8618",-0.65,0.55,-0.1,1.8,-1.9,-1.15,0.05,1,0,8  ],
#   ["Bowser","807B863C",-0.55,1.45,0.1,0.2,-3.6,-1,0.05,1,0,9  ],
#   ["Wario","807B8660",-0.55,0.75,0.4,1.5,-2.4,-1.6,0.05,1,0,10  ],
#   ["Waluigi","807B8684",-0.55,0.85,0.3,1.5,-2.3,-1,0.05,1,0,11  ],
#   ["Koopa(R)","807B86A8",-0.5,0.55,-0.2,1.6,-2.15,-1,0.05,1,0,12  ],
#   ["Toad(R)","807B86CC",-0.95,0.55,-0.1,1.8,-1.7,-1,0.05,0.75,0,13  ],
#   ["Boo","807B86F0",-0.45,0.85,-0.1,1.6,-2.4,-1,0.05,1.1,0,14  ],
#   ["Toadette","807B8714",-0.65,0.5,-0.1,1.7,-1.8,-1,0.05,0.75,0,15  ],
#   ["Shy Guy(R)","807B8738",-0.55,0.65,-0.1,1.4,-2.5,-1,0.05,1,0,16  ],
#   ["Birdo","807B875C",-0.55,0.55,0.1,1.8,-1.9,-1,0.05,1,0,17  ],
#   ["Monty","807B8780",-0.55,0.85,0.3,1.4,-2.5,-1,0.05,1,0,18  ],
#   ["Bowser Jr","807B87A4",-0.65,0.65,0.2,1.4,-2.5,-1,0.05,1,0,19  ],
#   ["Paratroopa(R)","807B87C8",-0.55,0.65,-0.2,1.6,-2.2,-1,0.05,1,0,20  ],
#   ["Pianta(B)","807B87EC",-0.45,0.85,0.5,1.3,-2.3,-1,0.05,1,0,21  ],
#   ["Pianta(R)","807B8810",-0.45,0.85,0.5,1.3,-2.3,-1,0.05,1,0,22  ],
#   ["Pianta(Y)","807B8834",-0.45,0.85,0.5,1.3,-2.3,-1,0.05,1,0,23  ],
#   ["Noki(B)","807B8858",-0.65,0.65,0.1,1.4,-2,-1.2,0.05,1,0,24  ],
#   ["Noki(R)","807B887C",-0.65,0.65,0.1,1.4,-2,-1.2,0.05,1,0,25  ],
#   ["Noki(G)","807B88A0",-0.65,0.65,0.1,1.4,-2,-1.2,0.05,1,0,26  ],
#   ["Bro(H)","807B88C4",-0.65,0.65,-0.2,1.2,-1.7,-1,0.05,1,1,27  ],
#   ["Toadsworth","807B88E8",-0.65,0.55,-0.1,1.6,-1.75,-1,0.05,0.75,1,28  ],
#   ["Toad(B)","807B890C",-0.45,0.45,-0.6,1.2,-1.7,-1,0.05,0.75,0,29  ],
#   ["Toad(Y)","807B8930",-0.45,0.45,-0.6,1.2,-1.7,-1,0.05,0.75,0,30  ],
#   ["Toad(G)","807B8954",-0.45,0.45,-0.6,1.2,-1.7,-1,0.05,0.75,0,31  ],
#   ["Toad(P)","807B8978",-0.45,0.45,-0.6,1.2,-1.7,-1,0.05,0.75,0,32  ],
#   ["Magikoopa(B)","807B899C",-0.6,0.7,-0.2,1.5,-2,-1,0.05,1,0,33  ],
#   ["Magikoopa(R)","807B89C0",-0.6,0.7,-0.2,1.5,-2,-1,0.05,1,0,34  ],
#   ["Magikoopa(G)","807B89E4",-0.6,0.7,-0.2,1.5,-2,-1,0.05,1,0,35  ],
#   ["Magikoopa(Y)","807B8A08",-0.6,0.7,-0.2,1.5,-2,-1,0.05,1,0,36  ],
#   ["King Boo","807B8A2C",-0.65,0.65,-0.1,1.8,-2.3,-1,0.05,1.2,0,37  ],
#   ["Petey","807B8A50",-0.65,0.65,-0.2,1.2,-1.9,-1.4,0.05,1.1,0,38  ],
#   ["Dixie","807B8A74",-0.65,0.55,0.2,1.7,-1.6,-1,0.05,1.2,0,39  ],
#   ["Goomba","807B8A98",-0.55,0.55,0,1.5,-2.1,-1,0.05,0.75,0,40  ],
#   ["Paragoomba","807B8ABC",-0.55,0.55,-0.2,1.4,-2.3,-1,0.05,1,0,41  ],
#   ["Koopa(G)","807B8AE0",-0.5,0.55,-0.2,1.6,-2.15,-1,0.05,1,0,42  ],
#   ["Paratroopa(G)","807B8B04",-0.55,0.65,-0.2,1.6,-2.1,-1,0.05,1,0,43  ],
#   ["Shy Guy(B)","807B8B28",-0.55,0.65,-0.1,1.4,-2.5,-1,0.05,1,0,44  ],
#   ["Shy Guy(Y)","807B8B4C",-0.55,0.65,-0.1,1.4,-2.5,-1,0.05,1,0,45  ],
#   ["Shy Guy(G)","807B8B70",-0.55,0.65,-0.1,1.4,-2.5,-1,0.05,1,0,46  ],
#   ["Shy Guy(Bk)","807B8B94",-0.55,0.65,-0.1,1.4,-2.5,-1,0.05,1,0,47  ],
#   ["Dry Bones(Gy)","807B8BB8",-0.75,0.55,-0.1,1.3,-1.9,-1.1,0.05,1,0,48  ],
#   ["Dry Bones(G)","807B8BDC",-0.75,0.55,-0.1,1.3,-1.9,-1.1,0.05,1,0,49  ],
#   ["Dry Bones(R)","807B8C00",-0.75,0.55,-0.1,1.3,-1.9,-1.1,0.05,1,0,50  ],
#   ["Dry Bones(B)","807B8C24",-0.75,0.55,-0.1,1.3,-1.9,-1.1,0.05,1,0,51  ],
#   ["Bro(F)","807B8C48",-0.65,0.65,-0.2,1.2,-1.7,-1,0.05,1,1,52  ],
#   ["Bro(B)","807B8C6C",-0.65,0.65,-0.2,1.2,-1.7,-1,0.05,1,1,53  ]
# ]

# characterList = [floatData[i][0] for i in range(0, len(floatData))]
# print(characterList)

# addr = 0x807b8fb4
# addrList = [addr + 0x10 * i for i in range(0, len(floatData))]

# finalFinalList = []
# for i in range(0,len(characterList)):
#    finalFinalList.append([])
#    finalFinalList[i].append(characterList[i] +" Hitbox Scaler")
#    finalFinalList[i].append(hex(0x800e8300 + 8*i))
#    finalFinalList[i].append(1.2)
#    finalFinalList[i].append("float")
#    finalFinalList[i].append(0)
#    finalFinalList[i].append(10)
#    finalFinalList[i].append(0.01)

# print(finalFinalList)

# #["Mario Hitbox Scaler", "0x800e8300", 1.18, "float", 0, 10, 0.01],
