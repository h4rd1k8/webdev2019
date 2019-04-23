import { Component, OnInit } from '@angular/core';
import {TaskList, Task} from '../../models/models';
import {ProviderService} from '../../services/provider.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public taskLists: TaskList[] = [];
  public tasks: Task[] = [];
  public name = '';
  public taskName = '';
  public taskStatus = '';
  public taskListID = 0;
  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    });
  }
  getTaskOfTaskList(taskList: TaskList) {
    this.provider.getTasks(taskList.id).then(res => {this.tasks = res; });
  }

  createTaskList() {
      if (this.name !== '') {
        this.provider.createTaskList(this.name).then(res => {
          this.name = '';
          this.taskLists.push(res);
        });
      }
  }

  updateTaskList(taskList: TaskList) {
    this.provider.updateTaskList(taskList).then(res => {});
  }

  deleteTaskList(taskList: TaskList) {
    this.provider.deleteTaskList(taskList).then(res => {
      this.provider.getTaskLists().then(r => {
        this.taskLists = r;
      });
    });
  }

  updateTask(task: Task) {
    this.provider.updateTask(task).then(res => {});
  }

  deleteTask(task: Task) {
    this.provider.deleteTask(task).then(res => {
      this.provider.getTasks(task.task_list.id).then(r => {
        this.tasks = r;
      });
    });
  }

  createTask(name: string, status: string, taskListID: number) {
    let taskList;
    for(let t in this.taskLists) {
      if(t.id === taskListID) {
        taskList = t;
        break;
      }
    }
    this.provider.createTask(name, status, taskList).then(res => {
      name = '';
      status = '';
      taskListID = 0;
    });
  }
}
