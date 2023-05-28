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
      environment.api + 'bodega/' + id,
      {headers: this.headers}
    )
  }
  getBodegas():Observable<Bodega[]>{
    return this.http.get<Bodega[]>(
      environment.api + 'bodega/get/',
      {headers: this.headers}
    )
  }
  setBodega(bodega):Observable<Bodega>{
    var body = JSON.stringify(bodega)
    return this.http.post<Bodega>(
      environment.api + 'bodega/set/',
      body,
      {headers: this.headers}
    )
  }
  deleteBodega(bodega):Observable<Bodega>{
    var body = JSON.stringify(bodega)
    return this.http.post<Bodega>(
      environment.api + 'bodega/del/',
      body,
      {headers: this.headers}
    )
  }
  createBodega(bodega):Observable<Bodega>{
    var body = JSON.stringify(bodega)
    return this.http.post<Bodega>(
      environment.api + 'bodega/add/',
      body,
      {headers: this.headers}
    )
  }
}
