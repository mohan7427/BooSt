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

  import json #Convert dict to json package

  f = open('/root/storage/ui/json_data_mixed')
  data = json.load(f)

  #Fetch desired data in dictionary
  ui_data={}
  for i in range(len(data['jobs'])):
    ui_data[data['jobs'][i]['jobname']]={}
    ui_data[data['jobs'][i]['jobname']]['bs']=data['jobs'][i]['job options']['bs']
    ui_data[data['jobs'][i]['jobname']]['iodepth']=data['jobs'][i]['job options']['iodepth']

    if 'read' in data['jobs'][i]['job options']['rw'] or 'randread' in data['jobs'][i]['job options']['rw']:
        ui_data[data['jobs'][i]['jobname']]['bw']=data['jobs'][i]['read']['bw']
        ui_data[data['jobs'][i]['jobname']]['iops']=data['jobs'][i]['read']['iops']
        ui_data[data['jobs'][i]['jobname']]['lat_ns']=data['jobs'][i]['read']['lat_ns']['mean']

    elif 'write' in data['jobs'][i]['job options']['rw'] or 'randwrite' in data['jobs'][i]['job options']['rw']:
        ui_data[data['jobs'][i]['jobname']]['bw']=data['jobs'][i]['write']['bw']
        ui_data[data['jobs'][i]['jobname']]['iops']=data['jobs'][i]['write']['iops']
        ui_data[data['jobs'][i]['jobname']]['lat_ns']=data['jobs'][i]['write']['lat_ns']['mean']

    elif 'rw' in data['jobs'][i]['job options']['rw'] or 'readwrite' in data['jobs'][i]['job options']['rw'] or 'randrw' in data['jobs'][i]['job options']['rw']:
        ui_data[data['jobs'][i]['jobname']]['bw']=(int(data['jobs'][i]['read']['bw'])+int(data['jobs'][i]['write']['bw']))/2
        ui_data[data['jobs'][i]['jobname']]['iops']=(float(data['jobs'][i]['read']['iops'])+float(data['jobs'][i]['write']['iops']))/2
        ui_data[data['jobs'][i]['jobname']]['lat_ns']=(float(data['jobs'][i]['read']['lat_ns']['mean'])+float(data['jobs'][i]['write']['lat_ns']['mean']))/2






  f.close()

  #Convert dict data to json
  js = json.dumps(ui_data, indent = 4)
  iops=[]
  iodepth=[]
  bs=[]
  bw=[]
  lat_ns=[]
  bw=[]
  seq_write_iops=[]
  seq_write_iodepth=[]
  seq_write_bs=[]
  seq_write_bw=[]
  seq_write_lat_ns=[]
  seq_write_bw=[]
  for i in ui_data:
    if 'seq_read' in i:
      bs.append(ui_data[i]['bs'])
      iops.append(ui_data[i]['iops'])
      lat_ns.append(ui_data[i]['lat_ns']/1000)
      iodepth.append(ui_data[i]['iodepth'])
      bw.append(ui_data[i]['bw'])
      job_name=i

    elif 'seq_write' in i:
      seq_write_bs.append(ui_data[i]['bs'])
      seq_write_iops.append(ui_data[i]['iops'])
      seq_write_lat_ns.append(ui_data[i]['lat_ns']/1000)
      
  import random
  get_colors = lambda n: ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(n)]
  get_colors=get_colors(len(bs))

  return render(request , 'graph2.html' , {'data_json': data_json, 'js':ui_data, 'seq_read_iops': iops, 'seq_read_iodepth': iodepth, 'seq_read_bs': bs, 'seq_read_bw': bw, 'seq_read_lat_ns': lat_ns, 'seq_read_bw': bw, 'get_colors': get_colors, 'job_name': job_name, 'seq_write_bs': seq_write_bs, 'seq_write_iops': seq_write_iops, 'seq_write_lat_ns': seq_write_lat_ns})

def job_execution(request):
    return render(request , 'job_execution.html' , {'data_json': '123'})
