import json #Convert dict to json package

#load file containing raw data in json
f = open('/root/storage/ui/json_data2')
data = json.load(f)

#Fetch desired data in dictionary
ui_data={}
for i in range(len(data['jobs'])):
    ui_data[data['jobs'][i]['jobname']]={}
    ui_data[data['jobs'][i]['jobname']]['bs']=data['jobs'][i]['job options']['bs']
    ui_data[data['jobs'][i]['jobname']]['iodepth']=data['jobs'][i]['job options']['iodepth']
    ui_data[data['jobs'][i]['jobname']]['read']={}
    ui_data[data['jobs'][i]['jobname']]['read']['bw']=data['jobs'][i]['read']['bw']
    ui_data[data['jobs'][i]['jobname']]['read']['iops']=data['jobs'][i]['read']['iops']
    ui_data[data['jobs'][i]['jobname']]['read']['lat_ns']=data['jobs'][i]['read']['lat_ns']['mean']
    ui_data[data['jobs'][i]['jobname']]['write']={}
    ui_data[data['jobs'][i]['jobname']]['write']['bw']=data['jobs'][i]['write']['bw']
    ui_data[data['jobs'][i]['jobname']]['write']['iops']=data['jobs'][i]['write']['iops']
    ui_data[data['jobs'][i]['jobname']]['write']['lat_ns']=data['jobs'][i]['write']['lat_ns']['mean']
f.close()

#Convert dict data to json
js = json.dumps(ui_data, indent = 4)
print(js)