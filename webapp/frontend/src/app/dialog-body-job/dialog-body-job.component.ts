import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

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

  constructor(public dialogRef: MatDialogRef<DialogBodyJobComponent>){
    
  }

  close() {
    // alert(JSON.stringify(this.validbranchDataDistinct))
    this.dialogRef.close();
  }

  // openDialog() {
  //   const dialogConfig = new MatDialogConfig();
  //   let dialogRef = this.matDialog.open(DialogBodyComponent,  { disableClose: true, data: {
  //     dataKey: this.dataKey
  //   } });
    
  // }

  submit(){
    this.loading = true;
    
    // this.obj = {
    //   usr_curr: window.sessionStorage.getItem("name"),
    //   usr_id: null,
    //   usr_name:this.userName,
    //   usr_email:this.email,
    //   usr_fname:this.firstName,
    //   usr_lname:this.lastName,
    //   usr_pwd:this.pwd,
    //   usr_lstloggedin:null,
    //   usr_joined:moment().format('YYYY/MM/DD hh:mm:ss'),
    //   usr_isAdmin:this.admin === true ? 1:0,
    //   usr_state:this.active === true ? 1:0,
    //   usr_branches : [this.validbranchDataDistinct,this.superbranchDataDistinct],
    //   usr_chains : [this.validchainDataDistinct,this.superchainDataDistinct],
    //   usr_widgets : [this.validwidgetDataDistinct,this.superwidgetDataDistinct],
    //   time : moment().format('YYYY/MM/DD hh:mm:ss')
      
    // }
    // console.log("branches add ",JSON.stringify(this.validbranchDataDistinct));
    // console.log("chains add ",JSON.stringify(this.validchainDataDistinct));
    // console.log("widgets add ",JSON.stringify(this.validwidgetDataDistinct));
   

    // console.log("branches add1 ",JSON.stringify(this.superbranchDataDistinct));
    // console.log("chains add1 ",JSON.stringify(this.superchainDataDistinct));
    // console.log("widgets add1 ",JSON.stringify(this.superwidgetDataDistinct));

    // console.log("obj ",JSON.stringify(this.obj));
   

    // this.UserService.addUser(this.obj)
    // .subscribe(
    //   data => {
        
    //     this.dataKey = data['success'];
    //     this.openDialog();
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
        
    //   }
    // )

    
  }

}
