import React from 'react';
import ReactDOM from 'react-dom';

let Hello = () => {
        return (
            <h1>
            Welcome to Attendance App!
            </h1>
          )
        };

document.addEventListener('DOMContentLoaded', () => {
  const root = document.getElementById('root');
  ReactDOM.render(<Hello/>, document.getElementById('root'));
});
