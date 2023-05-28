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
      environment.api + 'pais/' + id,
      {headers: this.headers}
    )
  }
  getPaiss():Observable<Paiss[]>{
    return this.http.get<Paiss[]>(
      environment.api + 'pais/get/',
      {headers: this.headers}
    )
  }
  setPais(pais):Observable<Paiss>{
    var body = JSON.stringify(pais)
    return this.http.post<Paiss>(
      environment.api + 'pais/set/',
      body,
      {headers: this.headers}
    )
  }
  delPais(pais):Observable<Paiss>{
    var body = JSON.stringify(pais)
    return this.http.post<Paiss>(
      environment.api + 'pais/del/',
      body,
      {headers: this.headers}
    )
  }
  createPais(pais):Observable<Paiss>{
    var body = JSON.stringify(pais)
    return this.http.post<Paiss>(
      environment.api + 'pais/add/',
      body,
      {headers: this.headers}
    )
  }
}
