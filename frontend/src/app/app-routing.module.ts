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
import { PaymentComponent } from './shared/payment/payment.component';
import { ProfileComponent } from './shared/profile/profile.component';
import { StockComponent } from './shared/stock/stock.component';
import { PurchaseComponent } from './pages/purchase/purchase.component';
import { ShowsComponent } from './pages/shows/shows.component';
import { UsersComponent } from './pages/users/users.component';
import { StatsComponent } from './pages/stats/stats.component';
import { SellsComponent } from './pages/sells/sells.component';
import { PersonalDemo } from './pages/purchase/personal';
import { SeatDemo } from './pages/purchase/seat';
import { PaymentDemo } from './pages/purchase/payment';
import { ConfirmationDemo } from './pages/purchase/confirmation';

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
    children: [
      {
        path: 'mi-perfil',
        component: ProfileComponent
      },
      {
        path: 'usuarios',
        component: UsersComponent
      },
      {
        path: 'mi-inventario',
        component: StockComponent
      },
      {
        path: 'mis-ventas',
        component: SellsComponent
      },
      {
        path: 'mis-compras',
        component: PurchaseComponent,
        children: [
          {
            path: 'personal',
            component: PersonalDemo
          },
          {
            path: 'seat',
            component: SeatDemo
          },
          {
            path: 'payment',
            component: PaymentDemo
          },
          {
            path: 'confirmation',
            component: ConfirmationDemo
          }
        ]
      },
      {
        path: 'estadisticas',
        component: StatsComponent
      }
    ]
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
