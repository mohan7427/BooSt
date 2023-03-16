import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DialogBodyJobComponent } from './dialog-body-job.component';

describe('DialogBodyJobComponent', () => {
  let component: DialogBodyJobComponent;
  let fixture: ComponentFixture<DialogBodyJobComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DialogBodyJobComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DialogBodyJobComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
