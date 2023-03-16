import sys
import os
dict={
    "JobId": 4,
    "RunTime": "60",
    "JobName": "job4",
    "NumJobs": 4,
    "IOEngine": "libaio",
    "BlockSize": "all",
    "IODepth": "32",
    "DiskName": "libioxxxxxx",
    "ReadWrite": "read",
    "POSITION": 2,
    "RUN": "play_circle_filled",#
    "DELETE": "delete"
}
print(dict["JobId"])
os.system("python3 demo.py {} {} {} {} {}".format(dict["IODepth"],dict["NumJobs"],dict["ReadWrite"],dict["BlockSize"],dict["RunTime"]))