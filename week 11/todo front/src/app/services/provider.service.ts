import { EventEmitter, Injectable } from '@angular/core';
import {TaskList, Task} from '../models/models';
import {HttpClient, HttpParams} from '@angular/common/http';
import {MainService} from './main.service';
@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {
  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<TaskList[]> {
    return this.get('http://127.0.0.1:8000/api/task_lists',  {});
  }
  getTasks(id: number) {
    return this.get(`http://localhost:8000/api/task_lists/${id}/tasks/`, {});
  }

}
