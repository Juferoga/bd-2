export class User{
  id ?: number;
  nombre: string;
  apellido: string;
  fecha_de_nacimiento: Date;
  genero: string;
  telefono: number;
  direccion: string;
  email: string;
  estado: string;
  username?: string;
  representante?: string;

  constructor(){
  }
}