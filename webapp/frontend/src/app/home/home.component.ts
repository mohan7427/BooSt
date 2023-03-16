import { Component, ChangeDetectorRef } from '@angular/core';
import {MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { JobsService } from 'src/Services/Jobs/jobs.service';
import { DialogBodyJobComponent } from '../dialog-body-job/dialog-body-job.component';
import { DialogBodyComponent } from '../dialog-body/dialog-body.component';
import { DialogDelJobComponent } from '../dialog-del-job/dialog-del-job.component';

export interface Job {
  'JOB NAME': string;
  'POSITION': number;
  'I/O-ENGINE': string;
  'DISKNAME':string;
  'BLOCKSIZE':string;
  'I/O-DEPTH':string;
  'NUMJOBS': number;
  'READ/WRITE': string;
  'RUNTIME' : string;
  'RUN'? : string;
  'DELETE'? : string;
}

const ELEMENT_DATA: Job[] = [
  {
    'JOB NAME': 'job1',
    'POSITION': 1,
    'I/O-ENGINE': 'rados',
    'DISKNAME':'/dev/sdb:/dev/sdc',
    'BLOCKSIZE':'16k',
    'I/O-DEPTH':'32',
    'NUMJOBS': 4,
    'READ/WRITE': 'rwmixread-50',
    'RUNTIME' : '20',
  },
  {
    'JOB NAME': 'job1',
    'POSITION': 1,
    'I/O-ENGINE': 'rados',
    'DISKNAME':'/dev/sdb:/dev/sdc',
    'BLOCKSIZE':'16k',
    'I/O-DEPTH':'32',
    'NUMJOBS': 4,
    'READ/WRITE': 'rwmixread-50',
    'RUNTIME' : '20',
  },
  {
    'JOB NAME': 'job1',
    'POSITION': 1,
    'I/O-ENGINE': 'rados',
    'DISKNAME':'/dev/sdb:/dev/sdc',
    'BLOCKSIZE':'16k',
    'I/O-DEPTH':'32',
    'NUMJOBS': 4,
    'READ/WRITE': 'rwmixread-50',
    'RUNTIME' : '20',
  },
  {
    'JOB NAME': 'job1',
    'POSITION': 1,
    'I/O-ENGINE': 'rados',
    'DISKNAME':'/dev/sdb:/dev/sdc',
    'BLOCKSIZE':'16k',
    'I/O-DEPTH':'32',
    'NUMJOBS': 4,
    'READ/WRITE': 'rwmixread-50',
    'RUNTIME' : '20',
  },
]

//var val = [{"JobId":1,"RunTime":"12","JobName":"job1","NumJobs":12,"IOEngine":"rbd","BlockSize":"16","IODepth":"12","DiskName":"rbdxxxxxxx","ReadWrite":"Randread","RUN":"play_circle_filled","DELETE":"delete"}]

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  displayedColumns: string[] = ['POSITION','JobName', 'IOEngine', 'DiskName','BlockSize','IODepth','NumJobs','ReadWrite','RunTime','RUN','DELETE'];
  data: Job[] = [];
  dataLoaded = false;
  //dataKey = false;
  

  constructor(private matDialog: MatDialog, public jobService:JobsService,private changeDetectorRefs: ChangeDetectorRef){
    //this.refresh();
  }

  ngOnInit(){

    

    // ELEMENT_DATA.forEach((d)=>{
    //   d['RUN'] = 'play_circle_filled',
    //   d['DELETE'] = 'delete'

    //   this.data.push(d);
    // })
    this.refresh();
    this.jobService.getChange().subscribe((d)=>{
      this.refresh();
    })
    
  }

  // ngDoCheck(): void {
  //   console.log("check");
  //   var d = this.jobService.getDone()
  //   if (d === true){
  //     this.data = [];
  //     this.refresh();
  //     this.jobService.setDoneFalse()
  //   }
  // }

  openDialog() {
    const dialogConfig = new MatDialogConfig();
     let dialogRef = this.matDialog.open(DialogBodyJobComponent,  { disableClose: true})
     //.afterClosed().subscribe(result => {
    //   console.log("rajat1")
    //   console.log(JSON.stringify(result));
    //   this.refresh();
    //});
    
  }


  deletejob(row :any) {

    const dialogRef = this.matDialog.open(DialogDelJobComponent,  { disableClose: true, data: row});

  }

  openbodydialog() {
    const dialogConfig = new MatDialogConfig();
    let dialogRef = this.matDialog.open(DialogBodyComponent,  { disableClose: true, data: {
      dataKey: true,
      datatype: "run"
    } });
  }

  runjob(row :any) {
    console.log(JSON.stringify(row));
    this.jobService.runJob(row).subscribe((d)=>{
      console.log(d);
    })
  }

  refresh(){
    var totdata:any = [];

    console.log("home");

    this.jobService.getJobs().subscribe((d)=>{
      console.log("rajat");
      console.log(JSON.stringify(d));
      totdata = d;
      this.data = [];

      totdata.forEach((d:any, index:any)=>{
        d['POSITION'] = index;
        d['RUN'] = 'play_circle_filled',
        d['DELETE'] = 'delete'
  
        this.data.push(d);

      })
      console.log(JSON.stringify(this.data));
      this.dataLoaded = true;
      //this.changeDetectorRefs.detectChanges();
    })
  }
}
