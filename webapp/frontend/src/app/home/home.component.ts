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

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  displayedColumns: string[] = ['POSITION','JOB NAME', 'I/O-ENGINE', 'DISKNAME','BLOCKSIZE','I/O-DEPTH','NUMJOBS','READ/WRITE','RUNTIME','RUN','DELETE'];
  data: Job[] = [];
  dataLoaded = false;

  constructor(private matDialog: MatDialog, public jobService:JobsService){

  }

  ngOnInit(){

    var totdata = [];

    this.jobService.getJobs().subscribe((d)=>{
      totdata = d;
    })

    ELEMENT_DATA.forEach((d)=>{
      d['RUN'] = 'play_circle_filled',
      d['DELETE'] = 'delete'

      this.data.push(d);
    })
    this.dataLoaded = true;
  }

  openDialog() {
    const dialogConfig = new MatDialogConfig();
    let dialogRef = this.matDialog.open(DialogBodyJobComponent,  { disableClose: true, data: true});
    
  }
}
