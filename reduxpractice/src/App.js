import CreateTodo from './components/createTodo';
import TodoList from './components/todoList';

function App() {
  return (
    <div className='createTodo'>
      <CreateTodo />
      <hr />
      <TodoList />
    </div>
  );
}

export default App;
