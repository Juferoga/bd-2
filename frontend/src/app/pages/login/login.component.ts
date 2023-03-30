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
  }

  logIn() {
    this.authSvc.onLogin(this.username, this.password).subscribe(
      {
          next: (data: TokenModel) => {
            sessionStorage.setItem('token', data.token);
            sessionStorage.setItem('role', data.role);
            sessionStorage.setItem('id', data.id.toString());
            this.messageService.add({key:'grl-toast', severity:'success', summary:'Ingreso correcto', detail:'Bienvenido a la plataforma'});
    
            if (data.role === ROLES.ADMINISTRATOR) {
              this.router.navigate(['/admin']);
            } else {
              this.router.navigate(['/app']);
            }
          },
  
        error: (any) => {
          this.messageService.add({key:'grl-toast', severity:'error', summary:'Ingreso Incorrecto', detail:'Datos de ingreso incorrectos'});
        }
      }
    );
  }

  onClear(){
    this.username="";
    this.password="";
  }
}
