import { Component } from "@angular/core";
import { ConfirmationService, MessageService } from "primeng/api";
import { User } from "src/app/core/models/users/user.model";
import { Representantes } from "src/app/core/models/representantes/representantes.model";
import { UserService } from "src/app/core/services/users/user.service";
import { RepresentanteService } from "src/app/core/services/representantes/representante.service";
import { HttpClient } from '@angular/common/http';
import { Paiss } from "src/app/core/models/paiss/paiss.model";
import { Regions } from "src/app/core/models/regions/regions.model";
import { Clasificacions } from "src/app/core/models/clasificacions/clasificacions.model";
import { RegionService } from "src/app/core/services/regions/region.service";
import { PaisService } from "src/app/core/services/paiss/pais.service";
import { ClasificacionService } from "src/app/core/services/clasificacions/clasificacion.service";

@Component({
  selector: "app-users",
  templateUrl: "./users.component.html",
  styleUrls: ["./users.component.scss"],
})
export class UsersComponent {
  usuarios: User[];
  userDialog: boolean;
  usuario: User =	{
		nombre: "",
		apellido: "",
		fecha_de_nacimiento: new Date(Date.now()),
		genero: "",
		telefono: 0,
		direccion: "",
		email: "",
		estado: "",

	};
  selectedusuarios: User[];
  submitted: boolean;
  statuses: any[];
	selectedUserType:string=''
	//Para llenar en representante
	paisesList: Paiss[];
	regionesList: Regions[];
  clasificacionList: Clasificacions[];
  // cliente
	ciudadesList: any;
	representantesList:Representantes[];
  isModeEdited:boolean = false;

  constructor(
    private userService: UserService,
    private regionService: RegionService,
    private paisService: PaisService,
    private clasificacionService : ClasificacionService,
    private messageService: MessageService,
    private confirmationService: ConfirmationService,
		private http: HttpClient,
		private representanteService:RepresentanteService
  ) {}

  ngOnInit() {

    this.loadData();

    this.userService.getUsers().subscribe(
      (users) => {
        this.usuarios = users["data"];
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Consulta exitosa",
          detail: "La consulta se realizo correctamente sobre la base de datos - Usuarios Cargados",
        });
      },
      (err) => {
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: "Consulta realizada SIN ÉXITO - Usuarios No cargados",
          detail: "::: ERROR ::: \n" + err["error"]["detail"],
        });
      }
    );

    this.paisService.getPaiss().subscribe(
      (data)=>{
        this.paisesList = data['data'];
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Consulta exitosa",
          detail: "La consulta se realizo correctamente sobre la base de datos - Países Cargados",
        });
      },
      (error)=>{
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: "Consulta realizada SIN ÉXITO - Países No cargados",
          detail: "::: ERROR ::: \n" + error["error"]["detail"],
        });
      }
    )

    this.clasificacionService.getClasificacions().subscribe(
      (data)=>{
        this.clasificacionList = data['data'];
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Consulta exitosa",
          detail: "La consulta se realizo correctamente sobre la base de datos - Países Cargados",
        });
      },
      (error)=>{
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: "Consulta realizada SIN ÉXITO - Países No cargados",
          detail: "::: ERROR ::: \n" + error["error"]["detail"],
        });
      }
    )

    this.statuses = [
      { label: "MASCULINO", value: "M" },
      { label: "FEMENINO", value: "F" },
      { label: "NO BINARIO", value: "N" },
    ];
  }

  openNew() {
    this.usuario = {
      nombre: "",
      apellido: "",
      fecha_de_nacimiento: new Date(Date.now()),
      genero: "",
      telefono: 0,
      direccion: "",
      email: "",
      estado: "",
    };
    this.submitted = false;
    this.userDialog = true;
  }

  deleteSelectedusuarios() {
    this.confirmationService.confirm({
      message: "Estas seguro de eliminar a los usuarios?",
      header: "Confirmar",
      icon: "pi pi-exclamation-triangle",
      accept: () => {
        this.usuarios = this.usuarios.filter(
          (val) => !this.selectedusuarios.includes(val)
        );
        this.selectedusuarios = null;
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "Usuarios eliminados.",
          life: 3000,
        });
      },
    });
  }

  editUsuario(usuario: User) {
    this.isModeEdited = true;
    this.usuario = { ...usuario };
    let fecha = this.usuario.fecha_de_nacimiento.toString().split('T')[0];
    this.usuario.fecha_de_nacimiento = (fecha as any);
    this.userDialog = true;
  }

  deleteUsuario(usuario: User) {
    this.confirmationService.confirm({
      message: "Estas seguro que deseas eliminar a " + usuario.nombre + "?",
      header: "Confirmar",
      icon: "pi pi-exclamation-triangle",
      accept: () => {
        this.usuarios = this.usuarios.filter(
          (val) => val.email !== usuario.email
        );
        this.usuario = null;
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "Usuario eliminado",
          life: 3000,
        });
      },
    });
  }

  hideDialog() {
    this.userDialog = false;
    this.submitted = false;
  }

  saveUsuario() {
    this.submitted = true;

    if (this.usuario.email.trim()) {
      if (!this.findIndexById(this.usuario.email)) {
        this.userService.setUser(this.usuario).subscribe(
          (data)=> {
            this.usuarios[this.findIndexById(this.usuario.email)] = data['data'];
            this.messageService.add({
              severity: "success",
              summary: "Successful",
              detail: "usuario Actualizado",
              life: 3000,
            });
          },
          (err)=> {
            this.messageService.add({
              severity: "error",
              summary: "Error",
              detail: "usuario NO Actualizado"+err,
              life: 3000,
            });
          }
        )
      } else {
        this.usuario.estado = 'A';
        if(this.selectedUserType == 'representante'){
          this.userService.createUserRep(this.usuario).subscribe({
            next:(res)=>{ 
              console.log(res);
              //this.usuarios.push(this.usuario);
              this.usuarios.push(res['data']) ;
              this.messageService.add({
                severity: "success",
                summary: "Successful",
                detail: "Usuario Creado",
                life: 3000,
              });
            },
            error:(err)=>{
              this.messageService.add({
                severity: "error",
                summary: "Error",
                detail: "Usuario NO Creado"+err,
                life: 3000,
              });
            }
          });
        }
        else{
          this.userService.createUserCli(this.usuario).subscribe({
            next:(res)=>{ 
              console.log(res);
              //this.usuarios.push(this.usuario);
              this.usuarios.push(res['data']) ;
              this.messageService.add({
                severity: "success",
                summary: "Successful",
                detail: "usuario Creado",
                life: 3000,
              });
            },
            error:(err)=>{
              this.messageService.add({
                severity: "error",
                summary: "Error",
                detail: "usuario NO Creado"+err,
                life: 3000,
              });
            }
          });
        }
      }

      this.usuarios = [...this.usuarios];
      this.userDialog = false;
      this.usuario = {
				nombre: "",
				apellido: "",
				fecha_de_nacimiento: new Date(Date.now()),
				genero: "",
				telefono: 0,
				direccion: "",
				email: "",
				estado: "",
			};
    }
  }

  findIndexById(id: string): number {
    let index = -1;
    for (let i = 0; i < this.usuarios.length; i++) {
      if (this.usuarios[i].email === id) {
        index = i;
        break;
      }
    }

    return index;
  }

  getSeverity(status: string) {
    switch (status) {
      case "M":
        return "success";
      case "F":
        return "success";
      case "N":
        return "success";
      default:
        return "danger";
    }
  }

	cargarContenidoJSON(ruta):any{
		return this.http.get(ruta)
	}

	loadData(){
		this.cargarContenidoJSON('../../../assets/json/paises.json').subscribe(
			(data) => {this.paisesList = data;},
			(error) => {console.error(error);}
		);
		this.cargarContenidoJSON('../../../assets/json/regiones-colombia.json').subscribe(
			(data) => {this.regionesList = data;},
			(error) => {console.error(error);}
		);
		this.cargarContenidoJSON('../../../assets/json/ciudades-colombia.json').subscribe(
			(data) => {this.ciudadesList = data;},
			(error) => {console.error(error);}
		);
		this.representanteService.getRepresentantes().subscribe({
			next:(res)=>{
				this.representantesList = res;
				console.log(this.representantesList)
			}
		})
	}

  onloadRegion(country){
    this.regionService.getRegion(country.target.value).subscribe(
      (data)=>{
        this.regionesList = data['data'];
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Consulta exitosa",
          detail: "La consulta se realizo correctamente sobre la base de datos - Regiones Cargadas",
        });
      },
      (error)=>{
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: "Consulta realizada SIN ÉXITO - Regiones No cargados",
          detail: "::: ERROR ::: \n" + error["error"]["detail"],
        });
      }
    )
  }
}
