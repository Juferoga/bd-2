import { Injectable } from '@angular/core';
import { Regions } from '../../models/regions/regions.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class RegionService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getRegion(id):Observable<Regions>{
    return this.http.get<Regions>(
      environment.api + 'regiones/' + id,
      {headers: this.headers}
    )
  }
  getRegions():Observable<Regions[]>{
    return this.http.get<Regions[]>(
      environment.api + 'regiones/get/',
      {headers: this.headers}
    )
  }
  setRegion(region):Observable<Regions>{
    var body = JSON.stringify(region)
    return this.http.post<Regions>(
      environment.api + 'regiones/set/',
      body,
      {headers: this.headers}
    )
  }
  delRegion(region):Observable<Regions>{
    var body = JSON.stringify(region)
    return this.http.post<Regions>(
      environment.api + 'regiones/del/',
      body,
      {headers: this.headers}
    )
  }
  createRegion(region):Observable<Regions>{
    var body = JSON.stringify(region)
    return this.http.post<Regions>(
      environment.api + 'regiones/add/',
      body,
      {headers: this.headers}
    )
  }
}
