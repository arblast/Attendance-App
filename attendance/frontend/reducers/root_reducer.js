import { combineReducers } from 'redux';
import AttendeeReducer from './attendees_reducer.js';

export default combineReducers({
  attendees: AttendeeReducer
});
