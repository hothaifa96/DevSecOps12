import React, { Component } from 'react';
class Movie extends Component {
    state = {  } 

    render() { 
        return (
            <tr>
                <th>{this.props.movie.id}</th>
                <th>{this.props.movie.name}</th>
                <th>{this.props.movie.length}</th>
                <th>{this.props.movie.genre}</th>
                <th><button className="btn btn-danger btn-sm" 
                onClick={this.props.delete}>Delete</button></th>
                <th><button 
                onClick={this.props.patch}
                className="btn btn-warning btn-sm">Patch</button></th>
            </tr>
        );
    }
}
 
export default Movie;