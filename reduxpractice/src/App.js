import { createContext, useState, useEffect } from 'react';
import Child from './components/Child';
import CreateTodo from './components/createTodo';
import TodoList from './components/todoList';
import AuthProvider from './provider/authProvider';
import Routes from './routes';

export const GlobalInfo = createContext()

// function useCustom(){
//   const [value, setValue] = useState('');
//   useEffect(()=>{
//     setValue('updated');
//   }, [])
//   return value;
// }

function App() {
  const [color, setColor] = useState('green');

  // const value = useCustom();
  // console.log('value', value)

  const getDay = (item) => {
    console.log(item);
  }
  
  return (
    // <GlobalInfo.Provider value={{color: color, getDay: getDay}}>
    //   <div className='createTodo'>
    //     {/* <CreateTodo />
    //     <hr />
    //     <TodoList /> */}
    //     <p>App components</p>
    //     <Child />
    //   </div>
    // </GlobalInfo.Provider>
    <AuthProvider>
      <Routes />
    </AuthProvider>
  );
}

export default App;
