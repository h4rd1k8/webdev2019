export interface TaskList {
  id: number;
  name: string;
}

export interface Task {
  id: number;
  name: string;
  task_list: TaskList
  status: string;
  created_at: Date;
  due_on: Date;
}
