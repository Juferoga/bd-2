import { Component } from "@angular/core";
import { ConfirmationService, MessageService } from "primeng/api";
import { Categorias } from "src/app/core/models/categorias/categorias.model";
import { Product } from "src/app/core/models/products/product.model";
import { CategoriaService } from "src/app/core/services/categorias/categoria.service";
import { ProductService } from "src/app/core/services/products/product.service";

@Component({
  selector: "app-stock",
  templateUrl: "./stock.component.html",
  styleUrls: ["./stock.component.scss"],
})
export class StockComponent {
  
  productDialog: boolean;
  products: Product[];
  product: Product;
  selectedProducts: Product[];
  submitted: boolean;
  statuses: any[];
  Delete: string;
  categoriesList: Categorias[]=[];

  constructor(
    private messageService: MessageService,
    private confirmationService: ConfirmationService,
    private productService : ProductService,
    private categoriaService:CategoriaService,
  ) {}

  ngOnInit() {
    this.productService.getProducts().subscribe(
      (users) => {
        this.products = users["data"];
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

    this.statuses = [
      { label: "INSTOCK", value: "instock" },
      { label: "LOWSTOCK", value: "lowstock" },
      { label: "OUTOFSTOCK", value: "outofstock" },
    ];

    this.categoriaService.getCategorias().subscribe({
      next:(response)=> {
        if (response as any) {
          this.categoriesList = [response];
        } else {
          this.categoriesList=[

          ]
        }
      }
    })
  }

  openNew() {
    this.product = {
      producto : '',
      nombre : '',
      descripcion : '',
      precio : 0,
      estado : true,
      categoria : ''
    };
    this.submitted = false;
    this.productDialog = true;
  }

  deleteSelectedProducts() {
    this.confirmationService.confirm({
      message: "Estas seguro de eliminar los productos?",
      header: "Confirmar",
      icon: "pi pi-exclamation-triangle",
      accept: () => {
        this.products = this.products.filter(
          (val) => !this.selectedProducts.includes(val)
        );
        this.selectedProducts = null;
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "Productos eliminados",
          life: 3000,
        });
      },
    });
  }

  editProduct(product: Product) {
    this.product = { ...product };
    this.productDialog = true;
  }

  deleteProduct(product: Product) {
    this.confirmationService.confirm({
      message: "Are you sure you want to delete " + product.nombre + "?",
      header: "Confirm",
      icon: "pi pi-exclamation-triangle",
      accept: () => {
        this.products = this.products.filter(
          (val) => val.producto !== product.producto
        );
        this.product = {
          producto : '',
          nombre : '',
          descripcion : '',
          precio : 0,
          estado : true,
          categoria : ''
        };
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "Product Deleted",
          life: 3000,
        });
      },
    });
  }

  hideDialog() {
    this.productDialog = false;
    this.submitted = false;
  }

  saveProduct() {
    this.submitted = true;

    if (this.product.nombre.trim()) {
      if (this.product.producto) {
        this.products[this.findIndexById(this.product.producto)] = this.product;
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "Producto Actualizado",
          life: 3000,
        });
      } else {
        this.product.producto = this.createId();
        this.products.push(this.product);
        this.messageService.add({
          severity: "success",
          summary: "Successful",
          detail: "Producto Creado",
          life: 3000,
        });
      }

      this.products = [...this.products];
      this.productDialog = false;
      this.product = {
        producto : '',
        nombre : '',
        descripcion : '',
        precio : 0,
        estado : true,
        categoria : ''
      };
    }
  }

  findIndexById(id: string): number {
    let index = -1;
    for (let i = 0; i < this.products.length; i++) {
      if (this.products[i].producto === id) {
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
