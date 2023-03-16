import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DialogDelJobComponent } from './dialog-del-job.component';

describe('DialogDelJobComponent', () => {
  let component: DialogDelJobComponent;
  let fixture: ComponentFixture<DialogDelJobComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DialogDelJobComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DialogDelJobComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
