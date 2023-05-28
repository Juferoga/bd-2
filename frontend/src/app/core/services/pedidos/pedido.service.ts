import { Injectable } from '@angular/core';
import { Pedidos } from '../../models/pedidos/pedidos.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class PedidoService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getPedido(id):Observable<Pedidos>{
    return this.http.get<Pedidos>(
      environment.api + 'pedidos/' + id,
      {headers: this.headers}
    )
  }
  getPedidos():Observable<Pedidos[]>{
    return this.http.get<Pedidos[]>(
      environment.api + 'pedidos/get/',
      {headers: this.headers}
    )
  }
  setPedido(pedido):Observable<Pedidos>{
    var body = JSON.stringify(pedido)
    return this.http.post<Pedidos>(
      environment.api + 'pedidos/set/',
      body,
      {headers: this.headers}
    )
  }
  delPedido(pedido):Observable<Pedidos>{
    var body = JSON.stringify(pedido)
    return this.http.post<Pedidos>(
      environment.api + 'pedidos/del/',
      body,
      {headers: this.headers}
    )
  }
  createPedido(pedido):Observable<Pedidos>{
    var body = JSON.stringify(pedido)
    return this.http.post<Pedidos>(
      environment.api + 'pedidos/add/',
      body,
      {headers: this.headers}
    )
  }
}
