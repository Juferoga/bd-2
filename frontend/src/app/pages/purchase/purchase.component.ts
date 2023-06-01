import { Component } from "@angular/core";
import { MenuItem, MessageService } from "primeng/api";
import { Subscription } from "rxjs";
import { factura } from "src/app/core/models/factura/factura.model";
import { Pedidos } from "src/app/core/models/pedidos/pedidos.model";
import { TicketService } from "src/app/core/services/compra/ticket.service";
import { FacturaService } from "src/app/core/services/factura/factura.service";
import { PedidoService } from "src/app/core/services/pedidos/pedido.service";
@Component({
  selector: "app-purchase",
  templateUrl: "./purchase.component.html",
  styleUrls: ["./purchase.component.scss"],
})
export class PurchaseComponent {
  items: MenuItem[];
  selectedPedido: any;
  subscription: Subscription;
  isShowDetails:boolean=false;
  pedidos: Pedidos[] = [
    {
      pedido: 1,
      fecha_creacion: new Date(),
      direccion: "Calle Principal 123",
      total: 66638.47, 
      estado: "pendiente",
      ciudad: "Bogotá",
      region: "Cundinamarca",
      pais: "Colombia",
      cliente: 12345
    },
  ]
  
  factura: factura={
      N_FACTURA: "F1",
      T_NCLIENTE: "Santiago Ávila Reina",
      F_CREACION: "2023-05-29",
      F_PAGO: "2023-05-29",
      I_ESTADOF: "Facturado",
      T_DIRECCIONE: "Calle 27 Sur # 12-57",
      T_REGION: "Región Andina",
      T_PAIS: "Colombia",
      A_ITEMSF: [
        {
          Q_PRODUCTO: 20,
          N_PRODUCTO: "Fabuloso Lavanda",
          V_UNITARIO: "12,000",
          V_UNITARIOF: "12,000",
          V_TOTAL: "240,000"
        },
        {
          Q_PRODUCTO: 20,
          N_PRODUCTO: "Fabuloso Lavanda",
          V_UNITARIO: "12,000",
          V_UNITARIOF: "12,000",
          V_TOTAL: "240,000"
        },
        {
          Q_PRODUCTO: 20,
          N_PRODUCTO: "Fabuloso Lavanda",
          V_UNITARIO: "12,000",
          V_UNITARIOF: "12,000",
          V_TOTAL: "240,000"
        },
      ],
      V_SUBTOTAL: "240,000",
      V_IVA: "45,600",
      V_TOTAL: "285,600",
      F_GENERADA: "2023-05-30 01:24"
    }; // con este factura de mentiras como datos cargando

  constructor(
    public messageService: MessageService,
    public ticketService: TicketService,
    private pedidoService: PedidoService,
    private facturaService: FacturaService
  ) {}

  ngOnInit() {
    this.items = [
      {
        label: "Información personal",
        routerLink: "personal",
      },
      {
        label: "Productos",
        routerLink: "seat",
      },
      {
        label: "Pago",
        routerLink: "payment",
      },
      {
        label: "Confirmación",
        routerLink: "confirmation",
      },
    ];

    this.subscription = this.ticketService.paymentComplete$.subscribe(
      (personalInformation) => {
        this.messageService.add({
          severity: "success",
          summary: "Order submitted",
          detail:
            "Dear, " +
            personalInformation.firstname +
            " " +
            personalInformation.lastname +
            " your order completed.",
        });
      }
    );
    this.pedidoService.getPedidos().subscribe({
      next: (res) => {
        console.log(res)
      },
      error:(err)=>{
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: "Carga de hiostorico de pedidos realizada SIN ÉXITO",
          detail: "::: ERROR ::: \n" + err["error"]["detail"],
        });
      }
    });

    this.getFactura(1);
  }

  ngOnDestroy() {
    if (this.subscription) {
      this.subscription.unsubscribe();
    }
  }

  getFactura(id: number) {
    this.facturaService.getFactura(id).subscribe(
      (factura) => {
        this.factura = factura["data"];
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Consulta exitosa",
          detail: "La consulta se realizo correctamente sobre la base de datos",
        });
      },
      (err) => {
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: "Consulta realizada SIN ÉXITO",
          detail: "::: ERROR ::: \n" + err["error"]["detail"],
        });
      }
    );
  }
  onPedidoSelect(event: any) {
    this.selectedPedido = event;
    this.isShowDetails = true
    this.getFactura(event.pedido)
  }
  
}
