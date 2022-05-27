import {ViewChild, Component, OnInit} from '@angular/core';
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
  filename='';
  file:any;
  @ViewChild('fileid', {static: false})
  InputVar: any;
  fileLoading=false;
  user:any;

  constructor(
    private fileService: FileService,
    private authService:AuthenticationService,
    private toastr: ToastrService,
    private showToastr: ShowToastrService,
    private router: Router,
    ) { }

  ngOnInit(): void {
    this.dataload(null);
    this.user = this.authService.getUser()
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

  onFileSelected(event:any) {
    // todo validar nombre de fichero

    const file:File = event.target.files[0];
    if(file.size < 104857600){
      this.file = file;
    } else {
      this.showToastr.showInfo('Hasta 100 megas por favor.', 'Pesa mucho!!!');
      this.cleanFileInput();
    }
  }

  fileUpload() {
    this.fileLoading = true;
    const self = this;
    setTimeout(function(){
    // for simulate the upload file, in a real server, quit setTimeout
    if(self.file) {
      const formData = new FormData();
      formData.append('file', self.file, self.file.name);
      const user_id = localStorage.getItem('id' ) || '1';
      formData.append('uploaded_by', user_id);
      self.fileService.createFile(formData).subscribe(resp => {
        self.showToastr.showSucces('Fichero subido al server', 'INFO!');
        self.dataload(null);
        self.cleanFileInput();
        self.fileLoading = false;
      }, error => {
        if (error?.error?.msg) {
          self.showToastr.showError(error.error.msg, 'Error!');
        } else {
          self.showToastr.showError('Fichero no subido, contacte con el admon', 'Error!');
        }
        self.fileLoading = false;
        self.cleanFileInput();
      })
    }
    }, 2000);
  }

  fileDelete(id:string) {
    const result = confirm("¿Desea eliminar el fichero? La información no podrá restarurarse");
    if (result) {
      this.fileService.deleteFile(id).subscribe(resp =>{
        this.showToastr.showInfo('Fichero eliminado', 'INFO!');
        this.dataload(null);
      }, error => {
        this.showToastr.showError('Fichero no eliminado, contacte con el admon', 'Error!');
      })
    }
  }

  cleanFileInput(): void {
    this.file = null;
    this.InputVar.nativeElement.value = ''
  }

  activeEditFileName(id:string) {
    const edit_file_id = 'file_edit_id_' + id;
    let edit_file = document.getElementById(edit_file_id);
    edit_file!.hidden = true;
    const input_file_id = 'file_id_' + id;
    let input_file = document.getElementById(input_file_id);
    input_file!.hidden = false;
  }

  inactiveFileName(id:string) {
    const edit_file_id = 'file_edit_id_' + id;
    let edit_file = document.getElementById(edit_file_id);
    edit_file!.hidden = false;
    const input_file_id = 'file_id_' + id;
    let input_file = document.getElementById(input_file_id);
    input_file!.hidden = true;
  }

  changeFileName(id:string) {
    //todo validar nombre nuevo de fichero
    const filename = document.getElementById('file_name_id_' + id) as HTMLInputElement;
    this.fileService.changeFileName(id, filename.value).subscribe(resp => {
      let new_name = document.getElementById('file_' + id) as HTMLSpanElement;
      new_name.innerHTML = filename.value;
      this.inactiveFileName(id);
      this.showToastr.showSucces("Nombre del fichero cambiado exitosamente!", "Super!!")
      // todo hay que actualizar la url de descarga tambien, para no hacer un reload a la tabla
    })
  }

}

