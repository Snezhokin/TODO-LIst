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