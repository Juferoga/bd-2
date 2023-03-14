import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CheckLoginGuard,  } from './core/guards/check-login.guard';
import { CheckLogoutGuard } from './core/guards/check-logout.guard';
import { ROLES } from './core/models/users/roles.enum';
import { LayoutComponent } from './layout/layout.component';
import { AdminComponent } from './pages/admin/admin.component';
import { HomeComponent } from './pages/home/home.component';
import { LoginComponent } from './pages/login/login.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { OnBuildComponent } from './pages/on-build/on-build.component';
import { MyReferralsComponent } from './shared/my-referrals/my-referrals.component';
import { MySalesComponent } from './shared/my-sales/my-sales.component';
import { MyShoppingComponent } from './shared/my-shopping/my-shopping.component';
import { PaymentComponent } from './shared/payment/payment.component';
import { ProfileComponent } from './shared/profile/profile.component';
import { ShipmentComponent } from './shared/shipment/shipment.component';
import { StockComponent } from './shared/stock/stock.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'inicio',
    pathMatch: 'full'
  },
  {
    path: 'inicio',
    component: HomeComponent,
    canActivate: [CheckLogoutGuard]
  },
  {
    path: 'no-encontrado',
    component: NotFoundComponent,
    canActivate: [CheckLogoutGuard]
  },
  {
    path: 'login',
    component: LoginComponent,
    canActivate: [CheckLogoutGuard]
  },
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [CheckLoginGuard],
    data: {
      allowedRoles: [ROLES.ADMINISTRATOR],
    },
    children: [
      {
        path: 'mi-perfil',
        component: ProfileComponent
      },
      {
        path: 'mi-inventario',
        component: StockComponent
      },
      {
        path: 'mis-ventas',
        component: MySalesComponent
      },
      {
        path: 'mis-compras',
        component: MyShoppingComponent
      },
      {
        path: 'mis-referidos',
        component: MyReferralsComponent
      }
    ]
  },
  {
    path: 'app',
    component: LayoutComponent,
    canActivate: [CheckLoginGuard],
    data: {
      allowedRoles: [ROLES.CLIENTE, ROLES.REPRESENTANTE_VENTAS],
    },
    children: [
      {
        path: 'mi-perfil',
        component: ProfileComponent
      },
      {
        path: 'mi-inventario',
        component: StockComponent
      },
      {
        path: 'mis-ventas',
        component: MySalesComponent
      },
      {
        path: 'mis-compras',
        component: MyShoppingComponent
      },
      {
        path: 'mis-referidos',
        component: MyReferralsComponent
      }
    ]
  },
  {
    path:'test',
    component: PaymentComponent,
    pathMatch: 'full'
  },
  {
    path:'envios',
    component: ShipmentComponent,
    pathMatch: 'full'
  },
  {
    path:'**',
    component: NotFoundComponent,
    pathMatch:'full'
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
