import { Injectable } from '@angular/core';
import { HttpClient , HttpHeaders} from '@angular/common/http';
import { BehaviorSubject, Observable, throwError } from 'rxjs';
import { retry, catchError } from 'rxjs/operators';
import { properties } from 'src/config/properties';
import { Job } from 'src/Classes/job';




@Injectable({
  providedIn: 'root'
})
export class JobsService {

  done: any = null;
  
  constructor(private httpClient: HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json',
      'X-Requested-With': 'XMLHttpRequest'
    })
  } 

  public change : BehaviorSubject<any> = new BehaviorSubject(null);

  getChange(): Observable<any> {
      return this.change.asObservable();
  }

  setChange() {
      this.change.next(true);
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
    console.log(body);
    return this.httpClient.post<any>(properties.add_job,body,{"headers":headers})
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
    
  }

  public delJob(user:any): Observable<any>{
    const headers = {"content-type":"application/json"}
    const body = JSON.stringify(user);
    return this.httpClient.delete<any>(properties.del_job+"/"+user,{"headers":headers})
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
    
  }

  public runJob(job:any): Observable<any>{
    const headers = {"content-type":"application/json"}
    const body = JSON.stringify(job);
    return this.httpClient.post<any>(properties.run_job,body,{"headers":headers})
    .pipe(
      retry(1),
      catchError(this.handleError)
    )
    
  }

  handleError(error:any) {
    let errorMessage = '';
    if(error.error instanceof ErrorEvent) {

      errorMessage = error.error.message;
    } else {

      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }

    return throwError(errorMessage);
 }
}

