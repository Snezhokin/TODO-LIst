task = {
    "id" : 1,
    "title" : "Learn Python",
    "completed" : False
}

todo_list=[]

def add_task(todo_list , title):
    task = {
        "id" : len(todo_list) + 1,
        "title" : title,
        "completed" : False
    }

    todo_list.append(task)

add_task(todo_list , "Learn Python")
print(todo_list)

def update_task(todo_list, task_id , new_title):
    for task in todo_list:
        if task["id"] == task_id:
            task["title"] = new_title
            break

todo_list = [{'id' : 1 , 'title' : 'Learn Python' , 'completed' : False}]
update_task(todo_list, 1 , "Repeat Python")
print(todo_list)

def complete_task(todo_list , task_id):
    for task in todo_list:
        if task["id"] == task_id:
            task["completed"] = True
            break

todo_list = [{'id' : 1 ,'title' : 'Repeat Python', 'completed' : False }]
complete_task(todo_list , 1)
print(todo_list)


def delete_task(todo_list, task_id):
    for task in todo_list:
        if task['id']== task_id:
            todo_list.remove(task)
            break

todo_list = [{'id': 1 , 'title' : 'Repeat Python' , 'completed' : True}]
delete_task(todo_list , 1)
print(todo_list)

def search_tasks(todo_list , query):
    return [ 
        task for task in todo_list
          if query.lower() in task["title"].lower() 
    ]

todo_list = [
    {'id' : 1 , 'title' : 'Learn Python', 'completed' : True},
    {'id' : 2 , 'title' : 'test the code' , 'completed' : False}
]

result = search_tasks(todo_list, "Pyhton")
print(result)