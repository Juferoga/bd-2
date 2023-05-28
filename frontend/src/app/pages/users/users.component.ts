import { Component } from '@angular/core';
import { ConfirmationService, MessageService } from 'primeng/api';
import { User } from 'src/app/core/models/users/user.model';
import { UserService } from 'src/app/core/services/users/user.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent {
  usuarios : User[];

  constructor(
    private userService: UserService,
    private messageService: MessageService,
    private confirmationService: ConfirmationService
  ) {}

  ngOnInit(){
    this.userService.getUsers().subscribe(
      (users) => {
        this.usuarios = users['data'];
        this.messageService.add({key:'grl-toast', severity:'success', summary:'Consulta exitosa', detail:'La consulta se realizo correctamente sobre la base de datos'});
      },
      (err)=>{
        this.messageService.add({key:'grl-toast', severity:'error', summary:'Consulta realizada SIN ÉXITO', detail:'::: ERROR ::: \n'+err['error']['detail']});
      }
    )

    this.statuses = [
      { label: 'MASCULINO', value: 'M' },
      { label: 'FEMENINO', value: 'F' },
      { label: 'NO BINARIO', value: 'N' }
  ];
  }
  
    userDialog: boolean;

    usuario: User;

    selectedusuarios: User[];

    submitted: boolean;

    statuses: any[];

    openNew() {
        this.usuario = null;
        this.submitted = false;
        this.userDialog = true;
    }

    deleteSelectedusuarios() {
        this.confirmationService.confirm({
            message: 'Estas seguro de eliminar a los usuarios?',
            header: 'Confirmar',
            icon: 'pi pi-exclamation-triangle',
            accept: () => {
                this.usuarios = this.usuarios.filter((val) => !this.selectedusuarios.includes(val));
                this.selectedusuarios = null;
                this.messageService.add({ severity: 'success', summary: 'Successful', detail: 'Usuarios eliminados.', life: 3000 });
            }
        });
    }

    editUsuario(usuario: User) {
        this.usuario = { ...usuario };
        this.userDialog = true;
    }

    deleteUsuario(usuario: User) {
        this.confirmationService.confirm({
            message: 'Estas seguro que deseas eliminar a ' + usuario.nombre + '?',
            header: 'Confirmar',
            icon: 'pi pi-exclamation-triangle',
            accept: () => {
                this.usuarios = this.usuarios.filter((val) => val.email !== usuario.email);
                this.usuario = null;
                this.messageService.add({ severity: 'success', summary: 'Successful', detail: 'Usuario eliminado', life: 3000 });
            }
        });
    }

    hideDialog() {
        this.userDialog = false;
        this.submitted = false;
    }

    saveUsuario() {
        this.submitted = true;

        if (this.usuario.nombre.trim()) {
            if (this.usuario.email) {
                this.usuarios[this.findIndexById(this.usuario.email)] = this.usuario;
                this.messageService.add({ severity: 'success', summary: 'Successful', detail: 'usuario Actualizado', life: 3000 });
            } else {
                this.usuario.email = this.createId();
                this.usuarios.push(this.usuario);
                this.messageService.add({ severity: 'success', summary: 'Successful', detail: 'usuario Creado', life: 3000 });
            }

            this.usuarios = [...this.usuarios];
            this.userDialog = false;
            this.usuario = null;
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

    createId(): string {
        let id = '';
        var chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        for (var i = 0; i < 5; i++) {
            id += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        return id;
    }

    getSeverity(status: string) {
        switch (status) {
            case 'M':
                return 'success';
            case 'F':
                return 'success';
            case 'N':
                return 'success';
            default: 
              return 'danger';
        }
    }
}
