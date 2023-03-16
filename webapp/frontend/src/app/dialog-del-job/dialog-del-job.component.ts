import { Component, Inject } from '@angular/core';
import { MatDialog, MatDialogConfig, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { JobsService } from 'src/Services/Jobs/jobs.service';
import { DialogBodyComponent } from '../dialog-body/dialog-body.component';

@Component({
  selector: 'app-dialog-del-job',
  templateUrl: './dialog-del-job.component.html',
  styleUrls: ['./dialog-del-job.component.scss']
})
export class DialogDelJobComponent {

  dataKey = false;
  loading = false;
  jobname = '';

  constructor(@Inject(MAT_DIALOG_DATA) public data: any,public dialogRef: MatDialogRef<DialogDelJobComponent>,public jobService:JobsService,private matDialog: MatDialog){
    console.log("rahul");
    console.log(JSON.stringify(data));
    console.log(data.Jobname);
    this.jobname = data.JobName;
  }

  ngOnInit(): void {
  }

  close(){
    console.log("close");
    this.dialogRef.close();
  }

  openDialog() {
    const dialogConfig = new MatDialogConfig();
    let dialogRef = this.matDialog.open(DialogBodyComponent,  { disableClose: true, data: {
      dataKey: false,
      drun: true
    } });
    
  }

  submit(){
    this.loading = true;
    console.log("rajt",this,this.jobname)
    this.jobService.delJob(this.jobname)
    .subscribe(
      data => {
        this.dataKey = true;
        this.jobService.setChange();
        this.openDialog();
        this.close();
        this.loading = false;
      }
    )
    
  }


}
