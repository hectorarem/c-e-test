import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ForntendMainComponent } from './forntend-main.component';

const routes: Routes = [{ path: '', component: ForntendMainComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ForntendMainRoutingModule { }
