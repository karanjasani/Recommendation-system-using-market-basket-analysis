import time

def frequentDoubles(tHold):

   dataset = "dataset/store_data.dat"

   tHold = float(tHold)

   myFile = open(dataset)

   pairsTable = {}

   lines = myFile.readlines()

   pairsTable = {}
   for line in lines:
       line = line.strip().rstrip('\n')
       #print(line)
       for item1 in line.split(','):
           #print(item1)
           for item2 in line.split(','):
               #print(item2)
               if (item1 < item2):
                   if (item1 +','+ item2) not in pairsTable:
                       pairsTable[item1 +','+ item2] = 1
                   else:
                       pairsTable[item1 +','+ item2] += 1

   ordered = {}
   for i in pairsTable:
       #print("ii--",triplesTable[i])
       if pairsTable[i] > len(lines) * tHold:
           #print("i-",i,"triplesTable-",triplesTable[i])
           ordered[i]=pairsTable[i]

   ordered = sorted(ordered.items(), key=lambda kv: kv[1], reverse=True)

   return ordered


def frequentTriples(tHold):

   dataset = "dataset/store_data.dat"

   tHold = float(tHold)

   myFile = open(dataset)

   triplesTable = {}

   lines = myFile.readlines()
   print("hi")
   for line in lines:
       line = line.strip().rstrip('\n')
       for item1 in line.split(','):
           for item2 in line.split(','):
               for item3 in line.split(','):
                   if (item1 < item2 and item2 < item3):
                       if (item1 +','+ item2 +','+ item3) not in triplesTable:
                           triplesTable[item1 +','+ item2 +','+ item3] = 1
                       else:
                           triplesTable[item1 +','+ item2 +','+ item3] += 1

   """
   ordered = []
   for i in triplesTable:
       if triplesTable[i] > (len(lines) * tHold):
           print(i)
           ordered.append([triplesTable[i], i])

   """

   tordered = {}
   for i in triplesTable:
        if triplesTable[i] > len(lines) * tHold:
            print("hi")
            tordered[i]=triplesTable[i]

   for k,v in sorted(tordered.items(), key=lambda kv: kv[1], reverse=True):
       print(k,v)

   tordered = sorted(tordered.items(), key=lambda kv: kv[1], reverse=True)

   return tordered
