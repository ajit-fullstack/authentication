import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addTodo } from '../redux/slices/todoSlice';

function CreateTodo() {
  const [todo, setTodo] = useState('');

  const dispatch = useDispatch()

  const clickHandler = () => {
    dispatch(addTodo(todo));
    setTodo('');
  }

  return (
    <div className='createTodo totalCenter'>
      <input 
        type='text'
        value={todo}
        className='padding-10 input'
        placeholder='Enter todos here...'
        onChange={(e) => setTodo(e.target.value)}
      />
      <button className='btn' onClick={clickHandler}> + </button>
    </div>
  )
}

export default CreateTodo;