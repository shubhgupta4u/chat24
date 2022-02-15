import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Chat24LibComponent } from './chat24-lib.component';

describe('Chat24LibComponent', () => {
  let component: Chat24LibComponent;
  let fixture: ComponentFixture<Chat24LibComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Chat24LibComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Chat24LibComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
