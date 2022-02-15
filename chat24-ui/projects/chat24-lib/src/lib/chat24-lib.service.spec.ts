import { TestBed } from '@angular/core/testing';

import { Chat24LibService } from './chat24-lib.service';

describe('Chat24LibService', () => {
  let service: Chat24LibService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Chat24LibService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
