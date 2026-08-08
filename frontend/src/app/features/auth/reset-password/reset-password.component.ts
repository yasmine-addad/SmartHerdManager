import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators
} from '@angular/forms';

import { ActivatedRoute, Router, RouterLink } from '@angular/router';
import { AuthService } from '../../../core/services/auth.service';

@Component({
  selector: 'app-reset-password',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    RouterLink
  ],
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.scss']
})
export class ResetPasswordComponent {

  loading = false;
  success = false;
  error = '';

  uid = '';
  token = '';

  form!: FormGroup;


  constructor(
    private fb: FormBuilder,
    private auth: AuthService,
    private route: ActivatedRoute,
    private router: Router
  ) {

    this.uid = this.route.snapshot.paramMap.get('uid') ?? '';
    this.token = this.route.snapshot.paramMap.get('token') ??'';


    this.form = this.fb.group({

      password: [
        '',
        [
          Validators.required,
          Validators.minLength(8)
        ]
      ],

      confirmPassword: [
        '',
        Validators.required
      ]

    });

  }


  resetPassword() {

    if (this.form.invalid) {

      this.form.markAllAsTouched();

      return;

    }


    if (
      this.form.value.password !==
      this.form.value.confirmPassword
    ) {

      this.error = "Les mots de passe ne correspondent pas.";

      return;

    }


    this.loading = true;

    this.error = '';


    this.auth.resetPassword(

      this.uid,

      this.token,

      this.form.value.password!

    ).subscribe({

      next: () => {

        this.loading = false;

        this.success = true;


        setTimeout(() => {

          this.router.navigate(['/login']);

        }, 2500);

      },


      error: () => {

        this.loading = false;

        this.error = "Le lien est invalide ou expiré.";

      }

    });

  }

}