import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class PaymentService {
  configUrl = environment.api
  constructor(private http: HttpClient) { }

  payUBuy() {
    return this.http.get<any>(`${this.configUrl}payu-payment`);
  }
}
