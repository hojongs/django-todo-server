$.ajax({
    url: '/b/todo/',
    type: 'get',
    success: function(data){
        $.each(data['todo_list'], function (index, todo) {
            console.log(todo);
            add_todo_li(todo, $("#todo_list"));
        });

    }
});
