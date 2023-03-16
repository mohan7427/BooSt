import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterModule } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { GraphComponent } from './graph/graph.component';
import { DialogBodyJobComponent } from './dialog-body-job/dialog-body-job.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatTableModule } from '@angular/material/table';
import {MatIconModule} from '@angular/material/icon';
import { FormsModule } from '@angular/forms';
import { MatDialogModule } from '@angular/material/dialog';
import { DialogBodyComponent } from './dialog-body/dialog-body.component';
import { HttpClientModule } from '@angular/common/http';
import { DialogDelJobComponent } from './dialog-del-job/dialog-del-job.component';
// import { ChartjsModule } from '@coreui/angular-chartjs';
// import { FusionChartsModule } from "angular-fusioncharts";

// Import FusionCharts library and chart modules
// import * as FusionCharts from "fusioncharts";
// import * as charts from "fusioncharts/fusioncharts.charts";
// import * as FusionTheme from "fusioncharts/themes/fusioncharts.theme.fusion";

// Pass the fusioncharts library and chart modules
//FusionChartsModule.fcRoot(FusionCharts, charts, FusionTheme);
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    FooterComponent,
    GraphComponent,
    DialogBodyJobComponent,
    DialogBodyComponent,
    DialogDelJobComponent
  ],
  imports: [
    BrowserModule,
    NgbModule,
    RouterModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatTableModule,
    MatIconModule,
    FormsModule,
    MatDialogModule,
    HttpClientModule,
    // FusionChartsModule,
    // ChartjsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
