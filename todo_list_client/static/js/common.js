function todo_li(todo) {
    return $('<li></li>').text('[' + todo.id + '] ' + todo.todo_name + ' (' + todo.priority + ') [' + todo.pub_date + ']');
}

function add_todo_li(todo, parent) {
    var li = todo_li(todo);
    li.appendTo(parent);

    var child_list = $('<ul></ul>');
    child_list.appendTo(li);
    $.each(todo.child_list, function (index, child_todo) {
        add_todo_li(child_todo, child_list);
    });
}
