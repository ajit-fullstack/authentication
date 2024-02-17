import React from 'react';
import { useSelector, useDispatch} from 'react-redux';
import { removeTodo } from '../redux/slices/todoSlice'; 
 
function TodoList() {

  const todoAll = useSelector((state) => state.todo.todos);

  const dispatch = useDispatch()

  return (
    <div className='todoList'>
      {todoAll.map((element, index) => (
          <tr key={index}>
            <td width='100px'>{index + 1}.</td>
            <td width='90%' style={{"textAlign": "left", "padding-left": "30px"}}>{element.todo}</td>
            <td width='100px'>
              <button className='color' onClick={() => dispatch(removeTodo(element.id))}>Delete</button>
            </td>
          </tr>
      ))}
    </div>
  )
}

export default TodoList;