import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {AuthGuard} from "./auth/guards/auth.guard";

const routes: Routes = [
  {
    path: '',
    loadChildren: () =>
      import('./forntend-main/forntend-main.module').then(
        (m) => m.ForntendMainModule
      ),
    canActivate: [AuthGuard],
  },
  {
    path: 'access',
    loadChildren: () => import('./auth/auth.module').then((m) => m.AuthModule),
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
