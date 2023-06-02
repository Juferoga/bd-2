import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Product } from '../../models/products/product.model';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getProduct():Observable<Product>{
    return this.http.get<Product>(
      environment.api + 'product/me/',
      {headers: this.headers}
    )
  }
  getProductS2(country, region):Observable<Product>{
    return this.http.get<Product>(
      environment.api + 'inventory/cr/?country='+country+'&region='+region,
      {headers: this.headers}
    )
  }
  getProducts():Observable<Product[]>{
    return this.http.get<Product[]>(
      environment.api + 'product/get/',
      {headers: this.headers}
    )
  }
  getProductsRegion():Observable<Product[]>{
    return this.http.get<Product[]>(
      environment.api + 'region/inventory/',
      {headers: this.headers}
    )
  }
  setProduct(product):Observable<Product>{
    var body = JSON.stringify(product)
    return this.http.post<Product>(
      environment.api + 'product/set/',
      body,
      {headers: this.headers}
    )
  }
  deleteProduct(id: number): Observable<Product> {
    const url = `${environment.api}product/disable/${id}`;
    return this.http.delete<Product>(url, { headers: this.headers });
  }
  createProduct(product):Observable<Product>{
    var body = JSON.stringify(product)
    return this.http.post<Product>(
      environment.api + 'product/add/',
      body,
      {headers: this.headers}
    )
  }
}
