function url_param (name) {
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null){
       return null;
    }
    else{
       return results[1] || 0;
    }
}

var todo_id = url_param('todo_id');

var h1 = $('h1');
var form = $('form');

h1.text('Create Todo');
var action = '/b/todo/';
if (todo_id)
{
    h1.text('Update Todo');
    action = '/b/todo/'+todo_id+'/';
}
form.attr('action', action);

$.ajax({
    url: '/b/todo_form/',
    type: 'get',
    data: { todo_id: todo_id },
    success: function(data) {
        $(data).appendTo(form);
    }
});

