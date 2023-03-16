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
#define list and dictionary elements
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
seq_randread_bs=[]
seq_randread_bw=[]
seq_randread_iops=[]
seq_randread_lat_ns=[]
seq_randwrite_bs=[]
seq_randwrite_bw=[]
seq_randwrite_iops=[]
seq_randwrite_lat_ns=[]
seq_read_32={}
seq_write_32={}
seq_randread_32={}
seq_randwrite_32={}
for i in ui_data:
    if 'seq_read' in i:
      bs.append(ui_data[i]['bs'])
      iops.append(ui_data[i]['iops'])
      lat_ns.append(ui_data[i]['lat_ns']/1000000)
      iodepth.append(ui_data[i]['iodepth'])
      bw.append(ui_data[i]['bw'])
      job_name=i
    elif 'seq_write' in i:
      seq_write_bs.append(ui_data[i]['bs'])
      seq_write_iops.append(ui_data[i]['iops'])
      seq_write_lat_ns.append(ui_data[i]['lat_ns']/1000000)
      seq_write_bw.append(ui_data[i]['bw'])
    elif 'seq_randread' in i:
      seq_randread_bs.append(ui_data[i]['bs'])
      seq_randread_iops.append(ui_data[i]['iops'])
      seq_randread_lat_ns.append(ui_data[i]['lat_ns']/1000000)
      seq_randread_bw.append(ui_data[i]['bw'])
    elif 'seq_randwrite' in i:
      seq_randwrite_bs.append(ui_data[i]['bs'])
      seq_randwrite_iops.append(ui_data[i]['iops'])
      seq_randwrite_lat_ns.append(ui_data[i]['lat_ns']/1000000)
      seq_randwrite_bw.append(ui_data[i]['bw'])
data_updated={}
data_updated['seq_read_32']={}
data_updated['seq_read_32']['bs']=bs
data_updated['seq_read_32']['bw']=bw
data_updated['seq_read_32']['latency']=lat_ns
data_updated['seq_read_32']['iops']=iops
data_updated['seq_write_32']={}
data_updated['seq_write_32']['bs']=seq_write_bs
data_updated['seq_write_32']['bw']=seq_write_bw
data_updated['seq_write_32']['latency']=seq_write_lat_ns
data_updated['seq_write_32']['iops']=seq_write_iops
data_updated['seq_randread_32']={}
data_updated['seq_randread_32']['bs']=seq_randread_bs
data_updated['seq_randread_32']['bw']=seq_randread_bw
data_updated['seq_randread_32']['iops']=seq_randread_iops
data_updated['seq_randread_32']['latency']=seq_randread_lat_ns
data_updated['seq_randwrite_32']={}
data_updated['seq_randwrite_32']['bs']=seq_randwrite_bs
data_updated['seq_randwrite_32']['bw']=seq_randwrite_bw
data_updated['seq_randwrite_32']['iops']=seq_randwrite_iops
data_updated['seq_randwrite_32']['latency']=seq_randwrite_lat_ns
js = json.dumps(data_updated, indent = 4)
print("JS\n\n"+js)
