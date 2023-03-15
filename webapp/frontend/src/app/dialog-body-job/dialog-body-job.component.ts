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
  dataKey = true;

  constructor(public dialogRef: MatDialogRef<DialogBodyJobComponent>,private matDialog: MatDialog,private jobservice: JobsService){
    
  }

  close() {
    // alert(JSON.stringify(this.validbranchDataDistinct))
    this.dialogRef.close();
  }

  openDialog() {
    const dialogConfig = new MatDialogConfig();
    let dialogRef = this.matDialog.open(DialogBodyComponent,  { disableClose: true, data: {
      dataKey: this.dataKey
    } });
    
  }


  submit(){
    this.loading = true;
    
    var obj = {
      BlockSize:this.blockSize,
      IODepth:this.ioDepth,
      RunTime:this.runTime,
      IOEngine:this.ioEngine,
      JobName:this.jobName,
      DiskName:this.diskName,
      NumJobs:this.numJobs,
      ReadWrite:this.readWrite,
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
        
        this.dataKey = true;
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
