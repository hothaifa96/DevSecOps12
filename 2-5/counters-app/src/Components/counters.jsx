import div, { Component } from 'react';
import Counter from './counter';

class Counters extends Component {
    state = { 
        
     } 
    
    render() { 
        const {myObjects,myDelete,myIncrement} =this.props;
        return (
            <div>
                {myObjects.map(val =>(
                    <Counter 
                    key={val.id} 
                    id={val.id}  
                    value={val.value} 
                    mydelete={()=>myDelete(val.id)}
                    increment={()=>myIncrement(val)}>
                    
                     </Counter>
                    ))}
            </div>
        );
    }
}
 
export default Counters;