import { Injectable } from '@angular/core';
import { Clasificacions } from '../../models/clasificacions/clasificacions.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class ClasificacionService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getClasificacion(id):Observable<Clasificacions>{
    return this.http.get<Clasificacions>(
      environment.api + 'classification/' + id,
      {headers: this.headers}
    )
  }
  getClasificacions():Observable<Clasificacions[]>{
    return this.http.get<Clasificacions[]>(
      environment.api + 'classification/get/',
      {headers: this.headers}
    )
  }
  setClasificacion(clasificacion):Observable<Clasificacions>{
    var body = JSON.stringify(clasificacion)
    return this.http.post<Clasificacions>(
      environment.api + 'classification/set/',
      body,
      {headers: this.headers}
    )
  }
  delelasificacion(clasificacion):Observable<Clasificacions>{
    var body = JSON.stringify(clasificacion)
    return this.http.post<Clasificacions>(
      environment.api + 'classification/del/',
      body,
      {headers: this.headers}
    )
  }
  crealasificacion(clasificacion):Observable<Clasificacions>{
    var body = JSON.stringify(clasificacion)
    return this.http.post<Clasificacions>(
      environment.api + 'classification/add/',
      body,
      {headers: this.headers}
    )
  }
}
