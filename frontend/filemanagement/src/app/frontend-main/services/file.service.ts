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

  getFiles(): Observable<any> {
    const access = localStorage.getItem('access');
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access,
      }),
    };
    return this.httpClient.get(this.baseUrl + 'file', httpOptions) as Observable<any>
  }
}
