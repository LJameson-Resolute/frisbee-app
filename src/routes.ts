import { Routes } from "@angular/router";
import { HomeComponent } from "./app/home/home.component";
import { DetailsComponent } from "./app/details/details.component";

const routeConfig: Routes = [
    {
        path: '',
        component: HomeComponent,
        title: 'Home page',
        pathMatch: 'full',
    },
    {
        path: 'details/:id',
        component: DetailsComponent,
        title: 'Player details',
    },
]

export default routeConfig;