import { combineReducers } from 'redux';
import { attendees_reducer} from './attendees_reducer.js';

export default combineReducers({
  attendees: attendees_reducer
});
