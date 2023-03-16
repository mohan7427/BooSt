import { Component, Inject } from '@angular/core';
import { MatDialogRef,MAT_DIALOG_DATA } from "@angular/material/dialog";

@Component({
  selector: 'app-dialog-body',
  templateUrl: './dialog-body.component.html',
  styleUrls: ['./dialog-body.component.scss']
})
export class DialogBodyComponent {

  data1 : any
  drun: any

  constructor(@Inject(MAT_DIALOG_DATA) public data: any,public dialogRef: MatDialogRef<DialogBodyComponent>) { 
    console.log(JSON.stringify(data));
     this.data1= data.dataKey;
     this.drun = data.drun;
     
  }

  ngOnInit(): void {
    
  }

  close() {
    this.dialogRef.close();
  }

}
