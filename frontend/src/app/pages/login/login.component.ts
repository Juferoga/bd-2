import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators, FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { tap } from 'rxjs';
import { ROLES } from 'src/app/core/models/users/roles.enum';
import { TokenModel } from 'src/app/core/models/users/token.model';
import { User } from 'src/app/core/models/users/user.model';
import { AuthService } from 'src/app/core/services/user/auth.service';
import { environment } from 'src/environments/environment.development';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  // Referencia de página de documentación
  docs = environment.docs;
  cronograma = environment.cronograma;
  repositorio = environment.repositorio;
  me = environment.juferoga;
  profesor = environment.profesor;
  materia = environment.materia;
  proyecto = environment.proyecto;
  integrantes = environment.integrantes;
  // Datos del usuario
  username:string="";
  password:string="";
  passwordConfirmation:string="";
  // Cargando la petición
  isLoading: boolean;
  // Registro e ingreso
  isLogin: boolean = true;
  // Control de modal
  display:boolean = false;

  constructor(
    private router: Router, 
    private route: ActivatedRoute,
    private authSvc: AuthService,
    private messageService: MessageService,
  ){}

  signUp(){
    this.authSvc.onClean();
    // if(this.loginForm.controls.password.value == passwordConfirmation){
      // this.authSvc.onSignUp(this.loginForm.controls.username.value, this.loginForm.controls.password.value).subscribe(
      //   {
      //       next: (data: TokenModel) => {
      //         sessionStorage.setItem('token', data.token);
      //         sessionStorage.setItem('role', data.role);
      //         sessionStorage.setItem('id', data.id.toString());
      //         this.messageService.add({key:'grl-toast', severity:'success', summary:'Ingreso correcto', detail:'Bienvenido a la plataforma'});
      
      //         if (data.role === ROLES.ADMINISTRATOR) {
      //           this.router.navigate(['/admin']);
      //         } else {
      //           this.router.navigate(['/app']);
      //         }
      //       },
    
      //     error: (any) => {
      //       this.messageService.add({key:'grl-toast', severity:'error', summary:'Ingreso Incorrecto', detail:'Datos de ingreso incorrectos'});
      //     }
      //   }
      // );
    //}
  }

  logIn() {
    // this.isLoading = true;
    this.authSvc.onClean();
    if (this.username == "admin" && this.password == "admin"){
      sessionStorage.setItem('token', 'abc123');
      sessionStorage.setItem('role', 'Administrador');
      sessionStorage.setItem('id', '123123123');
      this.router.navigate(['/admin']);
    }else{
      if (this.username == "user" && this.password == "user"){
        sessionStorage.setItem('token', 'abc123');
        sessionStorage.setItem('role', 'RepresentanteVentas');
        sessionStorage.setItem('id', '12312312321');
        this.router.navigate(['/app']);
      }else{
        if (this.username == "client" && this.password == "client"){
          sessionStorage.setItem('token', 'abc123');
          sessionStorage.setItem('role', 'Cliente');
          sessionStorage.setItem('id', '123123');
          this.router.navigate(['/app']);
        }else{
          this.username == "" && this.password == ""?
          this.messageService.add({key:'grl-toast', severity:'error', summary:'Ingreso Incorrecto', detail:'Escriba sus credenciales'}):
          this.messageService.add({key:'grl-toast', severity:'error', summary:'Ingreso Incorrecto', detail:'Datos de ingreso incorrectos'});
        }
      }
    }
    // this.authSvc.onLogin(this.loginForm.controls.username.value, this.loginForm.controls.password.value).subscribe(
    //   {
    //       next: (data: TokenModel) => {
    //         sessionStorage.setItem('token', data.token);
    //         sessionStorage.setItem('role', data.role);
    //         sessionStorage.setItem('id', data.id.toString());
    //         this.messageService.add({key:'grl-toast', severity:'success', summary:'Ingreso correcto', detail:'Bienvenido a la plataforma'});
    
    //         if (data.role === ROLES.ADMINISTRATOR) {
    //           this.router.navigate(['/admin']);
    //         } else {
    //           this.router.navigate(['/app']);
    //         }
    //       },
  
    //     error: (any) => {
    //       this.messageService.add({key:'grl-toast', severity:'error', summary:'Ingreso Incorrecto', detail:'Datos de ingreso incorrectos'});
    //     }
    //   }
    // );
  }

  onClear(){
    this.username="";
    this.password="";
  }
}
