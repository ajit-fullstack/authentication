import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import { useAuth } from '../provider/authProvider';
import { AuthGurd } from './authGurd';
import Child from '../components/Child';
import CreateTodo from '../components/createTodo';
import TodoList from '../components/todoList';

const Routes = () => {
    const { token } = useAuth();

    const routesForPublic = [
        {
            path: '/',
            element: <Child />
        },
        {
            path:"/service",
            element:<div>Service Page</div>,
        },
        {
            path: "/about-us",
            element: <div>About Us</div>
        }
    ];

    // const routesForAuthenticatedOnly = [
    //     {
    //         path: '',
    //         element: <AuthGurd /> ,
    //         children: [
    //             {
    //                 path: '/',
    //                 element: <div>User Home Page</div>
    //             },
    //             {
    //                 path: "/profile",
    //                 element: <div>User Profile</div>
    //             },
    //             {
    //                 path: '/logout',
    //                 element: <div>Logout</div>
    //             }
    //         ]
    //     }
    // ];

    // const routesForNotAuthenticatedOnly = [
    //     {
    //         path: '/',
    //         element: <div>Home Page</div>
    //     },
    //     {
    //         path: '/login',
    //         element: <div>Login</div>
    //     }
    // ];

    const router = createBrowserRouter([
        ...routesForPublic,
        // ...(!token ? routesForAuthenticatedOnly : []),
        // ...routesForNotAuthenticatedOnly
    ]);

    return <RouterProvider router={router} />
}

export default Routes;
