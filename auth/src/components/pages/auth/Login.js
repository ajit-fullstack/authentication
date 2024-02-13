import React from 'react';
import { Box, Button, TextField, Alert } from '@mui/material';

function Login() {
  return (
    <Box component='form' noValidate sx={{mt: 1}} id="login-form">
      <TextField required fullWidth id='email' name='email' label='Email Address' />
      <TextField required fullWidth id='password' name='password' label='Password' />
    </Box>
  )
}

export default Login;