export class User{
  id ?: number;
  nombre: string;
  apellido: string;
  fecha_de_nacimiento: Date;
  genero: string;
  telefono: number;
  direccion: string;
  email: string;
  estado: string = 'A';
  username?: string;
  representante?: string;
  ciudad?: string;
  
  contrato?: string;
  region?: string;
  pais?: string;
  clasificacion?: string;
  
  password?: string;

  constructor(){
  }
}

// export class User{
//   id : number;
//   nombre : string;
//   apellido : string;
//   fecha_de_nacimiento : Date;
//   genero : string;
//   telefono : number;
//   direccion : string;
//   email : string;
//   estado : string;

//   constructor(){
//   }
// }

// export class UserOfDB extends User{
//   username : string;
//   password
// }

// export class Representante extends UserOfDB{
//   contrato : Date;
//   region : string;
//   pais : string;
//   clasificacion : string;
// }

// export class Cliente extends UserOfDB{
//   ciudad : string;
// }