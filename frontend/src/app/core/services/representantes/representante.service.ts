import { Injectable } from '@angular/core';
import { Representantes } from '../../models/representantes/representantes.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class RepresentanteService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getRepresentante(id):Observable<Representantes>{
    return this.http.get<Representantes>(
      environment.api + 'representante/' + id,
      {headers: this.headers}
    )
  }
  getRepresentantes():Observable<Representantes[]>{
    return this.http.get<Representantes[]>(
      environment.api + 'representante/get/',
      {headers: this.headers}
    )
  }
  getRepresentantesCom():Observable<Representantes[]>{
    return this.http.get<Representantes[]>(
      environment.api + 'representante/comision/',
      {headers: this.headers}
    )
  }
  setRepresentante(representante):Observable<Representantes>{
    var body = JSON.stringify(representante)
    return this.http.post<Representantes>(
      environment.api + 'representante/set/',
      body,
      {headers: this.headers}
    )
  }
  delRepresentante(representante):Observable<Representantes>{
    var body = JSON.stringify(representante)
    return this.http.post<Representantes>(
      environment.api + 'representante/del/',
      body,
      {headers: this.headers}
    )
  }
  createRepresentante(representante):Observable<Representantes>{
    var body = JSON.stringify(representante)
    return this.http.post<Representantes>(
      environment.api + 'representante/add/',
      body,
      {headers: this.headers}
    )
  }
}
