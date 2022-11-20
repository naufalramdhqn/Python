import random 

nilai = set()
score = dict()

for i in range(5):
    br = random.randrange(1,51)
    nilai.add(br)
    
for i in range(5):
    value = random.randrange(100,1000)
    score.update({ i:value })
    
print(nilai)
print(score)