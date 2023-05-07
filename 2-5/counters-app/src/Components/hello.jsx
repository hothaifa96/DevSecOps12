import { Component } from "react";

class Hello extends Component {
    render(){
    return ( 

        <p>{this.props.match.params.year}</p>
        
     );
    }
}
 
export default Hello;