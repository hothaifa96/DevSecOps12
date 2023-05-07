import { Link, Route } from "react-router-dom";
import Movies from './movies';
import CountersList from './app';
import Hello from './hello';


const NavBar = props => {
    const {len , amount} = props;
    return (  
    <nav class="navbar bg-light">
        <div class="container-fluid"> 
           <Link  className="m-3" to="/2022">Homepage</Link>
           <Link className="m-3" to="/Counter">Counters</Link>
           <Link className="m-3" to="/Movies">Movies</Link>
           <Link className="m-3" to="/login">Login</Link>
    </div>
    </nav>
 );
}
 
export default NavBar;
