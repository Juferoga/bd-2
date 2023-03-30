import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ConfirmationService, MessageService } from 'primeng/api';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss','../stock/stock.component.scss']
})
export class UsersComponent {

  userForm: FormGroup;
  userDialog: boolean;
  usersList: any[];
  user: any;
  selectedUsers: any[];
  submitted: boolean;
  statuses: any[];
  estado:any;
  Delete: string;

  constructor(
    private fb: FormBuilder,
    private messageService: MessageService,
    private confirmationService: ConfirmationService
  ) {}

  ngOnInit() {
    // this.productService.getUsers().then(data => this.products = data);

    this.statuses = [
      { label: "ACTIVO", value: "1" },
      { label: "INACTIVO", value: "0" },
    ];
  }

  createForm(){
    this.userForm = this.fb.group({
      k_usuario: ['', Validators.required],
      t_nombre: ['', Validators.required],
      t_apellido: ['', Validators.required],
      f_nacimiento: ['', Validators.required],
      i_genero: ['', Validators.required],
      n_telefono: ['', Validators.required],
      t_direccion: ['', Validators.required],
      t_email: ['', Validators.required],
      i_estado: ['', ],
    });
  }
  openNew() {
    this.user = {};
    this.submitted = false;
    this.userDialog = true;
  }

  deleteSelectedUsers() {
    this.confirmationService.confirm({
      message: "Are you sure you want to delete the selected user?",
      header: "Confirm",
      icon: "pi pi-exclamation-triangle",
      accept: () => {
        this.usersList = this.usersList.filter(
          (val) => !this.selectedUsers.includes(val)
        );
        this.selectedUsers = null;
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "Users Deleted",
          life: 3000,
        });
      },
    });
  }

  editUser(user: any) {
    this.user = { ...user };
    this.userDialog = true;
  }

  deleteUser(user: any) {
    this.confirmationService.confirm({
      message: "Are you sure you want to delete " + user.name + "?",
      header: "Confirm",
      icon: "pi pi-exclamation-triangle",
      accept: () => {
        this.usersList = this.usersList.filter((val) => val.id !== user.id);
        this.user = {};
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "User Deleted",
          life: 3000,
        });
      },
    });
  }

  hideDialog() {
    this.userDialog = false;
    this.submitted = false;
  }

  onSubmit(){

  }

  saveUser() {
    this.submitted = true;

    if (this.user.name.trim()) {
      if (this.user.id) {
        this.usersList[this.findIndexById(this.user.id)] = this.user;
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "User Updated",
          life: 3000,
        });
      } else {
        this.user.id = this.createId();
        this.user.image = "product-placeholder.svg";
        this.usersList.push(this.user);
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "User Created",
          life: 3000,
        });
      }

      this.usersList = [...this.usersList];
      this.userDialog = false;
      this.user = {};
    }
  }

  findIndexById(id: string): number {
    let index = -1;
    for (let i = 0; i < this.usersList.length; i++) {
      if (this.usersList[i].id === id) {
        index = i;
        break;
      }
    }

    return index;
  }

  createId(): string {
    let id = "";
    var chars =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    for (var i = 0; i < 5; i++) {
      id += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return id;
  }
}
