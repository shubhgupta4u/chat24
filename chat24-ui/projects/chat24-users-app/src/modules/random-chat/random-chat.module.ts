import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RandomChatComponent } from './random-chat.component';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from '../../services/auth-guard.service';

const routes: Routes = [
  { path: '', component: RandomChatComponent , canActivate: [AuthGuard]}
];

@NgModule({
  declarations: [
    RandomChatComponent
  ],
  imports: [
    CommonModule,
    RouterModule.forChild(routes)
  ]
})
export class RandomChatModule { }
