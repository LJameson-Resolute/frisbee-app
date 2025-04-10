import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Player } from '../player';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-player-card', 
  imports: [CommonModule, RouterModule],
  templateUrl: './player-card.component.html',
  styleUrl: './player-card.component.css'
})
export class PlayerCardComponent {
  @Input() player!: Player;
}
