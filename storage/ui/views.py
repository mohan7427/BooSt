from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def graph(request):
  return render(request , 'graph.html' , {})

def graph2(request):
  with open('/root/storage/ui/raw_data') as f:
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
    data_json['cpu_user'].append(float(i[30]))
    data_json['cpu_kernel'].append(float(i[31]))
    data_json['cpu_wait'].append(float(i[32]))
    data_json['cpu_idle'].append(float(i[33]))

  print("JSON",data_json)

  return render(request , 'graph2.html' , {'data_json': data_json})

def job_execution(request):
    return render(request , 'job_execution.html' , {'data_json': '123'})
