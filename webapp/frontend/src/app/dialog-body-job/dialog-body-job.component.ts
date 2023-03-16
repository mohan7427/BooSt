import { Component } from '@angular/core';
import { MatDialog, MatDialogConfig, MatDialogRef } from '@angular/material/dialog';
import { JobsService } from 'src/Services/Jobs/jobs.service';
import { DialogBodyComponent } from '../dialog-body/dialog-body.component';

@Component({
  selector: 'app-dialog-body-job',
  templateUrl: './dialog-body-job.component.html',
  styleUrls: ['./dialog-body-job.component.scss']
})
export class DialogBodyJobComponent {

  jobName:string='';
  ioEngine:string='';
  diskName:string='';
  blockSize:string='';
  readWrite:string='';
  runTime:string='';
  ioDepth: number=0;
  numJobs: number=0;
  data = true;
  loading = false;
  dataKey:any = null;

  constructor(public dialogRef: MatDialogRef<DialogBodyJobComponent>,private matDialog: MatDialog,private jobservice: JobsService){
    
  }

  close() {
    // alert(JSON.stringify(this.validbranchDataDistinct))
    this.dialogRef.close();
  }

  openDialog() {
    const dialogConfig = new MatDialogConfig();
    let dialogRef = this.matDialog.open(DialogBodyComponent,  { disableClose: true, data: {
      dataKey: this.dataKey,
      drun: false
    } });
    
  }


  submit(){
    this.loading = true;

    // block_size: str
    // io_depth: str
    // run_time: str
    // io_engine: str
    // job_name: str
    // disk_name: str
    // num_jobs: int
    // read_write: str
    
    var obj = {
      block_size:this.blockSize,
      io_depth:this.ioDepth,
      run_time:this.runTime,
      io_engine:this.ioEngine,
      job_name:this.jobName,
      disk_name:this.diskName,
      num_jobs:this.numJobs,
      read_write:this.readWrite,
    }
    // console.log("branches add ",JSON.stringify(this.validbranchDataDistinct));
    // console.log("chains add ",JSON.stringify(this.validchainDataDistinct));
    // console.log("widgets add ",JSON.stringify(this.validwidgetDataDistinct));
   

    // console.log("branches add1 ",JSON.stringify(this.superbranchDataDistinct));
    // console.log("chains add1 ",JSON.stringify(this.superchainDataDistinct));
    // console.log("widgets add1 ",JSON.stringify(this.superwidgetDataDistinct));

    // console.log("obj ",JSON.stringify(this.obj));
   

    this.jobservice.addJob(obj)
    .subscribe(
      data => {
        console.log(JSON.stringify(data));
        
        this.dataKey = true;
        this.jobservice.setChange();

        this.openDialog();
        alert("rajat");
        this.close()
        
        /*if (JSON.stringify(this.validbranchDataDistinct[1]['brnch_status']) === 'true'){
          window.sessionStorage.setItem("DEV","true")
        }
        else{
          window.sessionStorage.setItem("DEV","false")
        }
        if (JSON.stringify(this.validbranchDataDistinct[0]['brnch_status']) === 'true'){
          window.sessionStorage.setItem("TAG","true")
        }
        else{
          window.sessionStorage.setItem("TAG","false")
        }*/
        this.loading = false;
    //     this.UserService.setDone();
        
      }
    )

    
  }

}
