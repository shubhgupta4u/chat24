import { Component, OnInit } from '@angular/core';
import * as jQuery from "jquery";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'chat24-users-app';

  ngOnInit(): void {
    // jQuery(($) => {
    //   const signs = document.querySelectorAll('x-sign')
    //   const randomIn = (min:number, max:number) => (
    //     Math.floor(Math.random() * (max - min + 1) + min)
    //   )

    //   const mixupInterval = (el:any) => {
    //     const ms = randomIn(2000, 4000)
    //     el.style.setProperty('--interval', `${ms}ms`)
    //   }

    //   signs.forEach(el => {
    //     mixupInterval(el)
    //     $(el).on('animationiteration webkitAnimationIteration oanimationiteration MSAnimationIteration', function (argument) {
    //       mixupInterval(el)
    //     });
    //     // el.addEventListener('webkitAnimationIteration', () => {
    //     //   mixupInterval(el)
    //     // })
    //   })
    // })
  }
}
