import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';
import { StaticsQueriesSeller } from '../../models/statics/statics.model';

@Injectable({
  providedIn: 'root'
})
export class StaticsService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }
  
  getBestSellers(fecha_incio,fecha_final):Observable<any>{
    return this.http.get(
      environment.api + 'statics/best/sellers/'+fecha_incio+'/'+fecha_final+'/',
      {headers: this.headers}
    )
  }

  getBestRegion(fecha_incio,fecha_final):Observable<any>{
    return this.http.get(
      environment.api + 'statics/best/regions/'+fecha_incio+'/'+fecha_final+'/',
      {headers: this.headers}
    )
  }

  getBestProducts(fecha_incio,fecha_final):Observable<any>{
    return this.http.get(
      environment.api + 'statics/best/products/'+fecha_incio+'/'+fecha_final+'/',
      {headers: this.headers}
    )
  }

}
