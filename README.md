# To Do List App API 서버 & 클라이언트
## Description
해야 할 일을 작성하여 저장해두고 관리하는 서비스의 API 서버 및 클라이언트

## 요구사항 충족여부
* 필수사항
  * API Server 구현 (완료)
    * 프로젝트 내 todo_list_app 구현
    * 생성,수정,조회,삭제 기능 구현
  * Documentation (API Reference Docs) (완료)
    * README.md에 작성
  * Github repo에 오픈 프로젝트 생성 후 업로드 (완료)
* 선택사항
  * 필수사항 외 기능 (완료)
    * Logging 기능 : API별 요청 처리 시 log 작성
    * Unit test 기능 : API별 test code 작성
    * 조회 기능 분리 (Todo List 기능 + Todo item 조회 기능)
      * Todo List 페이지를 통해 모든 Todo를 조회
      * Todo item 페이지를 통해 각각의 Todo item을 조회
    * 하위 Todo 추가 기능 : 상위 Todo와 하위 Todo 구분 가능, 하위 Todo의 깊이 제한 없음
    * (README.md : 3가지 기능에 대한 간단한 설명 작성하였음)
  * 완성된 Backend API를 사용하는 테스트 목적의 간단한 To Do List 클라이언트 구현 (완료)
      * 프로젝트 내 todo_list_client 구현
      * jQuery 기반 Web Client
  * Demo server 구축하여 host url 제출 (완료)

## Tech Stacks
* Backend : Python/Django
* Frontend : HTML/CSS/JS, jQuery

## Usage
* Run development server : `python manage.py runserver`

## Project Structure
* todo_list_server (project)
  * todo_list_app (backend API app)
  * todo_list_client (frontend view app)

## Backend API
### Get Todo list API
* Todo List를 가져옴
* URL : /b/todo/
* Method : GET
* Request Parameter : parent_id (in get parameter)
* Request Example
  * `/b/todo/` : 모든 Todo를 list 형태로 응답
  * `/b/todo/?parent_id=1` : id=1인 Todo의 모든 하위 Todo들을 list 형태로 응답
* Response data : {"todo_list": [Todo Object, Todo Object, Todo Object, ...]} 를 Json 형태로 응답
  * Todo Object structure example
  ```
  {
    "id" : 1,
    "todo_name" : "프로젝트 설계 구상",
    "pub_date" : "2019-10-25T09:30:00Z",
    "priority" : 1,
    "child_list" : [Todo Object, Todo Object, ...]
  }
  ```

### Get Todo item API
* 하나의 Todo item 정보를 가져옴
* URL : /b/todo/<todo_id>/
* Method : GET
* Request Parameter : todo_id (in url)
* Request Example
  * `/b/todo/1/` : id=1인 Todo의 데이터 응답
* Response Data : Todo Object 를 Json 형태로 응답
  * Todo Object structure example
  ```
  {
    "id" : 1,
    "todo_name" : "프로젝트 설계 구상",
    "pub_date" : "2019-10-25T09:30:00Z",
    "priority" : 1,
    "child_list" : [Todo Object, Todo Object, ...]
  }
  ```

### Create Todo API
* Todo item 생성
* URL : /b/todo/
* Method : POST
* Request Parameter : Todo Form Data
* Request Example
  * `/b/todo/`
    * POST body data (Update와 동일)
    ```
    {
      "todo_name": "데이터 구조 설계",
      "pub_date" : "2019-10-25T12:00:00Z",
      "priority" : 5,
      "parent_todo" : 1,
      "csrfmiddlewaretoken": "...",
    }
    ```
* Response Data : Todo Object 를 Json 형태로 응답 (Update와 동일)
  * Todo Object structure example
  ```
  {
    "id" : 1,
    "todo_name" : "프로젝트 설계 구상",
    "pub_date" : "2019-10-25T09:30:00Z",
    "priority" : 1,
    "child_list" : [Todo Object, Todo Object, ...]
  }
  ```

### Update Todo API
* 하나의 Todo item의 데이터를 수정
* URL : /b/todo/<todo_id>/
* Method : POST
* Request Parameter : todo_id, Todo Form Data
* Request Example
  * `/b/todo/2/` : id=2인 Todo item 수정
    * POST body data (Create와 동일)
    ```
    {
      "todo_name": "데이터 구조 구상 및 설계",
      "pub_date" : "2019-10-25T12:00:00Z",
      "priority" : 2,
      "parent_todo" : 1,
      "csrfmiddlewaretoken": "...",
    }
    ```
* Response Data : Todo Object 를 Json 형태로 응답 (Create와 동일)
  * Todo Object structure example
  ```
  {
    "id" : 1,
    "todo_name" : "프로젝트 설계 구상",
    "pub_date" : "2019-10-25T09:30:00Z",
    "priority" : 1,
    "child_list" : [Todo Object, Todo Object, ...]
  }
  ```

### Delete Todo API
* 하나의 Todo item을 삭제
* URL : /delete/
* Method : POST
* Request Parameter : delete_id (in ger parameter)
* Request Example
  * `/delete/?delete_id=2` : id=2인 Todo item 삭제
* Response Data : `{"success": True}` 를 Json 형태로 응답

### Todo Form API
* Frontend에서 사용되는 Form HTML Code를 생성
* URL : /todo_form/
* Method : GET
* Request Parameter : todo_id (수정할 Todo의 id
* Request URL Example
  * /todo_form/?todo_id=2
* Response Data : Form HTML Code
  ```
  <tr><th><label for="id_todo_name">Todo name:</label></th><td><input type="text" name="todo_name" maxlength="256" required id="id_todo_name"></td></tr>
  <tr><th><label for="id_pub_date">Date published:</label></th><td><input type="text" name="pub_date" value="2019-10-27 20:50:46" required id="id_pub_date"><input type="hidden" name="initial-pub_date" value="2019-10-27 20:50:46" id="initial-id_pub_date"></td></tr>
  <tr><th><label for="id_parent_todo">Parent todo:</label></th><td><select name="parent_todo" id="id_parent_todo">
  <option value="" selected>---------</option>
  <option value="5">&lt;First Todo5561 (None)&gt;</option>
  ......
  </select></td></tr>
  <tr><th><label for="id_priority">Priority:</label></th><td><input type="number" name="priority" id="id_priority"></td></tr>
  ```
* 사용 이유 : Frontend의 Form 코드를 빠르게 구현하기 위하여 사용

## View pages
### Todo list 조회
* URL : / (root)
#### Description
* 모든 Todo item을 list 형태로 보여주는 페이지
* 하위 Todo item은 들여쓰기로 구분되어 보여짐
* Create 버튼을 통해 Todo item 생성 가능
* Todo item을 클릭하여 Todo item의 정보 조회 가능
* <img src="/img/index.jpg" width="50%" height="50%">


### Todo item 조회 (Detail view)
* URL : /<todo_id>/
#### Description
* id=<todo_id>인 Todo의 정보를 보여주는 페이지
* Update, Delete 버튼을 통해 Todo item의 수정/삭제 가능
* <img src="/img/todo_item.jpg" width="50%" height="50%">

### Todo item 생성/수정
* URL : /todo_form/
#### Description
* Form을 통해 Todo의 4개 필드를 입력받는 페이지
* Create 버튼으로 접근했을 경우 Todo 생성을 처리
* Update 버튼으로 접근했을 경우 Todo 수정을 처리
* <img src="/img/create_todo.jpg" width="50%" height="50%">
* <img src="/img/update_todo.jpg" width="50%" height="50%">

## Todo table schema
|id|todo_name|pub_date|parent_todo|priority|
|--|---------|--------|-----------|--------|
|1|프로젝트 설계 구상|2019-10-27 19:40:00|null|1|
|2|CRUD 기능 구현|2019-10-27 19:41:00|null|2|
|3|Create 기능 구현|2019-10-27 19:42:00|2|2|
|4|Read 기능 구현|2019-10-27 19:43:00|2|2|

* id : 식별자, Integer (Primary Key)
* todo_name : Todo 이름, Char (max_length=256)
* pub_date : 작성 날짜, Datetime (yyyy-mm-dd hh:MM:ss)
* parent_todo : 상위 Todo, Foreign Key (Reference on Todo table)
* priority : 우선 순위, Integer

## 추가 기능
* Logging
  * backend API 처리 중 logging 추가
  * 코드 동작 파악 및 error 발생 시의 bug tracking을 위하여 추가
* Unit test
  * tests.py 파일
  * Test run command : python manage.py test
  * 코드 수정 시 API의 error 발생 여부를 빠르게 체크하기 위하여 사용
* 하위 Todo 추가 기능
  * 임의의 Todo에 소속된 하위 Todo를 추가할 수 있음
  * 하위 Todo를 통하여 상위 Todo를 세부적으로 분류하여 저장 및 관리 가능

## Error handling
* Get Todo list API
  * id=parent_id인 Todo가 존재하지 않을 경우
    * Request Example : /b/todo/?parent_id=99999 (id=99999인 Todo가 존재하지 않을 경우)
    * Response : {"todo_list: []} (empty todo_list)
      * Status Code : 200
  * parent_id가 정수가 아닐 경우
    * Request Example : /b/todo/?parent_id=aaa
    * Response : Bad Request(invalid parent_id)
      * Status Code : 400
* Get Todo item API
  * id=todo_id인 Todo가 존재하지 않을 경우
    * Request Example : /b/todo/99999 (id=99999인 Todo가 존재하지 않을 경우)
    * Response : Bad Request(Wrong Todo ID)
      * Status Code : 400
* Create Todo API
  * Invalid Form Data일 경우
    * Request Example : pub_date 필드의 값이 "asdf"와 같이 invalid할 경우
    * Response : Bad Request(invalid form data)
      * Status Code : 400
* Update Todo API
  * id=todo_id인 Todo가 존재하지 않을 경우 : Get Todo item API와 동일하게 처리
  * Invalid Form Data일 경우 : Create Todo API와 동일하게 처리
* Delete Todo API
  * delete_id가 정수가 아닐 경우 : Get Todo list API와 동일하게 처리
  * id=delete_id인 Todo가 존재하지 않을 경우
    * Request Example : /b/todo/?delete_id=99999 (id=99999인 Todo가 존재하지 않을 경우)
    * Response : Bad Request(invalid delete_id)
      * Status Code : 400
      
## Language/Library Version
### Backend
* Python==3.6.8
* Django==2.2.6

### Frontend
* jQuery-3.4.1
