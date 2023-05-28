import { Injectable } from '@angular/core';
import { Pagopedidos } from '../../models/pagopedidos/pagopedidos.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class PagopedidoService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getPagoPedido(id):Observable<Pagopedidos>{
    return this.http.get<Pagopedidos>(
      environment.api + 'pagopedido/' + id,
      {headers: this.headers}
    )
  }
  getPagoPedidos():Observable<Pagopedidos[]>{
    return this.http.get<Pagopedidos[]>(
      environment.api + 'pagopedido/get/',
      {headers: this.headers}
    )
  }
  setPagoPedido(pagoPedido):Observable<Pagopedidos>{
    var body = JSON.stringify(pagoPedido)
    return this.http.post<Pagopedidos>(
      environment.api + 'pagopedido/set/',
      body,
      {headers: this.headers}
    )
  }
  delPagoPedido(pagoPedido):Observable<Pagopedidos>{
    var body = JSON.stringify(pagoPedido)
    return this.http.post<Pagopedidos>(
      environment.api + 'pagopedido/del/',
      body,
      {headers: this.headers}
    )
  }
  createPagoPedido(pagoPedido):Observable<Pagopedidos>{
    var body = JSON.stringify(pagoPedido)
    return this.http.post<Pagopedidos>(
      environment.api + 'pagopedido/add/',
      body,
      {headers: this.headers}
    )
  }
}
