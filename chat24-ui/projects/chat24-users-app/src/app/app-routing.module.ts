import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from '../modules/home/home.component';
import { RandomChatComponent } from '../modules/random-chat/random-chat.component';

const chatModule = () => import('../modules/random-chat/random-chat.module').then(x => x.RandomChatModule);
const homeModule = () => import('../modules/home/home.module').then(x => x.HomeModule);

const routes: Routes = [
  { path: '', loadChildren: homeModule },
  { path: 'chat', loadChildren: chatModule },
  { path: '**', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
