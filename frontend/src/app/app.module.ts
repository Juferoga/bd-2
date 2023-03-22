/* Angular Auto Generated START  */
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';

/* Angular Components PRIMENG */
// Services
import { ConfirmationService, MessageService, FilterService, MenuItem } from 'primeng/api';
  // Modules
import { ButtonModule } from 'primeng/button';
import { CalendarModule } from 'primeng/calendar';
import { CardModule } from 'primeng/card';
import { ChartModule } from 'primeng/chart';
import { ConfirmDialogModule } from 'primeng/confirmdialog';
import { ContextMenuModule } from 'primeng/contextmenu';
import { DialogModule } from 'primeng/dialog';
import { DropdownModule } from 'primeng/dropdown';
import { FileUploadModule } from 'primeng/fileupload';
import { InputNumberModule } from 'primeng/inputnumber';
import { InputTextModule } from 'primeng/inputtext';
import { InputTextareaModule } from 'primeng/inputtextarea';
import { MenubarModule } from 'primeng/menubar';
import { MenuModule } from 'primeng/menu';
import { MultiSelectModule } from 'primeng/multiselect';
import { PasswordModule } from 'primeng/password';
import { ProgressBarModule } from 'primeng/progressbar';
import { RadioButtonModule } from 'primeng/radiobutton';
import { RatingModule } from 'primeng/rating';
import { SlideMenuModule } from 'primeng/slidemenu';
import { SliderModule } from 'primeng/slider';
import { SidebarModule } from 'primeng/sidebar';
import { TableModule } from 'primeng/table';
import { TabMenuModule } from 'primeng/tabmenu';
import { ToastModule } from 'primeng/toast';
import { ToolbarModule } from 'primeng/toolbar';

/* Angular Components  PAGES & LAYOUT */
import { AdminComponent } from './pages/admin/admin.component';
import { HomeComponent } from './pages/home/home.component';
import { LayoutComponent } from './layout/layout.component';
import { LoginComponent } from './pages/login/login.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { OnBuildComponent } from './pages/on-build/on-build.component';

/* Angular Components  SHARED */
import { MyReferralsComponent } from './shared/my-referrals/my-referrals.component';
import { MySalesComponent } from './shared/my-sales/my-sales.component';
import { MyShoppingComponent } from './shared/my-shopping/my-shopping.component';
import { ProfileComponent } from './shared/profile/profile.component';
import { PaymentComponent } from './shared/payment/payment.component';
import { SideBarComponent } from './shared/side-bar/side-bar.component';
import { StockComponent } from './shared/stock/stock.component';
import { TopBarComponent } from './shared/top-bar/top-bar.component';
import { PaymentModule } from './payment/payment.module';
import { NgxPayPalModule } from 'ngx-paypal';
import { PurchaseProcessCardComponent } from './components/purchase-process-card/purchase-process-card.component';
import { ShoppingCartComponent } from './pages/shopping-cart/shopping-cart.component';
import { StepToStepComponent } from './components/step-to-step/step-to-step.component';
import { ShoppingComponent } from './shared/shopping/shopping.component';
import { SidebarShoppingComponent } from './components/sidebar-shopping/sidebar-shopping.component';
import { AddressShoppingComponent } from './shared/address-shopping/address-shopping.component';
import { SelectedProductsComponent } from './components/selected-products/selected-products.component';
import { StepsModule } from 'primeng/steps';
import { ShipmentComponent } from './shared/shipment/shipment.component';

@NgModule({
  declarations: [
    AppComponent,
    AdminComponent,
    HomeComponent,
    LayoutComponent,
    LoginComponent,
    MyReferralsComponent,
    MySalesComponent,
    MyShoppingComponent,
    NotFoundComponent,
    OnBuildComponent,
    PaymentComponent,
    ProfileComponent,
    SideBarComponent,
    StockComponent,
    TopBarComponent,
    PurchaseProcessCardComponent,
    ShoppingCartComponent,
    StepToStepComponent,
    ShoppingComponent,
    SidebarShoppingComponent,
    AddressShoppingComponent,
    SelectedProductsComponent,
    ShipmentComponent,
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    BrowserAnimationsModule,
    ButtonModule,
    CalendarModule,
    CardModule,
    ChartModule,
    ConfirmDialogModule,
    ContextMenuModule,
    DialogModule,
    DropdownModule,
    FileUploadModule,
    InputTextModule,
    InputTextareaModule,
    InputNumberModule,
    PasswordModule,
    PaymentModule,
    ProgressBarModule,
    HttpClientModule,
    FormsModule,
    MenubarModule,
    MenuModule,
    MultiSelectModule,
    NgxPayPalModule,
    RatingModule,
    RadioButtonModule,
    ReactiveFormsModule,
    SidebarModule,
    SlideMenuModule,
    SliderModule,
    TabMenuModule,
    TableModule,
    ToastModule,
    ToolbarModule,
    StepsModule,
  ],
  providers: [
    ConfirmationService,
    FilterService,
    MessageService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
