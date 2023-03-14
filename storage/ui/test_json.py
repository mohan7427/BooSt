import json
f = open('/root/storage/ui/json_data')
data = json.load(f)
ui_data={}
for i in range(len(data['jobs'])):
    ui_data[data['jobs'][i]['jobname']]={}
    print("\n\nJob Name",data['jobs'][i]['jobname'])
    #ui_data[data['jobs'][i]['jobname']['bs']]=data['jobs'][i]['job options']['bs']
    x=data['jobs'][i]['job options']['bs']
    print(x)
    #y=ui_data[data['jobs'][i]['jobname']['bs']]
    print("BS",data['jobs'][i]['job options']['bs'])
    print("iodepth",data['jobs'][i]['job options']['iodepth'])
    #ui_data[data['jobs'][i]['jobname']['iodepth']]=data['jobs'][i]['job options']['iodepth']
    print("Read BW",data['jobs'][i]['read']['bw'])
    #ui_data[data['jobs'][i]['jobname']['read']]={}
    #ui_data[data['jobs'][i]['jobname']['read']['bw']]=data['jobs'][i]['read']['bw']
    print("Read iops",data['jobs'][i]['read']['iops'])
    #ui_data[data['jobs'][i]['jobname']['read']['iops']]=data['jobs'][i]['read']['iops']
    print("Read lat_ns",data['jobs'][i]['read']['lat_ns'])
    #ui_data[data['jobs'][i]['jobname']['read']['lat_ns']]=data['jobs'][i]['read']['lat_ns']
    print("Write BW",data['jobs'][i]['write']['bw'])
    #ui_data[data['jobs'][i]['jobname']['write']]={}
    #ui_data[data['jobs'][i]['jobname']['write']['bw']]=data['jobs'][i]['write']['bw']
    print("Write iops",data['jobs'][i]['write']['iops'])
    #ui_data[data['jobs'][i]['jobname']['write']['iops']]=data['jobs'][i]['write']['iops']
    print("Write lat_ns",data['jobs'][i]['write']['lat_ns'])
    #ui_data[data['jobs'][i]['jobname']['write']['lat_ns']]=data['jobs'][i]['write']['lat_ns']
f.close()

print("\n\nDICT",ui_data)
