import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Button, CssBaseline, Grid, Typography } from '@mui/material';
import ChangePassword from './auth/ChangePassword';

function Dashboard() {
  const navigate = useNavigate();
  const handleLogout = () =>{
    console.log('Logout');
    navigate('/login');
  }
  
  return (
    <>
      <CssBaseline />
      <Grid container>
        <Grid item sm={4} sx={{backgroundColor: 'gray', p: 5, color: 'white'}}>
          <h1>Dashboard</h1>
          <Typography variant='h5'>Email: ajitpathak0448@gmail.com</Typography>
          <Typography variant='h6'>Name: Ajit Kumar</Typography>
          <Button variant='contained' size='large' color='warning' onClick={handleLogout} sx={{mt: 8}}>Logout</Button>
        </Grid>
        <Grid item sm={8}>
          <ChangePassword />
        </Grid>
      </Grid>
    </>
  )
}

export default Dashboard