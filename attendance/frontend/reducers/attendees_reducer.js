import { RECEIVE_ATTENDEES } from '../actions/attendees_actions';
import { merge } from 'lodash';


const AttendeeReducer = (oldState=[], action) => {
  Object.freeze(oldState);
  switch (action.type) {
    case RECEIVE_ATTENDEES:
      return action.attendees;
    default:
      return oldState;
  }
};

export default AttendeeReducer;
