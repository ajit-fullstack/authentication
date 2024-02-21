import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { Box, Button, TextField, Alert } from '@mui/material';

function ChangePassword() {

    const [error, setError] = useState({
        status: false,
        msg: "",
        type: ""
    });
    const navigate = useNavigate();

    const handleSubmit = (e) =>{
        e.preventDefault();
        const data = new FormData(e.currentTarget);
        const actualData = {
            password: data.get('password'),
            confirmation_password: data.get('confirmation_password'),
        }
        if (actualData.password && actualData.confirmation_password){
            if (actualData.password === actualData.confirmation_password){
                console.log(actualData);
                document.getElementById('password-change-form').reset();
                setError({status: true, msg: "Password Changed Sucessfully.", type: 'success'});
                // navigate('/login');
                setTimeout(()=>{
                    navigate('/login');
            }, 3000);
        }else{
            setError({status: true, msg: "Password and confirm password does't match", type: 'error'});
        }
        }else{
            setError({status: true, msg: "All fields are required", type: 'error'})
        }
    }

  return (
    <Box sx={{display: 'flex', flexDirection: 'column', flexWrap: 'wrap', maxWidth: 600, mx: 4}}>
        <h1>Change Password</h1>
        <Box component='form' onSubmit={handleSubmit} noValidate sx={{mt: 1}} id="password-change-form">
            <TextField margin='normal' required fullWidth id='password' name='password' label='New Password' type='password' />
            <TextField margin='normal' required fullWidth id='confirmation_password' name='confirmation_password' label='Confirm Password' type='password' />
            <Box textAlign="center">
                <Button type='submit' variant='contained' sx={{mt:3, mb: 2, px: 5}}>Update</Button>
            </Box>
            {error.status ? <Alert severity={error.type}>{error.msg}</Alert> : ''}
        </Box>
    </Box>
  )
}

export default ChangePassword;