import { Injectable } from '@angular/core';
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

  getPedido(id):Observable<any>{
    return this.http.get<any>(
      environment.api + 'order/' + id,
      {headers: this.headers}
    )
  }
  getPedidos():Observable<any[]>{
    return this.http.get<any[]>(
      environment.api + 'order/get_orders_by_user',
      {headers: this.headers}
    )
  }
  setPedido(pedido):Observable<any>{
    var body = JSON.stringify(pedido)
    return this.http.post<any>(
      environment.api + 'order/set/',
      body,
      {headers: this.headers}
    )
  }
  delPedido(pedido):Observable<any>{
    var body = JSON.stringify(pedido)
    return this.http.post<any>(
      environment.api + 'order/del/',
      body,
      {headers: this.headers}
    )
  }
  createPedido(pedido):Observable<any>{
    var body = JSON.stringify(pedido)
    return this.http.post<any>(
      environment.api + 'order/add/',
      body,
      {headers: this.headers}
    )
  }
}
