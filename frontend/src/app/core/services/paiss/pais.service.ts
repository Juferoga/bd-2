import { Injectable } from '@angular/core';
import { Paiss } from '../../models/paiss/paiss.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class PaisService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getPais(id):Observable<Paiss>{
    return this.http.get<Paiss>(
      environment.api + 'country/' + id,
      {headers: this.headers}
    )
  }
  getPaiss():Observable<Paiss[]>{
    return this.http.get<Paiss[]>(
      environment.api + 'country/get/',
      {headers: this.headers}
    )
  }
  setPais(pais):Observable<Paiss>{
    var body = JSON.stringify(pais)
    return this.http.post<Paiss>(
      environment.api + 'country/set/',
      body,
      {headers: this.headers}
    )
  }
  delPais(pais):Observable<Paiss>{
    var body = JSON.stringify(pais)
    return this.http.post<Paiss>(
      environment.api + 'country/del/',
      body,
      {headers: this.headers}
    )
  }
  createPais(pais):Observable<Paiss>{
    var body = JSON.stringify(pais)
    return this.http.post<Paiss>(
      environment.api + 'country/add/',
      body,
      {headers: this.headers}
    )
  }
}
