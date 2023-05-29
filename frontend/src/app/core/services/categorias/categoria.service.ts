import { Injectable } from '@angular/core';
import { Categorias } from '../../models/categorias/categorias.model';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment.development';

@Injectable({
  providedIn: 'root'
})
export class CategoriaService {
  headers = new HttpHeaders();

  constructor(
    private http: HttpClient
  ) { 
    this.headers = this.headers.append("Content-Type", "application/json");
  }

  getCategoria(id):Observable<Categorias>{
    return this.http.get<Categorias>(
      environment.api + 'categoria/' + id,
      {headers: this.headers}
    )
  }
  getCategorias():Observable<Categorias>{
    return this.http.get<Categorias>(
      environment.api + 'categoria/',
      {headers: this.headers}
    )
  }
  getCaliServs():Observable<Categorias[]>{
    return this.http.get<Categorias[]>(
      environment.api + 'categoria/get/',
      {headers: this.headers}
    )
  }
  setCatgoria(categoria):Observable<Categorias>{
    var body = JSON.stringify(categoria)
    return this.http.post<Categorias>(
      environment.api + 'categoria/set/',
      body,
      {headers: this.headers}
    )
  }
  deleteCatgoria(categoria):Observable<Categorias>{
    var body = JSON.stringify(categoria)
    return this.http.post<Categorias>(
      environment.api + 'categoria/del/',
      body,
      {headers: this.headers}
    )
  }
  createCatgoria(categoria):Observable<Categorias>{
    var body = JSON.stringify(categoria)
    return this.http.post<Categorias>(
      environment.api + 'categoria/add/',
      body,
      {headers: this.headers}
    )
  }
}
