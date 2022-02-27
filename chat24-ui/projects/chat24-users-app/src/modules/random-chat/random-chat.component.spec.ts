import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RandomChatComponent } from './random-chat.component';

describe('RandomChatComponent', () => {
  let component: RandomChatComponent;
  let fixture: ComponentFixture<RandomChatComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RandomChatComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RandomChatComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
