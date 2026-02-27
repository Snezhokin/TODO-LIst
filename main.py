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