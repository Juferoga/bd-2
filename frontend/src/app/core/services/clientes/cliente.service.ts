import { Injectable } from '@angular/core';
import { Clientes } from '../../models/clientes/clientes.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class ClienteService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getCliente(id):Observable<Clientes>{
    return this.http.get<Clientes>(
      environment.api + 'clientes/' + id,
      {headers: this.headers}
    )
  }
  getClientes():Observable<Clientes[]>{
    return this.http.get<Clientes[]>(
      environment.api + 'clientes/get/',
      {headers: this.headers}
    )
  }
  setCliente(clientes):Observable<Clientes>{
    var body = JSON.stringify(clientes)
    return this.http.post<Clientes>(
      environment.api + 'clientes/set/',
      body,
      {headers: this.headers}
    )
  }
  delCliente(clientes):Observable<Clientes>{
    var body = JSON.stringify(clientes)
    return this.http.post<Clientes>(
      environment.api + 'clientes/del/',
      body,
      {headers: this.headers}
    )
  }
  createCliente(clientes):Observable<Clientes>{
    var body = JSON.stringify(clientes)
    return this.http.post<Clientes>(
      environment.api + 'clientes/add/',
      body,
      {headers: this.headers}
    )
  }
}
