import {Navigate} from "react-router";
import {AppLayout} from "./AppLayout.tsx";
import BlackoutMain from "./components/blackout/BlackoutMain.tsx";
import Config from "./components/config/Config.tsx";
import Health from "./components/health/Health.tsx";
import Downloads from "./components/downloads/Downloads.tsx";
import Menu from "./components/menu/Menu.tsx";

export const routes = [
    {
        element: <AppLayout/>,
        children: [
            {path: '/', element: <Navigate to="/learn" replace/>},
            {
                path: '*',
                element: <Menu/>,
                children: [
                    {path: 'learn', element: <Config/>},
                ]
            },
        ]
    }
];
