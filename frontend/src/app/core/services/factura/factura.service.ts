import { Injectable } from '@angular/core';
import { factura } from '../../models/factura/factura.model';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class FacturaService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getFactura(id):Observable<factura>{
    return this.http.get<factura>(
      environment.api_factura + id,
      {headers: this.headers}
    )
  }
}
