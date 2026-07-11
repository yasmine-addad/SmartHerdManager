import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { FeatureCardComponent } from '../../shared/components/feature-card/feature-card.component';

interface FeatureItem {
  icon: string;
  title: string;
  description: string;
}

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterLink, FeatureCardComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css',
})
export class HomeComponent {
  readonly features: FeatureItem[] = [
    {
      icon: '🐄',
      title: 'Gestion des animaux',
      description: 'Ajoutez, modifiez et suivez toutes les informations de votre cheptel.',
    },
    {
      icon: '📋',
      title: 'Suivi et historique',
      description: "Consultez l'historique complet de vos animaux et de leurs activités.",
    },
    {
      icon: '📈',
      title: 'Tableaux de bord',
      description: 'Visualisez vos données clés et prenez des décisions rapidement.',
    },
    {
      icon: '🔔',
      title: "Système d'alertes",
      description: 'Recevez des notifications automatiques pour les rappels de vaccins et rendez-vous.',
    },
    {
      icon: '👤',
      title: 'Gestion des utilisateurs',
      description: 'Gérez les accès et les licences de votre équipe en toute sécurité.',
    },
  ];
}