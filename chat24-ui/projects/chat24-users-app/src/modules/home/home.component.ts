import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth-service.service';
import * as jQuery from "jquery";
declare var grecaptcha:any;

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {
  captchaVerified:boolean=false;

  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    jQuery(()=>{
      this.checkCaptcha(this);
    })
  }

  login() {
    
  }
  checkCaptcha(self:HomeComponent|null = null) {
    if (!self) {
      self = this;
    }

    grecaptcha.ready(()=> {
      grecaptcha.execute('6Lc5SfUUAAAAAHCcuEiscTko7ov1CSfAwFbEgYGu', { action: 'homepage' }).then(function (token:any) {
        console.log(token);     
        if(self != null){
          self.authService.checkCaptcha(token).subscribe((data:any)=>{
            console.log(data);
            if(self && data && data.success){
              self.captchaVerified = true;
            }          
          })
        }   
      });
    });
    //secret key
    //6Lc5SfUUAAAAADRAeQPzp-BOeivdn2H_3Vi9HPl5

  }
  signup() {
    
  }
}
