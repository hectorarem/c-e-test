import {AfterViewInit, Component, OnInit} from '@angular/core';
import {MatTableDataSource} from '@angular/material/table';
import {FileService} from "./services/file.service";
import {AuthenticationService} from "../auth/services/authentication.service";
import {ToastrService} from "ngx-toastr";
import {Router} from "@angular/router";
import {ShowToastrService} from "../services/showtoast.service";


@Component({
  selector: 'app-frontend-main',
  templateUrl: './frontend-main.component.html',
  styleUrls: ['./frontend-main.component.css']
})

export class FrontendMainComponent implements OnInit{
  displayedColumns: string[] = ['FECHA', 'SUBIDO POR', 'NOMBRE', 'EXTENSIÓN', 'TAMAÑO', 'ACCIONES'];
  dataSource: any;
  list_count=0;
  previous=null;
  next=null;

  constructor(
    private fileService: FileService,
    private authService:AuthenticationService,
    private toastr: ToastrService,
    private showToastr: ShowToastrService,
    private router: Router,
    ) {  }

  ngOnInit(): void {
    this.dataload(null);
  }

  dataload(url:string | null): void {
    this.fileService.getFiles(url).subscribe(resp => {
      this.dataSource = resp.results;
      this.previous = resp.previous;
      this.next = resp.next;
      this.list_count = resp.count;
    }, error => {
      this.authService.logout();
      this.showToastr.showInfo('Ya expiró la session.', 'Ups!!');
      this.router.navigate(['/access/login']);
    })
  }
  moveToPageNext(): void {
    this.dataload(this.next);
  }
  moveToPagePrevious(): void {
    this.dataload(this.previous);
  }

}

