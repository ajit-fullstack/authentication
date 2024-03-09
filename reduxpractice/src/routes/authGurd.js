import { Navigate, Outlet } from 'react-router-dom';
import { useAuth } from '../provider/authProvider';

export const AuthGurd = () =>{
    const { token } = useAuth();
    if (!token){
        return <Navigate to="/login" />;
    }
    return <Outlet />;
}