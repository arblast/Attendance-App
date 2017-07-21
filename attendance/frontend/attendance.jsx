import React from 'react';
import ReactDOM from 'react-dom';

let Hello = () => {
        return (
            <h1>
            Hello, React!
            </h1>
          )
        };

document.addEventListener('DOMContentLoaded', () => {
  const root = document.getElementById('root');
  ReactDOM.render(<Hello/>, document.getElementById('root'));
});
