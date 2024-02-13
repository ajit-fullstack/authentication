import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { Box, Button, TextField, Alert, FormControl, FormControlLabel, Checkbox } from '@mui/material';

function Regestration() {
  const [error, setError] = useState({
    status: false,
    msg: "",
    type: ""
  })
  const navigate = useNavigate()
  const handleSubmit = (e) =>{
    e.preventDefault();
    const data = new FormData(e.currentTarget);
    const actualData = {
      tc: data.get('tc'),
      name: data.get('name'),
      email: data.get('email'),
      password: data.get('password'),
      confirmation_password: data.get('confirmation_password'),
    }
    if (actualData.name && actualData.email && actualData.password && actualData.tc !== null){
      if (actualData.password === actualData.confirmation_password){
        console.log(actualData);
        document.getElementById('regestration-form').reset();
        setError({status: true, msg: "Regestration sucessfull", type: 'success'});
        // navigate('/');
      }
      else{
        setError({status: true, msg: "Password and confirm password does't match", type: 'error'});
      }
    }else{
      setError({status: true, msg: "All fields are required", type: 'error'})
    }
  }
  return (
    <Box component='form' noValidate sx={{mt: 1}} id="regestration-form" onSubmit={handleSubmit}>
      <TextField margin='normal' required fullWidth id='email' name='email' label='Email Address' />
      <TextField margin='normal' required fullWidth id='name' name='name' label='Name' />
      <TextField margin='normal' required fullWidth id='password' name='password' label='Password' type='password' />
      <TextField margin='normal' required fullWidth id='confirmation_password' name='confirmation_password' label='Confirm Password' type='password' />
      <FormControlLabel control={<Checkbox value="agree" color='primary' name='tc' id='tc' />} label="I agree to terms and condition." />
      <Box textAlign="center">
        <Button type='submit' variant='contained' sx={{mt:3, mb: 2, px: 5}}>Join</Button>
      </Box>
      {error.status ? <Alert severity={error.type}>{error.msg}</Alert> : ''}
    </Box>
  )
}

export default Regestration;