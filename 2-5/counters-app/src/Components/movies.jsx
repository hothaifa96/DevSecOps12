import React, { Component } from 'react';
import Movie from './movie';
class Movies extends Component {
    state = { 
        moviesList:[
            {id:1,name:'taken',length:2.22,genre:'comedy'},
            {id:2,name:'dumb and dumber to',length:2.22,genre:'comedy'},
            {id:3,name:'gosto',length:2.22,genre:'comedy'},
            {id:4,name:'kongfu panda',length:2.22,genre:'comedy'}
        ]
     } 


    render() { 
        return (
            <table className='table'>
                <thead>
                    <tr>
                        <th>id</th>
                        <th>name</th>
                        <th>length</th>
                        <th>genre</th>
                    </tr>
                </thead>
                <tbody>
                { this.state.moviesList.map(mv =>
                    <Movie movie={mv} key={mv.id} 
                    delete={()=>this.handleDelete(mv.id)}
                    patch={()=>this.handlePatch(mv.id)}
                    ></Movie>)}
    
                </tbody>
            </table>
        );
    }

    handleDelete=(movieId)=>{
        const moviesList=this.state.moviesList.filter(val => val.id !== movieId);
        this.setState({moviesList})
    }
    
    handlePatch=(movieId)=>{
        const moviesList=this.state.moviesList.map(val => {
        if(val.id == movieId)
            val.name='null'
         return val; 
    });
        this.setState({moviesList})
    }
}
 
export default Movies;