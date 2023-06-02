import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { Order, OrderItem } from '../../models/order/order.model';

@Injectable({
  providedIn: 'root'
})
export class OrderService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getOrder():Observable<any>{
    return this.http.get<any>(
      environment.api + 'order/get/',
      {headers: this.headers}
    )
  }

  getOrderItemsByOrderId(orderId):Observable<any>{
    return this.http.get<any>(
      environment.api + 'order/get/'+orderId,
      {headers: this.headers}
    )
  }

  deleteOrderItem(orderId,itemId):Observable<any>{
    var body = JSON.stringify({'id_pedido':orderId,'id_producto':itemId})
    return this.http.delete<any>(
      environment.api + 'order/delete_item/',
      {headers: this.headers}
    )
  }

  addOrder(order:Order):Observable<any>{
    let body = JSON.stringify(order);
    return this.http.post<any>(
      environment.api + 'order/add/',
      body,
      {headers: this.headers}
    )
  }

  addItemOrder(item:OrderItem):Observable<any>{
    let body = JSON.stringify(item); 
    return this.http.post<any>(
      environment.api + "order/add_item",
      body,
      {headers: this.headers}
    )
  }

  setItemOrder(item:OrderItem):Observable<any>{
    let body = JSON.stringify(item); 
    return this.http.post<any>(
      environment.api + "order/add_item",
      body,
      {headers: this.headers}
    )
  }

  rateOrder(item:any):Observable<any>{
    let body = JSON.stringify(item); 
    return this.http.post<any>(
      environment.api + "order/rate_service",
      body,
      {headers: this.headers}
    )
  }

  
}
