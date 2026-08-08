import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';


export const routes: Routes = [

  // 🌿 Partie publique
  {
    path: '',

    loadComponent: () =>
      import('./features/home/home.component')
      .then(m => m.HomeComponent)
  },


  {
    path: 'auth/login',

    loadComponent: () =>
      import('./features/auth/login/login.component')
      .then(m => m.LoginComponent)

  },


  {
    path: 'auth/register',

    loadComponent: () =>
      import('./features/auth/register/register.component')
      .then(m => m.RegisterComponent)

  },


  // 🔐 Partie privée
  {
    path: '',

    loadComponent: () =>
      import('./layout/main-layout/main-layout.component')
      .then(m => m.MainLayoutComponent),

    /*canActivate: [authGuard],*/

    children: [

      {
        path: 'dashboard',

        loadComponent: () =>
          import('./features/dashboard/dashboard.component')
          .then(m => m.DashboardComponent)

      },


      {
        path: 'animals',

        loadComponent: () =>
          import('./features/animals/animals.component')
          .then(m => m.AnimalsComponent)

      },


      {
        path: 'alerts',

        loadComponent: () =>
          import('./features/alerts/alerts.component')
          .then(m => m.AlertsComponent)

      },


      {
        path: 'users',

        loadComponent: () =>
          import('./features/users/users.component')
          .then(m => m.UsersComponent)

      }

    ]

  },

  {
  path: 'forgot-password',
  loadComponent: () =>
    import('./features/auth/forgot-password/forgot-password.component')
      .then(m => m.ForgotPasswordComponent)
  },

  {
  path: 'reset-password/:uid/:token',
  loadComponent: () =>
    import('./features/auth/reset-password/reset-password.component')
      .then(m => m.ResetPasswordComponent) 
  },


  {
    path: '**',
    redirectTo: ''
  },

  

  

];