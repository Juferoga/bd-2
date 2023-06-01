import { Component } from "@angular/core";
import { ConfirmationService, MessageService } from "primeng/api";
import { Bodega } from "src/app/core/models/bodegas/bodegas.model";
import { Categorias } from "src/app/core/models/categorias/categorias.model";
import { Product } from "src/app/core/models/products/product.model";
import { BodegaService } from "src/app/core/services/bodegas/bodega.service";
import { CategoriaService } from "src/app/core/services/categorias/categoria.service";
import { ProductService } from "src/app/core/services/products/product.service";

@Component({
  selector: "app-stock",
  templateUrl: "./stock.component.html",
  styleUrls: ["./stock.component.scss"],
})
export class StockComponent {

  //Inventario
  productDialog: boolean;
  products: Product[];
  product: Product;
  selectedProducts: Product[];
  submitted: boolean;
  statuses: any[];
  Delete: string;
  categoriesList: Categorias[]=[];
  bodegasList: Bodega[];
  bodega : Bodega;
  isUpdated:boolean=false;
  //Productos
  productosDialog: boolean;
  productos: Product[];
  producto: Product;
  productoSeleccionado: Product[];

  constructor(
    private messageService: MessageService,
    private confirmationService: ConfirmationService,
    private productService : ProductService,
    private categoriaService:CategoriaService,
    private bodegaService:BodegaService,
  ) {}

  ngOnInit() {
    this.productService.getProductsRegion().subscribe(
      (users) => {
        this.products = users["data"];
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Consulta exitosa",
          detail: "La consulta de los PRODUCTOS POR REGIÓN se realizo correctamente sobre la base de datos",
        });
      },
      (err) => {
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: "Consulta de PRODUCTOS POR REGIÓN realizada SIN ÉXITO",
          detail: "::: ERROR ::: \n" + err["error"]["detail"],
        });
      }
    );
    this.productService.getProducts().subscribe(
      (users) => {
        this.productos = users["data"];
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Consulta exitosa",
          detail: "La consulta de los PRODUCTOS se realizo correctamente sobre la base de datos",
        });
      },
      (err) => {
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: "Consulta de PRODUCTOS realizada SIN ÉXITO",
          detail: "::: ERROR ::: \n" + err["error"]["detail"],
        });
      }
    );

    this.bodegaService.getBodegas().subscribe(
      (bodegas) => {
        this.bodegasList = bodegas["data"];
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Consulta exitosa",
          detail: "La consulta de las BODEGAS se realizo correctamente sobre la base de datos",
        });
      },
      (err) => {
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: "Consulta de las BODEGAS realizada SIN ÉXITO",
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
      id:0,
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
    this.isUpdated = true;
    this.productDialog = true;
  }

  /* editProduct(productItem: Product,product: Product,dialog: boolean) {
    product = { ...productItem };
    dialog = true;
  } */

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


  editProducto(product: Product) {
    this.producto = { ...product };
    this.productosDialog = true;
  }


  deleteProducto(product: Product) {
    this.confirmationService.confirm({
      message: "Are you sure you want to delete " + product.nombre + "?",
      header: "Confirm",
      icon: "pi pi-exclamation-triangle",
      accept: () => {
        this.productos = this.productos.filter(
          (val) => val.producto !== product.producto
        );
        this.producto = {
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

  createProductInv(){
    this.bodegaService.createBodega(this.product).subscribe({
      next:()=>{
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Actualización exitosa",
          detail: `La actualización del producto ${this.product['nombre'].toUpperCase()},
          se realizo correctamente sobre la base de datos`,
        });
      },
      error:(err)=>{
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: `Consulta del producto ${this.product['nombre'].toUpperCase()} realizada SIN ÉXITO`,
          detail: "::: ERROR ::: \n" + err["error"]["detail"],
        });
      }
    })
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
  saveProductInv(){
    this.submitted = true;
    let data = {
      id_warehouse: Number(this.product.bodega),
      id_product: Number(this.product.id),
      cantidad: Number(this.product.cantidad)
    }
    this.bodegaService.editProductBodega(data).subscribe({
      next:()=>{
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Actualización exitosa",
          detail: `La actualización del producto ${this.products.find(el=> el.id == data.id_product)['nombre'].toUpperCase()},
          se realizo correctamente sobre la base de datos`,
        });
      },
      error:(err)=>{
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: `Consulta del producto ${this.products.find(el=> el.id == data.id_product)['nombre'].toUpperCase()} realizada SIN ÉXITO`,
          detail: "::: ERROR ::: \n" + err["error"]["detail"],
        });
      }
    })
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

  checkWarehouse(event){
    this.bodegaService.getBodega(event.target.value).subscribe({
      next: (response) => {
        this.products = response["data"];
        this.messageService.add({
          key: "grl-toast",
          severity: "success",
          summary: "Consulta exitosa",
          detail: `La consulta de la BODEGA ${event.target.value} se realizo correctamente sobre la base de datos`,
        });
      },
      error: (err) => {
        this.messageService.add({
          key: "grl-toast",
          severity: "error",
          summary: `Consulta de la BODEGA ${event.target.value} realizada SIN ÉXITO`,
          detail: "::: ERROR ::: \n" + err["error"]["detail"],
        });
      }
    });
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
