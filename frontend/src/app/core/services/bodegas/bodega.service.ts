import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Bodega } from '../../models/bodegas/bodegas.model';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class BodegaService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getBodega(id):Observable<Bodega>{
    return this.http.get<Bodega>(
      environment.api + 'warehouse/' + id + '/inventory',
      {headers: this.headers}
    )
  }
  getBodegaInventory(url):Observable<Bodega>{
    return this.http.get<Bodega>(
      environment.api + 'inventory/' + url,
      {headers: this.headers}
    )
  }
  getBodegas():Observable<Bodega[]>{
    return this.http.get<Bodega[]>(
      environment.api + 'warehouse/get/',
      {headers: this.headers}
    )
  }
  setBodega(bodega):Observable<Bodega>{
    var body = JSON.stringify(bodega)
    return this.http.post<Bodega>(
      environment.api + 'warehouse/set/',
      body,
      {headers: this.headers}
    )
  }
  deleteBodega(bodega):Observable<Bodega>{
    var body = JSON.stringify(bodega)
    return this.http.post<Bodega>(
      environment.api + 'warehouse/del/',
      body,
      {headers: this.headers}
    )
  }
  createBodega(bodega):Observable<Bodega>{
    var body = JSON.stringify(bodega)
    return this.http.post<Bodega>(
      environment.api + 'warehouse/add_product/',
      body,
      {headers: this.headers}
    )
  }
  editProductBodega(bodega):Observable<Bodega>{
    var body = JSON.stringify(bodega)
    return this.http.post<Bodega>(
      environment.api + 'warehouse/edit_product/',
      body,
      {headers: this.headers}
    )
  }
}
