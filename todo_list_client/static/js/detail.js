var todo_id = location.href.split('/').reverse()[1];
console.log('/b/todo/' + todo_id);

var a = $('#update');
a.attr('href', '/todo_form/?todo_id=' + todo_id);

$.ajax({
    url: '/b/todo/' + todo_id,
    type: 'get',
    success: function(todo){
        console.log(todo);
        $('<span>' + todo.todo_name + '</span>').appendTo($('#todo_name'));
        $('<span>' + todo.id + '</span>').appendTo($('#todo_id'));
        $('<span>' + todo.pub_date + '</span>').appendTo($('#pub_date'));
        add_todo_li(todo, $("#todo_tree"));
        $('<span>' + todo.priority + '</span>').appendTo($('#priority'));

        $('#delete_id').val(todo.id);
    }
});
