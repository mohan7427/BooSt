import { Component, Input } from '@angular/core';
import { ChartConfiguration } from 'chart.js';

@Component({
  selector: 'app-bar-chart',
  templateUrl: './bar-chart.component.html',
  styleUrls: ['./bar-chart.component.scss']
})
export class BarChartComponent {

// data = {
//   "seq_read_32":{
//        "bs":["1k","2k","4k"],
//        "bw":[73976,83976,93976],
//        "lantency":[171899.659711,181899.659711,161899.659711],
//        "iops":[739736.155203,759736.155203,729736.155203]
//   },
//   "seq_write_32":{
//     "bs":["1k","2k","4k"],
//     "bw":[63976,43976,73976],
//     "lantency":[141399.659711,161899.659711,131899.659711],
//     "iops":[639736.155203,759736.155203,739736.155203]
//   },
//   "seq_randread_32":{
//     "bs":["1k","2k","4k"],
//     "bw":[73976,53976,43976],
//     "lantency":[171899.659711,381899.659711,261899.659711],
//     "iops":[439736.155203,659736.155203,329736.155203]
//   },
//   "seq_randwrite_32":{
//     "bs":["1k","2k","4k"],
//     "bw":[73976,83976,93976],
//     "lantency":[171899.659711,181899.659711,161899.659711],
//     "iops":[739736.155203,759736.155203,729736.155203]
//   },

// };

barChartLegend = true;
barChartPlugins = [];

barChartDataBw:any;
barChartDataLat:any;
barChartDataIops:any;

barChartOptions: ChartConfiguration<'bar'>['options'] = {
responsive: false,
};

@Input() graphData: any;

ngOnInit(){

  console.log("rajat",this.graphData.value['bs']);



  var dt1:ChartConfiguration<'bar'>['data'] = {
    labels: this.graphData.value['bs'],
    datasets: [
      { data: this.graphData.value['bw'], label: 'BandWidth (in MB/s)', borderColor: '#36A2EB', backgroundColor: '#566D7E'}      
    ]
  };

  console.log(this.graphData.value['latency']);

  var dt2:ChartConfiguration<'bar'>['data'] = {
    labels: this.graphData.value['bs'],
    datasets: [      
      { data: this.graphData.value['latency'], label: 'Latency (in ms)', borderColor: '#36A2EB', backgroundColor: '#7BCCB5'}
    ]
  };

  var dt3:ChartConfiguration<'bar'>['data'] = {
    labels: this.graphData.value['bs'],
    datasets: [
      { data: this.graphData.value['iops'], label: 'IOPS', borderColor: '#36A2EB', backgroundColor: '#ED7014'}
    ]
  };

  this.barChartDataBw = dt1;
  this.barChartDataLat = dt2;
  this.barChartDataIops = dt3;
  
}



}
