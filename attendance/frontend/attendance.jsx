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
  window.test = () => { $.ajax({
    url: "/attendanceapp/attendee",
    success: (e) => console.log(e),
    error: (e) => console.log(e)
    })}
  ReactDOM.render(<Hello/>, document.getElementById('root'));
});
