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


    this.jobservice.addJob(obj)
    .subscribe(
      data => {
        console.log("rajat");
        console.log(JSON.stringify(data));
        
        this.dataKey = true;
        this.jobservice.setChange();

        this.openDialog();
        alert("rajat");
        this.close()

        this.loading = false;
        
      }
    )

    
  }

}
