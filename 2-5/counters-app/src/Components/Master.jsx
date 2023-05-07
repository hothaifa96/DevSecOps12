import React, { Component } from 'react';
import CountersList from './app';
import NavBar from './navbar';
import Main from './Main';

class Master extends Component {
    state = {  } 
    render() { 
        return (
            <React.Fragment>
                <NavBar/>
                <Main classes="bg-danger"/>
            </React.Fragment>
        );
    }
}
 
export default Master;