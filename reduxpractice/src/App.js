import { createContext, useState } from 'react';
import Child from './components/Child';
import CreateTodo from './components/createTodo';
import TodoList from './components/todoList';

export const GlobalInfo = createContext()

function App() {
  const [color, setColor] = useState('green');

  const getDay = (item) => {
    console.log(item);
  }
  
  return (
    <GlobalInfo.Provider value={{color: color, getDay: getDay}}>
      <div className='createTodo'>
        {/* <CreateTodo />
        <hr />
        <TodoList /> */}
        <p>App components</p>
        <Child />
      </div>
    </GlobalInfo.Provider>
  );
}

export default App;
