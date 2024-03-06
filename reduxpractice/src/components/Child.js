import React, {useContext} from 'react'
import {GlobalInfo} from '../App';

function Child() {

  const day = "sunday"
  const {color, getDay} = useContext(GlobalInfo);
  console.log(color);
  
  return (
    <div>
        <p>Child Conponen</p>
        <button onClick={ ()=> getDay(day)}>save</button>
    </div>
  )
}

export default Child