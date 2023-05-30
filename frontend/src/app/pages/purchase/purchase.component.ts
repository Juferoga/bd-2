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
      creacion: new Date(),
      direcciones: "Calle Principal 123",
      total: 66638.47, 
      estado: "pendiente",
      ciudad: "Bogotá",
      region: "Cundinamarca",
      pais: "Colombia",
      cliente: 12345
    },
    {
      pedido: 2,
      creacion: new Date(),
      direcciones: "Avenida Central 456",
      total: 39479.25, // Valor en peso colombiano (COP)
      estado: "entregado",
      ciudad: "Medellín",
      region: "Antioquia",
      pais: "Colombia",
      cliente: 67890
    },
    {
      pedido: 3,
      creacion: new Date(),
      direcciones: "Rua Principal 789",
      total: 90714.08, // Valor en peso colombiano (COP)
      estado: "en proceso",
      ciudad: "Cali",
      region: "Valle del Cauca",
      pais: "Colombia",
      cliente: 54321
    },
    {
      pedido: 4,
      creacion: new Date(),
      direcciones: "Rue Principale 987",
      total: 27752.76, 
      estado: "pendiente",
      ciudad: "Barranquilla",
      region: "Atlántico",
      pais: "Colombia",
      cliente: 98765
    },
    {
      pedido: 5,
      creacion: new Date(),
      direcciones: "Hauptstrasse 321",
      total: 120358.25, 
      estado: "entregado",
      ciudad: "Cartagena",
      region: "Bolívar",
      pais: "Colombia",
      cliente: 45678
    },
    {
      pedido: 6,
      creacion: new Date(),
      direcciones: "Via Principale 654",
      total: 101932.61, 
      estado: "en proceso",
      ciudad: "Pereira",
      region: "Risaralda",
      pais: "Colombia",
      cliente: 23456
    },
    {
      pedido: 7,
      creacion: new Date(),
      direcciones: "Carrera Principal 321",
      total: 48321.75, 
      estado: "entregado",
      ciudad: "Bucaramanga",
      region: "Santander",
      pais: "Colombia",
      cliente: 76543
    },
    {
      pedido: 8,
      creacion: new Date(),
      direcciones: "Main Street 555",
      total: 43239.88, 
      estado: "pendiente",
      ciudad: "Cúcuta",
      region: "Norte de Santander",
      pais: "Colombia",
      cliente: 32109
    },
    {
      pedido: 9,
      creacion: new Date(),
      direcciones: "Rua Principal 222",
      total: 71036.13, 
      estado: "en proceso",
      ciudad: "Santa Marta",
      region: "Magdalena",
      pais: "Colombia",
      cliente: 89012
    },
    {
      pedido: 10,
      creacion: new Date(),
      direcciones: "Calle Principal 777",
      total: 35511.63, 
      estado: "entregado",
      ciudad: "Ibagué",
      region: "Tolima",
      pais: "Colombia",
      cliente: 56789
    }
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
