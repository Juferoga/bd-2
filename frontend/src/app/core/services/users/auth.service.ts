import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { TokenModel } from '../../models/users/token.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  headers = new HttpHeaders();

  constructor(private http: HttpClient) {
    this.headers = this.headers.append('Content-Type', 'application/json');
  }

  ngOnInit(): void {
    this.onClean();
  }

  onClean(): void{
    sessionStorage.removeItem('role');
    sessionStorage.removeItem('token');
    sessionStorage.removeItem('id');
    sessionStorage.clear();
  }

  onLogin(correo: string, pass: string):Observable<TokenModel> {
    const body = new URLSearchParams();
    body.set('username', correo);
    body.set('password', pass); 
    return this.http.post<TokenModel>(
      environment.api + 'token',
      body.toString(),
      { headers: {'Content-Type':'application/x-www-form-urlencoded'} }
    );
  }

  isAuthorized(allowedRoles: string[]): boolean {
    if (allowedRoles == null || allowedRoles.length == 0) {
      return true;
    }

    const token = sessionStorage.getItem('token');
    const role = sessionStorage.getItem('role');

    if (!token) {
      return false;
    }

    return allowedRoles.includes(role);
  }
  
}
