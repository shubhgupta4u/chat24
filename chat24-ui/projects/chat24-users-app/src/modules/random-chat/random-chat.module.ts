import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RandomChatComponent } from './random-chat.component';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', component: RandomChatComponent }
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
