import React from 'react';
import ReactDOM from 'react-dom';
import configureStore from './store/store.js';
import {createDate, fetchDate} from './actions/dates_actions.js';

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
  let store = configureStore();
  ReactDOM.render(<Hello/>, document.getElementById('root'));
  window.createDate = createDate;
  window.fetchDate = fetchDate;
  window.store = store;
});
