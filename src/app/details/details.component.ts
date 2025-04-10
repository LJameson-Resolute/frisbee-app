import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink, RouterOutlet } from '@angular/router';
import { PlayerService } from '../player.service';
import { Player } from '../player';

@Component({
  selector: 'app-details',
  imports: [CommonModule, RouterLink, RouterOutlet],
  templateUrl: './details.component.html',
  styleUrl: './details.component.css'
})
export class DetailsComponent {
  route: ActivatedRoute = inject(ActivatedRoute);
  playerService = inject(PlayerService);
  player: Player | undefined;
  playerId = -1;

  constructor() {}

  ngOnInit() {
    this.playerId = Number(this.route.snapshot.params['id']);
    console.log(this.playerId);
    this.player = this.playerService.getPlayerById(this.playerId);
    console.log(this.player?.name);
  }
}

