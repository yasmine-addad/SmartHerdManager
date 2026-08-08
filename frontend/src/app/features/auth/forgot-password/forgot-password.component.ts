import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators
} from '@angular/forms';

import { RouterLink } from '@angular/router';
import { AuthService } from '../../../core/services/auth.service';

@Component({
  selector: 'app-forgot-password',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    RouterLink
  ],
  templateUrl: './forgot-password.component.html',
  styleUrls: ['./forgot-password.component.scss']
})
export class ForgotPasswordComponent {

  loading = false;
  success = false;
  error = '';

  form!: FormGroup;

  constructor(
    private fb: FormBuilder,
    private auth: AuthService
  ) {

    this.form = this.fb.group({
    email: [
      '',
      [
        Validators.required,
        Validators.email
      ]
    ]
  });
}

  sendEmail() {

    if (this.form.invalid) {

      this.form.markAllAsTouched();

      return;

    }

    this.loading = true;

    this.error = '';

    this.auth.forgotPassword(
      this.form.value.email!
    ).subscribe({

      next: () => {

        this.loading = false;

        this.success = true;

      },

      error: () => {

        this.loading = false;

        this.error = "Impossible d'envoyer le lien.";

      }

    });

  }

}