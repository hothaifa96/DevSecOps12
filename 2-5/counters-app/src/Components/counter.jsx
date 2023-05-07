import React, { Component } from 'react';

class Counter extends Component {
    state ={
    };

    render() { 
        
        const { increment , mydelete ,id} = this.props;
        return (
        <div>
            <span className='m5' style={this.style} >{this.formatCount()} </span>
            <button  
            onClick={increment}
             className="btn btn-success btn-sm"
             > + </button>
             
            <button onClick={mydelete}
             className="btn btn-danger m-2 btn-sm"
             >Delete</button>

        </div>);
    }

    componentDidUpdate(prevState,prevProps){
        // AJAX 
        console.log('prevState-',prevState)
        console.log('prevProps-',prevProps)
    }
   
    formatCount(){
        return this.props.value===0? 'Zero': this.props.value;
    }

    componentWillUnmount(){
        console.log(' see you again ohhh oooooooh ohhhhh o');
    }
}
 
export default Counter;



