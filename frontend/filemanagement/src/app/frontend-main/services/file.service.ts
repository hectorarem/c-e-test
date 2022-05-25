import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {environment} from "../../../environments/environment";
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FileService {
  baseUrl = environment.baseUrl + 'file/';
  constructor(private httpClient: HttpClient) {}

  getFiles(url:string | null): Observable<any> {
    const url_r = url ? url : this.baseUrl + 'file';
    const access = localStorage.getItem('access');
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access,
      }),
    };
    return this.httpClient.get(url_r, httpOptions) as Observable<any>
  }
}
