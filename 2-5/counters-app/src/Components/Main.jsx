import React from "react";
import { Redirect, Route, Switch } from "react-router-dom";
import Hello from './hello';
import Movies from './movies';
import CountersList from './app';
import Login from "./login";

const Main = (props) => {
    return ( 
        <React.Fragment>
            <Switch>
                <Route path="/Movies" component={ Movies } />
                <Route path="/Counter" component={CountersList} />
                <Redirect from="/hello"  to="/Movies" />
                <Route path="/login/:name/:password" component={Movies}  />
                <Route path="/login" component={Login}  />
                <Route path="/:year?"  render={ (props) => <Hello name="hodi"
                 {...props}/>} />
            </Switch>
        </React.Fragment>
     );
}   
 
export default Main;