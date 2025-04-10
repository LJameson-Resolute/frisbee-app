import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PlayerCardComponent } from '../player-card/player-card.component';
import { Player } from '../player';
import { PlayerService } from '../player.service';

@Component({
  selector: 'app-home',
  imports: [CommonModule, PlayerCardComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  playerList: Player[] = [];
  playerService: PlayerService = inject(PlayerService);
  filteredPlayerList: Player[] = [];

  constructor() {
    this.playerList = this.playerService.getAllPlayers();
    this.filteredPlayerList = this.playerList;
  }

  filterResults(text: string) {
    if(!text){
      this.filteredPlayerList = this.playerList;
      return;
    }

    this.filteredPlayerList = this.playerList.filter((player) => player?.name.toLowerCase().includes(text.toLowerCase()));
  }
  
}
