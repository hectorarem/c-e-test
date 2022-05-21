import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root',
})
export class AuthenticationService {
  userUrl = environment.authUrl + 'auth/login';
  userLogout = environment.authUrl + 'auth/logout';
  urlSingUp = environment.authUrl + 'auth/register/';

  constructor(private httpClient: HttpClient) {}

  login(user: string, password: string) {
    const data = {
      username: user,
      password: password,
    };
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      }),
    };

    return this.httpClient.post<any>(this.userUrl, data, httpOptions);
  }

  logout(): Observable<any> {
    return this.httpClient.get(this.userLogout);
  }

  singUp(body:any): Observable<any> {
    return this.httpClient.post<any>(this.urlSingUp, body);
  }


  getUser(): any {
    return JSON.parse(localStorage.getItem('user') || '{}');
  }

  isLoggedIn(): boolean {
    return this.getUser().username;
  }


  updateUserToken(resp: any) {
    const dataString = JSON.stringify(resp.user);
    try {
      localStorage.setItem('user', dataString);
      localStorage.setItem('id', resp.id);
    } catch (e) {}
    // this.$loggedInUserUpdated.next(dataString);
  }
}

export const AUTH_PROVIDERS: Array<any> = [
  {
    provide: AuthenticationService,
    useClass: AuthenticationService,
  },
];
