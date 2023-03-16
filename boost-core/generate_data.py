import json #Convert dict to json package

#load file containing raw data in json
f = open('/root/BooSt/boost-core/test.json')
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
print(js)
