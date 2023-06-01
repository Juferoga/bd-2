import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { Paiss } from 'src/app/core/models/paiss/paiss.model';
import { Regions } from 'src/app/core/models/regions/regions.model';
import { TicketService } from 'src/app/core/services/compra/ticket.service';
import { PaisService } from 'src/app/core/services/paiss/pais.service';
import { RegionService } from 'src/app/core/services/regions/region.service';

@Component({
    template: `
        <div class="stepsdemo-content">
            <p-card>
                <ng-template pTemplate="title"> Información Personal </ng-template>
                <ng-template pTemplate="subtitle"> Ingresa tu información personal </ng-template>
                <ng-template pTemplate="content">
                    <div class="p-fluid">
                        <div class="field">
                            <label for="pais">País</label>
                            <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                    <i class="pi pi-globe"></i>
                                </span>
                                <select id="pais" [(ngModel)]="personalInformation.pais" (change)="onloadRegion($event)">
                                    <option selected disabled value="null">Seleccione País</option>
                                    <option *ngFor="let pais of paisesList" [value]="pais.id">{{ pais.nombre }}</option>
                                </select>
                            </div>
                        </div>
                        <div class="field" *ngIf="personalInformation.pais !== null">
                            <label for="region">Región</label>
                            <div class="p-inputgroup">
                                <span class="p-inputgroup-addon">
                                    <i class="pi pi-globe"></i>
                                </span>
                                <select id="region" [(ngModel)]="personalInformation.region" *ngIf="regionesList.length !=0">
                                    <option selected disabled value="null">Seleccione Región</option>
                                    <option *ngFor="let region of regionesList" [value]="region['id']">{{ region.nombre }}</option>
                                </select>
                                <div *ngIf="!(regionesList.length !=0)">
                                    <input style="min-width: 150px;" placeholder="Escribe tu región..." #region="ngModel" id="ciudad" type="text" required pInputText [(ngModel)]="personalInformation.region" [ngClass]="{ 'ng-dirty': (region.invalid && submitted) || (region.dirty && region.invalid) }" />
                                    <small class="p-error" *ngIf="(ciudad.invalid && submitted) || (ciudad.dirty && ciudad.invalid)">Ciudad es requerido.</small>
                                </div>
                            </div>
                        </div>      
                        <div class="field">
                            <label for="ciudad">Ciudad</label>
                                <input #ciudad="ngModel" id="ciudad" type="text" required pInputText [(ngModel)]="personalInformation.ciudad" [ngClass]="{ 'ng-dirty': (ciudad.invalid && submitted) || (ciudad.dirty && ciudad.invalid) }" />
                            <small class="p-error" *ngIf="(ciudad.invalid && submitted) || (ciudad.dirty && ciudad.invalid)">Ciudad es requerido.</small>
                        </div>
                        <div class="field">
                            <label for="direccion_entrega">Dirección de entrega</label>
                            <input #direccion_entrega="ngModel" id="direccion_entrega" type="text" required pInputText [(ngModel)]="personalInformation.direccion_entrega" [ngClass]="{ 'ng-dirty': (direccion_entrega.invalid && submitted) || (direccion_entrega.dirty && direccion_entrega.invalid) }" />
                            <small class="p-error" *ngIf="(direccion_entrega.invalid && submitted) || (direccion_entrega.dirty && direccion_entrega.invalid)">direccion_entrega is required.</small>
                        </div>
                    </div>
                </ng-template>
                <ng-template pTemplate="footer">
                    <div class="grid grid-nogutter justify-content-end">
                        <p-button label="Siguiente" (onClick)="nextPage()" icon="pi pi-angle-right" iconPos="right"></p-button>
                    </div>
                </ng-template>
            </p-card>
        </div>
    `
})
export class PersonalDemo implements OnInit {
    personalInformation: any;

    submitted: boolean = false;

    paisesList: Paiss[] = [];
	regionesList: Regions[] = [];

    constructor(
        public ticketService: TicketService, 
        private router: Router,
        private messageService: MessageService,
        private regionService: RegionService,
        private paisService: PaisService) {}

    ngOnInit() {
        this.personalInformation = this.ticketService.getTicketInformation().personalInformation;
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
    }

    nextPage() {
        if (this.personalInformation.region && this.personalInformation.pais && this.personalInformation.direccion_entrega && this.personalInformation.ciudad) {
            this.ticketService.ticketInformation.personalInformation = this.personalInformation;
            this.router.navigate(['admin/mis-compras/seat']);

            return;
        }

        this.submitted = true;
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