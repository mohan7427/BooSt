import os 
import sys
import itertools
import subprocess
import configparser

iodepth=sys.argv[1]
numjobs=sys.argv[2]
user_rw=sys.argv[3]
user_bs=sys.argv[4]
runtime=sys.argv[5]
bs=['1k','2k','4k','8k','16K','32k','64k','128k','256k','512k','1024k','2048k','4096k']
rw=['read','write','randread','randwrite']
fileoutput="test.json"

def fio():
    os.system("rm -rf new/test.json")
    ceph=os.system("fio master.fio  --output={} --output-format=json".format(fileoutput))
    if ceph==0:
      print("command ran successfully!")
    elif ceph!=0:
      print("command failed!")


def ini():
    #create new config object
    config=configparser.ConfigParser()
 
    #read config file into object
    config.read("master.fio")
 
    #Add new section 
    config["global"]={
        "iodepth": "32",
        "direct": "0",
        "ioengine": "libaio",
        "group_reporting":"1",
        "name":"sec",
        "log_avg_msec":"1000",
        "bwavgtime":"1000",
        "filename":"/dev/sdb:/dev/sdc",
        }

    config["seq_{}_{}_{}_1W".format(user_rw,iodepth,user_bs)]={
            "stonewall": "1",
            "bs":"{}".format(user_bs),
            "iodepth":"{}".format(iodepth),
            "numjobs":"{}".format(numjobs),
            "rw":"{}".format(user_rw),
            "runtime":"{}".format(runtime),
            }
 
    #save the config object back to file
    with open("master.fio","w") as file_object:
        config.write(file_object, space_around_delimiters=False)

def ini_count():
    #create new config object
    config=configparser.ConfigParser()

    #read config file into object
    config.read("master.fio")

    for i in itertools.product(rw,bs):
    #Add new section 
        config["global"]={
            "iodepth": "32",
            "direct": "0",
            "ioengine": "libaio",
            "group_reporting":"1",
            "name":"sec",
            "log_avg_msec":"1000",
            "bwavgtime":"1000",
            "filename":"/dev/sdb:/dev/sdc",
            }

        config["seq_{}_{}_{}_1W".format(i[0],iodepth,i[1])]={
                "stonewall": "1",
                "bs":"{}".format(i[1]),
                "iodepth":"{}".format(iodepth),
                "numjobs":"{}".format(numjobs),
                "rw":"{}".format(i[0]),
                "runtime":"{}".format(runtime),
                }

    #save the config object back to file
    with open("master.fio","w") as file_object:
        config.write(file_object, space_around_delimiters=False)

def ini_count_bs_all():
    #create new config object
    config=configparser.ConfigParser()

    #read config file into object
    config.read("master.fio")

    for i in itertools.product(rw,bs):
    #Add new section 
            #Add new section
        config["global"]={
            "iodepth": "32",
            "direct": "0",
            "ioengine": "libaio",
            "group_reporting":"1",
            "name":"sec",
            "log_avg_msec":"1000",
            "bwavgtime":"1000",
            "filename":"/dev/sdb:/dev/sdc",
            }


        config["seq_{}_{}_{}_1W".format(user_rw,iodepth,i[1])]={
                "stonewall": "1",
                "bs":"{}".format(i[1]),
                "iodepth":"{}".format(iodepth),
                "numjobs":"{}".format(numjobs),
                "rw":"{}".format(user_rw),
                "runtime":"{}".format(runtime),
                }

    #save the config object back to file
    with open("master.fio","w") as file_object:
        config.write(file_object, space_around_delimiters=False)

def ini_count_rw_all():
    #create new config object
    config=configparser.ConfigParser()

    #read config file into object
    config.read("master.fio")

    for i in itertools.product(rw,bs):
        #Add new section
        config["global"]={
            "iodepth": "32",
            "direct": "0",
            "ioengine": "libaio",
            "group_reporting":"1",
            "name":"sec",
            "log_avg_msec":"1000",
            "bwavgtime":"1000",
            "filename":"/dev/sdb:/dev/sdc",
            }

        config["seq_{}_{}_{}_1W".format(i[0],iodepth,user_bs)]={
                "stonewall": "1",
                "bs":"{}".format(user_bs),
                "iodepth":"{}".format(iodepth),
                "numjobs":"{}".format(numjobs),
                "rw":"{}".format(i[0]),
                "runtime":"{}".format(runtime),
                }

    #save the config object back to file
    with open("master.fio","w") as file_object:
        config.write(file_object, space_around_delimiters=False)



if (user_bs)=='all' and (user_rw)=='all': 
    ini_count()
elif (user_rw)=='all' and (user_bs)!='all':
    bs=user_bs
    ini_count_rw_all()
elif (user_rw)!='all' and (user_bs)=='all':
    rw=user_rw
    ini_count_bs_all()
elif (user_bs and user_rw)!='all':
    ini()

fio()
test=os.system("rm -rf master.fio")
