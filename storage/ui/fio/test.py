bs_list=['4k','8k','16k','32k']
data="\n\n[seq_rd_qd_32_4k] \nstonewall \nbs=4k \niodepth=32 \nnumjobs=4 \nrw=read \nruntime=60 \nwrite_bw_log=seq_read_bw.log"
with open('master-all.fio', 'w+') as f:
    base_data="[global]\niodepth=32\ndirect=1\nioengine=libaio\ngroup_reporting\ntime_based\nname=seq\nlog_avg_msec=1000\nbwavgtime=1000\nfilename=/dev/sdb:/dev/sdc"
    f.write(base_data)
    #lines=f.readlines()
    for bs in bs_list:
        data=f"\n\n[seq_rd_qd_32_{bs}] \nstonewall \nbs={bs} \niodepth=32 \nnumjobs=4 \nrw=read \nruntime=60 \nwrite_bw_log=seq_read_bw.log\n\n[seq_rd_qd_32_{bs}] \nstonewall \nbs={bs} \niodepth=32 \nnumjobs=4 \nrw=write \nruntime=60 \nwrite_bw_log=seq_write_bw.log\n\n[seq_rd_qd_32_{bs}] \nstonewall \nbs={bs} \niodepth=32 \nnumjobs=4 \nrw=randread \nruntime=60 \nwrite_bw_log=rand_rd_bw.log\n\n[seq_rd_qd_32_{bs}] \nstonewall \nbs={bs} \niodepth=32 \nnumjobs=4 \nrw=randwrite \nruntime=60 \nwrite_bw_log=rand_rd_bw.log"
        f.write(data)

read_write = 100

