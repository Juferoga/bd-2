import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { TicketService } from 'src/app/core/services/compra/ticket.service';

@Component({
    template: `
        <div class="stepsdemo-content">
            <p-card>
                <ng-template pTemplate="title"> Información Personal </ng-template>
                <ng-template pTemplate="subtitle"> Ingresa tu información personal </ng-template>
                <ng-template pTemplate="content">
                    <div class="p-fluid">
                        <div class="field">
                            <label for="region">Región</label>
                            <input
                                #region="ngModel"
                                id="region"
                                type="text"
                                required
                                pInputText
                                [(ngModel)]="personalInformation.region"
                                [ngClass]="{ 'ng-dirty': (region.invalid && submitted) || (region.dirty && region.invalid) }"
                            />
                            <small *ngIf="(region.invalid && submitted) || (region.dirty && region.invalid)" class="p-error">Región es required.</small>
                        </div>
                        <div class="field">
                            <label for="pais">País</label>
                            <input #pais="ngModel" id="pais" type="text" required pInputText [(ngModel)]="personalInformation.pais" [ngClass]="{ 'ng-dirty': (pais.invalid && submitted) || (pais.dirty && pais.invalid) }" />
                            <small class="p-error" *ngIf="(pais.invalid && submitted) || (pais.dirty && pais.invalid)">País es requerido.</small>
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

    constructor(public ticketService: TicketService, private router: Router) {}

    ngOnInit() {
        this.personalInformation = this.ticketService.getTicketInformation().personalInformation;
    }

    nextPage() {
        if (this.personalInformation.region && this.personalInformation.pais && this.personalInformation.direccion_entrega && this.personalInformation.ciudad) {
            this.ticketService.ticketInformation.personalInformation = this.personalInformation;
            this.router.navigate(['admin/mis-compras/seat']);

            return;
        }

        this.submitted = true;
    }
}