import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LayoutComponent } from './layout/layout.component';
import { LoginComponent } from './pages/login/login.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AdminComponent } from './pages/admin/admin.component';
import { HomeComponent } from './pages/home/home.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { HttpClientModule } from '@angular/common/http';
import {InputTextModule} from 'primeng/inputtext';
import {PasswordModule} from 'primeng/password';
import {ButtonModule} from 'primeng/button';
import {ToastModule} from 'primeng/toast';
import {MessageService} from 'primeng/api';
import {MenubarModule} from 'primeng/menubar';
import { TopBarComponent } from './shared/top-bar/top-bar.component';
import { SideBarComponent } from './shared/side-bar/side-bar.component';
import {SlideMenuModule} from 'primeng/slidemenu';
import {MenuModule} from 'primeng/menu';
import { ProfileComponent } from './shared/profile/profile.component';
import {ChartModule} from 'primeng/chart';
import { OnBuildComponent } from './pages/on-build/on-build.component';
import {SidebarModule} from 'primeng/sidebar';

@NgModule({
  declarations: [
    AppComponent,
    LayoutComponent,
    LoginComponent,
    AdminComponent,
    HomeComponent,
    NotFoundComponent,
    TopBarComponent,
    SideBarComponent,
    ProfileComponent,
    OnBuildComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    InputTextModule,
    PasswordModule,
    ButtonModule,
    HttpClientModule,
    ToastModule,
    FormsModule,
    MenubarModule,
    SlideMenuModule,
    MenuModule,
    ChartModule,
    SidebarModule,
  ],
  providers: [
    MessageService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
