import { Injectable } from '@angular/core';
import { Metodopagos } from '../../models/metodopagos/metodopagos.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class MetodopagoService {
  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getMetodoPago(id):Observable<Metodopagos>{
    return this.http.get<Metodopagos>(
      environment.api + 'payment/' + id,
      {headers: this.headers}
    )
  }
  getMetodoPagos():Observable<Metodopagos[]>{
    return this.http.get<Metodopagos[]>(
      environment.api + 'payment/get/',
      {headers: this.headers}
    )
  }
  setMetodoPago(metodoPago):Observable<Metodopagos>{
    var body = JSON.stringify(metodoPago)
    return this.http.post<Metodopagos>(
      environment.api + 'payment/set/',
      body,
      {headers: this.headers}
    )
  }
  delMetodoPago(metodoPago):Observable<Metodopagos>{
    var body = JSON.stringify(metodoPago)
    return this.http.post<Metodopagos>(
      environment.api + 'payment/del/',
      body,
      {headers: this.headers}
    )
  }
  createMetodoPago(metodoPago):Observable<Metodopagos>{
    var body = JSON.stringify(metodoPago)
    return this.http.post<Metodopagos>(
      environment.api + 'payment/add/',
      body,
      {headers: this.headers}
    )
  }
}
