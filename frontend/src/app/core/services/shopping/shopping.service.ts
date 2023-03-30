import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class ShoppingService {
  shoppingCart: BehaviorSubject<any> = new BehaviorSubject(null);

  configUrl = environment.api
  constructor(private http: HttpClient) { }

  sendproduct(msg:any){
    this.shoppingCart.next(msg);
  }

  getProducts() {
    return this.http.get<any>(`${this.configUrl}`);
  }
}
