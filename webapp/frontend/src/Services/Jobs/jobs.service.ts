import { Injectable } from '@angular/core';
import { HttpClient , HttpHeaders} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { properties } from 'src/config/properties';
import { Job } from 'src/Classes/job';




@Injectable({
  providedIn: 'root'
})
export class JobsService {
  
  constructor(private httpClient: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest'
    })
  } 

  public getJob(): Observable<Job> {
    console.log("getjob")
    return this.httpClient.get<any>(properties.get_job,{headers: this.httpOptions.headers})
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  public getJobs(): Observable<any> {
    console.log("getjobst");

    return this.httpClient.get<any>(properties.get_jobs,{headers: this.httpOptions.headers})
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
  }

  public addJob(job:any): Observable<any>{
    const headers = {"content-type":"application/json"}
    const body = JSON.stringify(job);
    return this.httpClient.post<any>(properties.add_job,body,{"headers":headers})
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
    
  }

  public delJob(user:any): Observable<any>{
    const headers = {"content-type":"application/json"}
    const body = JSON.stringify(user);
    return this.httpClient.post<any>(properties.del_job,body,{"headers":headers})
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
    
  }

  handleError(error:any) {
    let errorMessage = '';
    if(error.error instanceof ErrorEvent) {
      // Get client-side error
      errorMessage = error.error.message;
    } else {
      // Get server-side error
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    // console.log(errorMessage);
    return throwError(errorMessage);
 }
}

