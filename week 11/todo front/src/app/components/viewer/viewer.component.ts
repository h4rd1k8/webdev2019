import { Component, OnInit } from '@angular/core';
import {TaskList, Task} from '../../models/models';
import {ProviderService} from '../../services/provider.service';

@Component({
  selector: 'app-viewer',
  templateUrl: './viewer.component.html',
  styleUrls: ['./viewer.component.css']
})
export class ViewerComponent implements OnInit {
  public taskLists: TaskList[] = [];
  public tasks: Task[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
  }
  getTaskOfTaskList(taskList: TaskList) {
    this.provider.getTasks(taskList.id).then(res => {this.tasks = res; });
  }
}
