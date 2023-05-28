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
      environment.api + 'clasificacion/' + id,
      {headers: this.headers}
    )
  }
  getClasificacions():Observable<Clasificacions[]>{
    return this.http.get<Clasificacions[]>(
      environment.api + 'clasificacion/get/',
      {headers: this.headers}
    )
  }
  setClasificacion(clasificacion):Observable<Clasificacions>{
    var body = JSON.stringify(clasificacion)
    return this.http.post<Clasificacions>(
      environment.api + 'clasificacion/set/',
      body,
      {headers: this.headers}
    )
  }
  delelasificacion(clasificacion):Observable<Clasificacions>{
    var body = JSON.stringify(clasificacion)
    return this.http.post<Clasificacions>(
      environment.api + 'clasificacion/del/',
      body,
      {headers: this.headers}
    )
  }
  crealasificacion(clasificacion):Observable<Clasificacions>{
    var body = JSON.stringify(clasificacion)
    return this.http.post<Clasificacions>(
      environment.api + 'clasificacion/add/',
      body,
      {headers: this.headers}
    )
  }
}
