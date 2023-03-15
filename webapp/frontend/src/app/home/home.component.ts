import { Component } from '@angular/core';
import {MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { JobsService } from 'src/Services/Jobs/jobs.service';
import { DialogBodyJobComponent } from '../dialog-body-job/dialog-body-job.component';

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

  constructor(private matDialog: MatDialog, public jobService:JobsService){

  }

  ngOnInit(){

    var totdata:any = [];

    console.log("home");

    this.jobService.getJobs().subscribe((d)=>{
      console.log("rajat");
      console.log(JSON.stringify(d));
      totdata = d;

      totdata.forEach((d:any, index:any)=>{
        d['POSITION'] = index;
        d['RUN'] = 'play_circle_filled',
        d['DELETE'] = 'delete'
  
        this.data.push(d);
      })
      console.log(JSON.stringify(this.data));
      this.dataLoaded = true;
    })

    // ELEMENT_DATA.forEach((d)=>{
    //   d['RUN'] = 'play_circle_filled',
    //   d['DELETE'] = 'delete'

    //   this.data.push(d);
    // })
    
  }

  openDialog() {
    const dialogConfig = new MatDialogConfig();
    let dialogRef = this.matDialog.open(DialogBodyJobComponent,  { disableClose: true, data: true});
    
  }
}
