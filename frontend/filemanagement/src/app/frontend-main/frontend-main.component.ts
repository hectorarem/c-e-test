import {AfterViewInit, Component, OnInit} from '@angular/core';
import {MatTableDataSource} from '@angular/material/table';
import {FileService} from "./services/file.service";


@Component({
  selector: 'app-frontend-main',
  templateUrl: './frontend-main.component.html',
  styleUrls: ['./frontend-main.component.css']
})

export class FrontendMainComponent implements OnInit{
  displayedColumns: string[] = ['FECHA', 'SUBIDO POR', 'NOMBRE', 'EXTENSIÓN', 'TAMAÑO', 'ACCIONES'];
  dataSource: any;


  constructor(private fileService: FileService) {  }

  ngOnInit(): void {
    this.fileService.getFiles().subscribe(resp => {
      this.dataSource = resp;
    })
  }

}

