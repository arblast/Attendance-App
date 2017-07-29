import {CREATE_ATTENDEE, FETCH_ATTENDEES, receiveAttendees} from '../actions/attendees_actions.js';
import {fetchAttendees, createAttendee} from '../util/attendees_api_util.js';

const AttendeeMiddleware = store => next => action => {
  let success = (data) => store.dispatch(receiveAttendees(data.attendees));
  let error = (data) => console.log(error);
  switch(action.type) {
    case CREATE_ATTENDEE:
      createAttendee(action.attendeeParams, success, error);
      return next(action);
    case FETCH_ATTENDEES:
      fetchAttendees(success, error);
      return next(action);
    default:
      return next(action);
  }
}

export default AttendeeMiddleware;
