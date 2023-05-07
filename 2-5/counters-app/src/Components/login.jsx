import React, { Component } from 'react';



class Login extends Component {
    state = {  } 

    userEmail=React.createRef();

     handleOnSubmit=(e)=>{
        e.preventDefault();
         const email= this.userEmail.current.value;
            
     }

    render() { 
        return (
            <form className='m-4'  >
                <div className="mb-3">
                    <label htmlFor="email" className="form-label">Email address</label>
                    <input name='mail' ref={this.userEmail} id="email"  type="email" className="form-control" aria-describedby="emailHelp"/>
                </div>
                <div className="mb-3">
                    <label htmlFor="password" className="form-label">Password</label>
                    <input  name='password' type="password" className="form-control" id="password"/>
                </div>
                <div className="mb-3 form-check">
                    <input type="checkbox" className="form-check-input" id="exampleCheck1"/>
                    <label className="form-check-label" htmlFor="">Check me out</label>
                </div>
            <button type="submit" className="btn btn-primary" >Submit</button>
            </form>
        );
    }
}
 
export default Login ;