with open('raw_data') as f:
    lines=f.readlines()

for i, line in enumerate(lines):
   if line.startswith('         tod'):
             version = line.strip()
             date = lines[i + 3].strip()
             #print(line,date)
             print(lines[(i+1)::])
             data=lines[(i+1)::]
data_json={}
data_json['timestamp']=[]
data_json['cpu_used']=[]
data_json['cpu_user']=[]
data_json['cpu_kernel']=[]
data_json['cpu_wait']=[]
data_json['cpu_idle']=[]
timestamp=cpu_used=cpu_user=cpu_kernel=cpu_wait=cpu_idle=[]
for i in data:
    i=i.split(' ')
    print("I",i)
    data_json['timestamp'].append(i[1])
    data_json['cpu_used'].append(i[29])
    data_json['cpu_user'].append(i[30])
    data_json['cpu_kernel'].append(i[31])
    data_json['cpu_wait'].append(i[32])
    data_json['cpu_idle'].append(i[33])

print("JSON",data_json)
