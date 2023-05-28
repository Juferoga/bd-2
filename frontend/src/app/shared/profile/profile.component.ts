import { Component } from "@angular/core";
import { MessageService } from "primeng/api";
import { Representantes } from "src/app/core/models/representantes/representantes.model";
import { User } from "src/app/core/models/users/user.model";
import { RepresentanteService } from "src/app/core/services/representantes/representante.service";
import { UserService } from "src/app/core/services/users/user.service";

@Component({
  selector: "app-profile",
  templateUrl: "./profile.component.html",
  styleUrls: ["./profile.component.scss"],
})
export class ProfileComponent {

  // TODO: Integrate -> https://primeng.org/tree/horizontal

  userLoading = {
    'nombre':'Cargando',
    'apellido':'Cargando',
    'fecha_de_nacimiento': new Date(Date.now()),
    'genero':'Cargando',
    'telefono': 300000000,
    'direccion':'Cargando',
    'email':'Cargando',
    'estado':'Cargando'
  }

  username = sessionStorage.getItem("username")? sessionStorage.getItem("username"):'Loading...';
  representantes : Representantes[];
  user : User = this.userLoading;
  data: any;
  chartOptions: any;
  isEdited:boolean = false;

  constructor(
    private userService: UserService,
    private repService: RepresentanteService,
    private messageService: MessageService,
  ) {}

  ngOnInit() {

    this.userService.getUser().subscribe(
      (user:User)=>{
        this.user = user['data'];
        this.messageService.add({key:'grl-toast', severity:'success', summary:'Consulta exitosa', detail:'La consulta se realizo correctamente sobre la base de datos'});
      },
      (err)=>{
        this.messageService.add({key:'grl-toast', severity:'error', summary:'Consulta realizada SIN ÉXITO', detail:'::: ERROR ::: \n'+err['error']['detail']});

      }
    )

    this.repService.getRepresentantes().subscribe(
      (representante:Representantes[])=>{
        this.representantes = representante['data'];
        this.messageService.add({key:'grl-toast', severity:'success', summary:'Consulta exitosa', detail:'La consulta se realizo correctamente sobre la base de datos'});
      },
      (err)=>{
        this.messageService.add({key:'grl-toast', severity:'error', summary:'Consulta realizada SIN ÉXITO', detail:'::: ERROR ::: \n'+err['error']['detail']});
      }
    )

    this.data = {
      labels: [
        "Eating",
        "Drinking",
        "Sleeping",
        "Designing",
        "Coding",
        "Cycling",
        "Running",
      ],
      datasets: [
        {
          label: "My First dataset",
          backgroundColor: "rgba(179,181,198,0.2)",
          borderColor: "rgba(179,181,198,1)",
          pointBackgroundColor: "rgba(179,181,198,1)",
          pointBorderColor: "#fff",
          pointHoverBackgroundColor: "#fff",
          pointHoverBorderColor: "rgba(179,181,198,1)",
          data: [65, 59, 90, 81, 56, 55, 40],
        },
        {
          label: "My Second dataset",
          backgroundColor: "rgba(255,99,132,0.2)",
          borderColor: "rgba(255,99,132,1)",
          pointBackgroundColor: "rgba(255,99,132,1)",
          pointBorderColor: "#fff",
          pointHoverBackgroundColor: "#fff",
          pointHoverBorderColor: "rgba(255,99,132,1)",
          data: [28, 48, 40, 19, 96, 27, 100],
        },
      ],
    };
  }

    deleteUser() {
      console.log("Usuario BORRADO")
    }

    saveUser() {
      console.log("Usuario ACTUALIZADO")
    }
}
