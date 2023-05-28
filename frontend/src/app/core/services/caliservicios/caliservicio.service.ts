import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { CalificacionServicios } from '../../models/caliservicios/caliservicios.model';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class CaliservicioService {

  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getCaliServ(id):Observable<CalificacionServicios>{
    return this.http.get<CalificacionServicios>(
      environment.api + 'calif_serv/' + id,
      {headers: this.headers}
    )
  }
  getCaliServs():Observable<CalificacionServicios[]>{
    return this.http.get<CalificacionServicios[]>(
      environment.api + 'calif_serv/get/',
      {headers: this.headers}
    )
  }
  setCaliServ(calServ):Observable<CalificacionServicios>{
    var body = JSON.stringify(calServ)
    return this.http.post<CalificacionServicios>(
      environment.api + 'calif_serv/set/',
      body,
      {headers: this.headers}
    )
  }
  deleteCaliServ(calServ):Observable<CalificacionServicios>{
    var body = JSON.stringify(calServ)
    return this.http.post<CalificacionServicios>(
      environment.api + 'calif_serv/del/',
      body,
      {headers: this.headers}
    )
  }
  createCaliServ(calServ):Observable<CalificacionServicios>{
    var body = JSON.stringify(calServ)
    return this.http.post<CalificacionServicios>(
      environment.api + 'calif_serv/add/',
      body,
      {headers: this.headers}
    )
  }
}
