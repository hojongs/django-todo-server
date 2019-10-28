import argparse
from urllib import parse
import json
import pprint
from html.parser import HTMLParser
import requests


def get_parser():
    parser = argparse.ArgumentParser(description='http client for testing todo_list_app api')
    parser.add_argument('method', type=str, help='GET or POST')
    parser.add_argument('url', type=str, help='Example : http://hojong.shop:8001/b/todo/?parent_id=1')
    parser.add_argument('--data', type=str, required=False,
                        help='POST data, '
                             'Example : todo_name=my_todo&pub_date=2019-10-25 10:00:00&parent_todo=1&priority=1')

    return parser


if __name__ == '__main__':
    select = 0

    if select == 1:
        # todo_list
        parent_id = 1
        args = get_parser().parse_args(['get', 'http://hojong.shop:8001/b/todo/?parent_id=%s' % parent_id])
    elif select == 2:
        # create_todo
        data = 'todo_name=my_todo&pub_date=2019-10-25 10:00:00&parent_todo=1&priority=1'
        args = get_parser().parse_args(['post', 'http://hojong.shop:8001/b/todo/', '--data', data])
    elif select == 3:
        # get_todo
        todo_id = 9
        args = get_parser().parse_args(['get', 'http://hojong.shop:8001/b/todo/%s/' % todo_id])
    elif select == 4:
        # update_todo
        todo_id = 9
        data = 'todo_name=my_todo2'
        args = get_parser().parse_args(['post', 'http://hojong.shop:8001/b/todo/%s/' % todo_id, '--data', data])
    elif select == 5:
        # delete_todo
        delete_id = 9
        data = 'delete_id=' + str(delete_id)
        args = get_parser().parse_args(['post', 'http://hojong.shop:8001/b/delete/',
                                        '--data', data])
    else:
        args = get_parser().parse_args()

    method = args.method.lower()
    url = args.url
    print('method : %s' % method)
    print('url : %s' % url)

    if method == 'get':
        response = requests.get(url=url)
    elif method == 'post':
        data_dict = parse.parse_qs(args.data)
        s = requests.Session()

        # add csrf token
        referer = 'http://hojong.shop:8001/todo_form/'
        response = s.get(referer)
        data_dict['csrfmiddlewaretoken'] = response.cookies['csrftoken']

        print('data : ')
        pprint.pprint(data_dict)

        response = s.post(url=url, data=data_dict, headers=dict(Referer=referer))
    else:
        response = None

    try:
        print('Response : ')
        result = json.loads(response.content)
        pprint.pprint(result)
    except Exception as e:
        print('Response Status Code : %s' % response.status_code)
        print(response.content)
