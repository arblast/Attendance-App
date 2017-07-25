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
  let csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
  function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });
  window.test = () => { $.ajax({
    type: "POST",
    data: {first_name: "test", last_name: "two", club: "Club"},
    url: "/attendanceapp/attendee/",
    success: (e) => console.log(e),
    error: (e) => console.log(e)
    })}
  ReactDOM.render(<Hello/>, document.getElementById('root'));
});
