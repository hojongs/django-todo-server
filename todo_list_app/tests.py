# run command : python manage.py test [AppName.tests[.TestCaseName[.TestName]]]
import json
import unittest
import django

from .models import Todo


class BackendTestCase(django.test.TestCase):
    def setUp(self):
        self.c = django.test.Client()

        t1 = Todo(todo_name='test1')
        t1.save()
        t2 = Todo(todo_name='test2')
        t2.save()
        t21 = Todo(todo_name='test2-1', parent_todo=t2)
        t21.save()
        t211 = Todo(todo_name='test2-1-1', parent_todo=t21)
        t211.save()
        t22 = Todo(todo_name='test2-2', parent_todo=t2)
        t22.save()
        self.test_data = [t1, t2, t21, t211, t22]

    def tearDown(self):
        Todo.objects.all().delete()

    def test_todo_list(self):
        # root todo_list
        parent_id = None
        response = self.c.get('/b/todo/')
        todo_list = json.loads(response.content)
        todo_list = todo_list['todo_list']
        self.assertEqual(len(todo_list), len(Todo.todo_list(parent_id=parent_id)))

        # child of test2
        parent_id = self.test_data[1].id
        response = self.c.get('/b/todo/?parent_id=%s' % parent_id)
        todo_list = json.loads(response.content)
        todo_list = todo_list['todo_list']
        self.assertEqual(len(todo_list), len(Todo.todo_list(parent_id=parent_id)))

        # child of test2-1-1 don't have any child
        parent_id = self.test_data[3].id
        response = self.c.get('/b/todo/?parent_id=%s' % parent_id)
        todo_list = json.loads(response.content)
        todo_list = todo_list['todo_list']
        self.assertEqual(len(todo_list), len(Todo.todo_list(parent_id=parent_id)))

    def test_todo_detail(self):
        for i in [0, 3]:
            t = self.test_data[i]
            response = self.c.get('/b/todo/%s/' % t.id)
            t2 = json.loads(response.content)
            self.assertTrue(t.id == t2['id']
                            and t.todo_name == t2['todo_name']
                            and t.priority == t2['priority'])

    def test_todo_form(self):
        t = self.test_data[0]

        response = self.c.get('/b/todo_form/')
        self.assertEqual(response.status_code, 200)
        response = self.c.get('/b/todo_form/?todo_id=%s' % t.id)
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        t = self.test_data[0]
        response = self.c.post('/b/todo/', {
            'todo_name': 'First Todo5561', 'pub_date': ['2019-10-25 18:27:07'], 'parent_todo': t.id, 'priority': ''
        })
        self.assertEqual(len(self.test_data)+1, len(Todo.objects.all()))

    def test_update_todo(self):
        t = self.test_data[0]
        todo_name = 'changed todo'

        response = self.c.post('/b/todo/%s/' % t.id, {
            'todo_name': todo_name,
        })

        self.assertEqual(len(self.test_data), len(Todo.objects.all()))
        self.assertEqual(Todo.objects.get(id=t.id).todo_name, todo_name)

    def test_delete_todo_forbidden(self):
        t = self.test_data[0]

        response = self.c.get('/b/delete/', {
            'delete_id': t.id,
        })
        self.assertEqual(response.status_code, 403)

        response = self.c.post('/b/delete/', {
            'delete_id': -1,
        })
        self.assertEqual(response.status_code, 403)

    def test_delete_todo_success(self):
        t = self.test_data[0]

        self.assertIsNotNone(Todo.objects.get(id=t.id))

        response = self.c.post('/b/delete/', {
            'delete_id': t.id,
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(Todo.objects.filter(id=t.id)), 0)


if __name__ == '__main__':
    unittest.main()
